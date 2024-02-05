# Pre-commit Configuration

This repository uses a pre-commit configuration for maintaining code quality. When you clone this repository, please ensure to enable the pre-commit checks.

Follow these steps to enable pre-commit:

1. Install pre-commit. If you're using pip, you can do this by running `pip install pre-commit`.

2. Navigate to the repository's directory and run `pre-commit install`. This will set up the git hook scripts.

Now, pre-commit will run automatically on `git commit`. If there are any issues detected, the commit will be aborted and you'll be shown a description of the issues. Fix the issues and try committing again.

Remember, pre-commit is a tool to help you but is not a replacement for manual review of your code.
