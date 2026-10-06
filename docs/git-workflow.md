# Git Workflow

This document describes the Git workflow followed while building the Server Health Monitor project.

## Branch Strategy

The project uses the following primary branches:

- `main` - Stable version of the project.
- `dev` - Development and integration branch.
- `feature/*` - Branches used to develop individual features.
- `chore/*` - Branches used for project configuration and maintenance changes.

The general workflow followed was:

```text
main
  |
  └── dev
       |
       ├── feature/system-info
       |
       ├── feature/disk-monitoring
       |
       ├── feature/python-info
       |
       └── chore/project-config
```

## Development Workflow

### 1. Repository Initialization

The project was initialized as a local Git repository and the default branch was renamed to `main`.

The repository was then connected to GitHub using a remote named `origin`.

A `dev` branch was created from `main` and used as the primary development branch.

---

### 2. System Information Feature

A feature branch named:

```text
feature/system-info
```

was created from `dev`.

The feature added:

- Hostname detection
- Operating system detection

The changes were committed locally and the branch was pushed to GitHub.

A pull request was created with:

```text
feature/system-info → dev
```

The changes were reviewed and merged into `dev`.

After the merge, the local `dev` branch was synchronized with GitHub using `git fetch` and `git pull`.

---

### 3. Disk Monitoring Feature

A second feature branch was created:

```text
feature/disk-monitoring
```

The feature added disk usage monitoring using Python's `shutil` module.

The script displays:

- Total disk space
- Used disk space
- Free disk space

for the C:, D:, and E: drives.

After testing the script locally, the changes were committed and pushed to GitHub.

A pull request was created:

```text
feature/disk-monitoring → dev
```

The pull request was reviewed and merged into `dev`.

The local `dev` branch was then synchronized with the remote repository.

---

### 4. Remote Branch Without a Pull Request

A separate branch was created:

```text
feature/python-info
```

This feature added the Python interpreter version to the health monitor output.

The branch was:

1. Created from `dev`
2. Modified and tested
3. Committed locally
4. Pushed to GitHub

No pull request was created and the branch was not merged into `dev`.

This demonstrated that pushing a branch to a remote repository does not automatically require a pull request or merge.

```text
feature/python-info
        |
      commit
        |
       push
        |
      GitHub

No Pull Request
No Merge
```

The feature therefore remains isolated from the `dev` branch.

---

### 5. Project Configuration

A maintenance branch named:

```text
chore/project-config
```

was created from `dev`.

A `.gitignore` file was added to prevent generated and environment-specific files from being tracked.

The configuration excludes files such as:

- Python cache files
- Python virtual environments
- VS Code settings
- Windows system files
- Log files

The branch was pushed to GitHub and merged into `dev` through a pull request.

---

## Pull Request Workflow

For features intended to become part of the project, the following workflow was used:

```text
dev
 |
 └── feature branch
        |
        ├── Modify files
        ├── Test changes
        ├── Review with git diff
        ├── Stage changes
        ├── Commit changes
        └── Push to GitHub
                 |
                 ▼
            Pull Request
                 |
                 ▼
               dev
```

Before merging each pull request, the base and compare branches were verified to ensure the changes were being merged into the correct destination.

---

## Local and Remote Synchronization

After a pull request was merged on GitHub, the local `dev` branch did not automatically contain the new merge commit.

The following workflow was used:

```bash
git switch dev
git fetch origin
git status
git pull
```

`git fetch origin` updated the local remote-tracking references with the latest information from GitHub.

`git pull` then updated the local `dev` branch to match the updated remote branch.

---

## Final Integration

After development and documentation are complete, the final development branch will be merged into the stable branch using:

```text
dev → main
```

This keeps development work separate from the stable `main` branch until the project is ready for release.

A Git tag will then be used to identify the completed version of the project.