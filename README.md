# Guidelines for developing features in Baani

## Setup and Installation

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up environment variables for API keys and tokens.
4. Run `python app.py` to start the Flask server.

## Pre-commit Configuration

This repository uses a pre-commit configuration for maintaining code quality. When you clone this repository, please ensure to enable the pre-commit checks.

Follow these steps to enable pre-commit:

1. Install pre-commit. If you're using pip, you can do this by running `pip install pre-commit`.
2. Navigate to the repository's directory and run `pre-commit install`. This will set up the git hook scripts.

Now, pre-commit will run automatically on `git commit`. If there are any issues detected, the commit will be aborted and you'll be shown a description of the issues. Fix the issues and try committing again.

Remember, pre-commit is a tool to help you but is not a replacement for manual review of your code.

## Feature Development Guidelines




To ensure consistency and maintain code quality, please follow these guidelines when creating new features:

1. Create a directory for the feature in the `integrations` folder, if it doesn't already exist. This will help organize the codebase and make it easier to locate specific features.

2. Create blueprints for all endpoints used in the API. Blueprints provide a clear structure and documentation for the API endpoints, making it easier for other developers to understand and work with the code.

```python
from flask import Blueprint

bp = Blueprint('bp_name', __name__)

@bp.route('/')
def index():
    return "Hello, World!"from flask import Flask
```

3. Create an 'API' folder to manage external APIs.

4. Register each blueprint in root app.py.

```python
from .your_blueprint_file import bp
app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/prefix')
```

Remember to review and test your code thoroughly before committing. These guidelines are meant to maintain a high standard of code quality and improve collaboration among developers.

Happy coding!
