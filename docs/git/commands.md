# Git Complete Commands Reference ⚡

A comprehensive, categorized guide to Git commands from basic snapshotting to advanced debugging and rebase operations.

---

## 🎯 Quick Navigation
- [1. Setup & Initialization](#1-setup-initialization)
- [2. Basic Snapshotting & Staging](#2-basic-snapshotting-staging)
- [3. Branching & Merging](#3-branching-merging)
- [4. Inspecting & History Log](#4-inspecting-history-log)
- [5. Undoing Changes & Reverting](#5-undoing-changes-reverting)
- [6. Remote Repositories](#6-remote-repositories)
- [7. Stashing (Temporary Storage)](#7-stashing-temporary-storage)
- [8. Advanced: Rebase, Cherry-Pick & Bisect](#8-advanced-rebase-cherry-pick-bisect)
- [9. Housekeeping & Internal Inspection](#9-housekeeping-internal-inspection)

---

## 1. Setup & Initialization

| Command | Explanation | Example |
| :--- | :--- | :--- |
| `git init` | Initializes a new empty Git repository in current directory. | `git init` |
| `git init <dir>` | Creates directory and initializes a new repo inside it. | `git init my-app` |
| `git clone <url>` | Clones a remote repository to local machine. | `git clone git@github.com:user/repo.git` |
| `git config` | Views or sets user/repo level parameters. | `git config --global user.name "John"` |

---

## 2. Basic Snapshotting & Staging

| Command | Explanation | Example |
| :--- | :--- | :--- |
| `git status` | Shows state of working directory and staging area. | `git status` |
| `git add <file>` | Adds file changes to staging area. | `git add index.html` |
| `git add .` | Stages all modified, new, and deleted files. | `git add .` |
| `git add -p` | Interactively review and stage code chunks (hunks). | `git add -p` |
| `git commit -m` | Saves staged snapshot into history with a message. | `git commit -m "feat: add user login"` |
| `git commit -am` | Stages tracked modified files and commits in one step. | `git commit -am "fix: header alignment"` |
| `git commit --amend` | Modifies the latest commit (message or staged files). | `git commit --amend -m "Updated message"` |
| `git rm <file>` | Removes file from working tree and stages the removal. | `git rm old_file.py` |
| `git mv <src> <dst>` | Renames/moves a file and stages the change. | `git mv old.txt new.txt` |

---

## 3. Branching & Merging

| Command | Explanation | Example |
| :--- | :--- | :--- |
| `git branch` | Lists all local branches. | `git branch` |
| `git branch -a` | Lists all local and remote-tracking branches. | `git branch -a` |
| `git branch <name>` | Creates a new branch at current commit. | `git branch feature-auth` |
| `git checkout <branch>` | Switches to specified branch. | `git checkout feature-auth` |
| `git switch <branch>` | Modern replacement for switching branches. | `git switch feature-auth` |
| `git checkout -b <name>`| Creates and immediately switches to new branch. | `git checkout -b feature-payment` |
| `git switch -c <name>`  | Modern way to create and switch to new branch. | `git switch -c feature-payment` |
| `git merge <branch>` | Merges target branch into current active branch. | `git merge feature-auth` |
| `git branch -d <name>` | Deletes branch safely (only if fully merged). | `git branch -d feature-auth` |
| `git branch -D <name>` | Force deletes branch even if unmerged. | `git branch -D experiment` |

---

## 4. Inspecting & History Log

```bash
# Simple log history
git log

# Single line clean visual log
git log --oneline

# Graph layout showing branch/merge history
git log --oneline --graph --all

# Show changes introduced in latest commit
git show HEAD

# Compare working directory against staging area
git diff

# Compare staged changes against last commit
git diff --staged

# Compare two branches
git diff main..feature-branch
```

---

## 5. Undoing Changes & Reverting

> ⚠️ **Warning**: Be careful when running destructive commands like `git reset --hard`.

| Level | Command | What it does |
| :--- | :--- | :--- |
| **Discard Unstaged Changes** | `git checkout -- <file>` or `git restore <file>` | Discards local changes in working directory, resetting file to staged/HEAD state. |
| **Unstage Files** | `git restore --staged <file>` or `git reset HEAD <file>` | Removes file from staging area without touching physical file. |
| **Revert Commit (Safe for Shared Repos)** | `git revert <commit_hash>` | Creates a brand-new commit that inverses the changes of specified commit. |
| **Soft Reset** | `git reset --soft HEAD~1` | Moves HEAD back 1 commit. Preserves changes in **Staging Area**. |
| **Mixed Reset (Default)** | `git reset --mixed HEAD~1` | Moves HEAD back 1 commit. Preserves changes in **Working Directory** (unstaged). |
| **Hard Reset** | `git reset --hard HEAD~1` | **DESTRUCTIVE**. Wipes last commit, staging area, and local changes completely. |

---

## 6. Remote Repositories

```bash
# View configured remote servers
git remote -v

# Add a remote repo alias
git remote add origin git@github.com:username/repository.git

# Change URL of existing remote
git remote set-url origin git@github.com:username/new-repo.git

# Fetch updates from remote without merging
git fetch origin

# Download and automatically merge remote changes into current branch
git pull origin main

# Push local commits to remote branch
git push origin main

# Push and set upstream tracking branch
git push -u origin feature-branch

# Delete remote branch
git push origin --delete feature-branch
```

---

## 7. Stashing (Temporary Storage)

Stashing temporarily shelves uncommitted modifications so you can work on something else without committing incomplete work.

```bash
# Stash current work (staged + unstaged)
git stash

# Stash with a descriptive message
git stash save "work in progress on user profile"

# Include untracked files in stash
git stash -u

# List all stashes
git stash list

# Apply latest stash and remove it from stash list
git stash pop

# Apply specific stash without removing from list
git stash apply stash@{1}

# Delete specific stash / clear all stashes
git stash drop stash@{0}
git stash clear
```

---

## 8. Advanced: Rebase, Cherry-Pick & Bisect

### Interactive Rebase (`git rebase -i`)
Rebase rewrites commit history. Use interactive rebase to clean up, combine (squash), edit, or drop commits before merging into main.

```bash
# Rebase current branch onto main
git rebase main

# Interactively clean last 4 commits
git rebase -i HEAD~4
```

*Interactive Rebase Commands (in editor):*
- `p` or `pick`: keep commit as is.
- `r` or `reword`: keep commit, but change commit message.
- `e` or `edit`: stop and modify commit content.
- `s` or `squash`: combine commit into previous commit.
- `d` or `drop`: delete commit.

### Cherry-Picking
Applies specific commit(s) from another branch to current branch.

```bash
git cherry-pick <commit_hash>
```

### Git Bisect (Debugging Bug Origin)
Uses binary search through project history to find which commit introduced a bug.

```bash
# Start bisect session
git bisect start

# Mark current commit as broken/bad
git bisect bad

# Mark an older known working commit as good
git bisect good v1.0.0

# Git will checkout mid-points automatically. Test your app, then mark:
git bisect good   # or git bisect bad

# Once Git finds culprit commit, reset state:
git bisect reset
```

---

## 9. Housekeeping & Internal Inspection

```bash
# View entire reference log (even deleted commits / lost branches)
git reflog

# Restore lost commit via reflog
git checkout -b recovered-branch <commit_hash_from_reflog>

# Check object details (Blob/Tree/Commit)
git cat-file -p <object_hash>

# Check object type
git cat-file -t <object_hash>

# Clean untracked files and directories
git clean -fd

# Run Garbage Collection and optimize repo
git gc --prune=now
```