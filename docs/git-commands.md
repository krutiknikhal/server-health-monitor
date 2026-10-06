# Git Commands Used

This document contains the main Git commands used while building and managing the Server Health Monitor project.

## Repository Initialization

### Initialize a Git Repository

```bash
git init
```

Creates a new local Git repository in the current directory.

### Rename the Current Branch

```bash
git branch -M main
```

Renames the current branch to `main`.

---

## Checking Repository Status

```bash
git status
```

Displays the current branch and shows tracked, modified, staged, and untracked files.

---

## Viewing Changes

### View Unstaged Changes

```bash
git diff
```

Shows changes in tracked files that have not yet been staged.

### View Staged Changes

```bash
git diff --staged
```

Shows the changes that are currently staged and will be included in the next commit.

---

## Staging Changes

```bash
git add <file>
```

Adds a specific file to the staging area.

Example:

```bash
git add health_monitor.py
```

To stage multiple intended files, each file can be added individually before committing.

---

## Creating Commits

```bash
git commit -m "commit message"
```

Creates a commit containing the staged changes.

Examples used in this project include:

```text
feat: add system information monitoring
feat: add disk usage monitoring
feat: add Python version information
chore: add project gitignore
```

---

## Working with Branches

### List Local Branches

```bash
git branch
```

Displays the local branches. The branch marked with `*` is the currently checked-out branch.

### Create and Switch to a New Branch

```bash
git switch -c <branch-name>
```

Example:

```bash
git switch -c feature/disk-monitoring
```

Creates a new branch from the current commit and immediately switches to it.

### Switch Between Existing Branches

```bash
git switch <branch-name>
```

Example:

```bash
git switch dev
```

Changes the working directory to the version represented by the selected branch.

### Rename a Branch

```bash
git branch -m <new-name>
```

Renames the current branch.

### Delete a Local Branch

```bash
git branch -d <branch-name>
```

Safely deletes a local branch when Git determines that its work has already been merged.

---

## Working with a Remote Repository

### Add a Remote Repository

```bash
git remote add origin <repository-url>
```

Connects the local repository to a remote repository and gives it the name `origin`.

### View Configured Remotes

```bash
git remote -v
```

Displays the remote repositories configured for the local repository.

---

## Pushing Branches

```bash
git push -u origin <branch-name>
```

Pushes a local branch to GitHub.

The `-u` option sets the remote branch as the upstream tracking branch.

Example:

```bash
git push -u origin feature/disk-monitoring
```

After upstream tracking is configured, future pushes can normally use:

```bash
git push
```

---

## Fetching Remote Changes

```bash
git fetch origin
```

Downloads information about new commits and branches from the remote repository and updates remote-tracking references.

It does not directly modify the files in the current working branch.

---

## Pulling Remote Changes

```bash
git pull
```

Fetches remote changes and integrates the appropriate remote branch into the current local branch.

In this project, it was used after pull requests were merged on GitHub to synchronize the local `dev` branch.

---

## Viewing Commit History

```bash
git log --oneline --decorate --all --graph
```

Displays the repository history in a compact graphical format.

It was useful for viewing:

- Commit history
- Branch relationships
- Merge commits
- Local branches
- Remote-tracking branches
- Current `HEAD`

---

## Viewing Branch Tracking Information

```bash
git branch -vv
```

Displays local branches along with their latest commits and upstream tracking branches.

Example:

```text
feature/python-info [origin/feature/python-info]
```

shows that the local branch tracks its corresponding remote branch.

---

## Git Restore

```bash
git restore <file>
```

Restores changes in a working-directory file back to its last committed version.

This should be used carefully because uncommitted changes can be lost.

---

## Git Ignore

The `.gitignore` file tells Git which untracked files or directories should normally not be added to version control.

Examples used in this project include:

```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.vscode/
Thumbs.db
*.log
```

A file that is already tracked by Git is not automatically untracked simply because it is later added to `.gitignore`.

---

## Git Tags

### Create an Annotated Tag

```bash
git tag -a v1.0.0 -m "Server Health Monitor v1.0.0"
```

Creates an annotated tag named `v1.0.0` for the current commit.

Annotated tags contain additional metadata such as the tagger, date, and tag message.

### View Tag Information

```bash
git show v1.0.0
```

Displays information about the tag and the commit it references.

### Push a Tag to GitHub

```bash
git push origin v1.0.0
```

Publishes the local tag to the remote GitHub repository.

### List Tags

```bash
git tag
```

Displays the tags available in the local repository.

## Typical Workflow Used in This Project

```bash
git status
git diff
git add <file>
git diff --staged
git commit -m "message"
git push
```

For a new feature branch:

```bash
git switch dev
git switch -c feature/example
# Make and test changes
git status
git diff
git add <file>
git diff --staged
git commit -m "feat: add example feature"
git push -u origin feature/example
```

For synchronizing `dev` after a GitHub pull request merge:

```bash
git switch dev
git fetch origin
git status
git pull
```

This workflow helped ensure changes were reviewed before they were committed and that the local repository remained synchronized with GitHub.