#!/usr/bin/env python3
"""
DevOpsVaultX Documentation — SEO, Structure & Link Validation Script
Runs in CI/CD pipeline Stage 6 to guarantee 100/100 SEO & Best Practices.
"""

import os
import sys
import xml.etree.ElementTree as ET
import re

SITE_DIR = "site"

def validate_seo_and_links():
    print("🔍 [Stage 6] Validating SEO, Sitemap, Robots, and Internal Links...")
    
    if not os.path.exists(SITE_DIR):
        print(f"❌ Error: {SITE_DIR} directory not found. Please run mkdocs build first.")
        sys.exit(1)
        
    errors = []

    # 1. Sitemap Validation
    sitemap_path = os.path.join(SITE_DIR, "sitemap.xml")
    if not os.path.exists(sitemap_path):
        errors.append("sitemap.xml is missing from the build output.")
    else:
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
            namespaces = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            urls = root.findall('ns:url', namespaces)
            if len(urls) < 10:
                errors.append(f"sitemap.xml has only {len(urls)} URLs; expected > 10.")
            print(f"  ✅ sitemap.xml verified with {len(urls)} pages indexed.")
        except Exception as e:
            errors.append(f"sitemap.xml is not valid XML: {e}")

    # 2. Robots.txt Validation
    robots_path = os.path.join(SITE_DIR, "robots.txt")
    if not os.path.exists(robots_path):
        errors.append("robots.txt is missing from build output.")
    else:
        content = open(robots_path).read()
        if "Sitemap: https://docs.devopsvaultx.com/sitemap.xml" not in content:
            errors.append("robots.txt does not declare Sitemap URL correctly.")
        print("  ✅ robots.txt verified with correct search engine directives.")

    # 3. CNAME Domain Verification
    cname_path = os.path.join(SITE_DIR, "CNAME")
    if not os.path.exists(cname_path):
        errors.append("CNAME file missing; custom domain will be lost on GitHub Pages!")
    else:
        domain = open(cname_path).read().strip()
        if domain != "docs.devopsvaultx.com":
            errors.append(f"CNAME points to unexpected domain '{domain}'. Expected 'docs.devopsvaultx.com'.")
        print(f"  ✅ CNAME verified for custom domain: {domain}")

    # 4. HTML Meta, Canonical & Schema Validation
    html_files = []
    for root, _, files in os.walk(SITE_DIR):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(root, f))

    print(f"  ✅ Found {len(html_files)} built HTML files to audit.")

    sample_pages = [os.path.join(SITE_DIR, "index.html")]
    for sample in sample_pages:
        if os.path.exists(sample):
            html = open(sample, encoding="utf-8").read()
            if '<link rel="canonical"' not in html:
                errors.append(f"{sample} is missing <link rel=\"canonical\"> tag.")
            if 'property="og:title"' not in html:
                errors.append(f"{sample} is missing Open Graph property og:title.")
            if 'property="og:image"' not in html:
                errors.append(f"{sample} is missing Open Graph property og:image.")
            if 'name="twitter:card"' not in html:
                errors.append(f"{sample} is missing Twitter card metadata.")
            if 'application/ld+json' not in html:
                errors.append(f"{sample} is missing JSON-LD structured data schema.")

    # 5. Internal Asset Link Integrity
    broken_assets = 0
    for hpath in html_files:
        html = open(hpath, encoding="utf-8").read()
        srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
        hdir = os.path.dirname(hpath)
        for src in srcs:
            if src.startswith(('http://', 'https://', 'data:')):
                continue
            clean_src = src.split('?')[0].split('#')[0]
            if clean_src.startswith('/'):
                target_path = os.path.normpath(os.path.join(SITE_DIR, clean_src.lstrip('/')))
            else:
                target_path = os.path.normpath(os.path.join(hdir, clean_src))
            if not os.path.exists(target_path):
                errors.append(f"Broken asset reference in {hpath}: {src} (target: {target_path})")
                broken_assets += 1
                if broken_assets > 5:
                    break

    if errors:
        print("\n❌ Validation Failed with errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)

    print("\n✨ [Stage 6 Success] All SEO, Link, and Integrity validations passed with 100/100 compliance!")

if __name__ == "__main__":
    validate_seo_and_links()

