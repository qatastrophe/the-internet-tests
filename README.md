# The Internet Project

## Prerequisites

- Python 3.12+
- Docker (optional, for container runs)

## Install and run tests locally

1. Create and activate a virtual environment:

	 - Unix:

		 ```bash
		 python -m venv .venv
		 source .venv/bin/activate
		 ```

	 - Windows (PowerShell):

		 ```powershell
		 python -m venv .venv
		 .\.venv\Scripts\Activate.ps1
		 ```

2. Install Python dependencies and Playwright browsers:

	 ```bash
	 pip install -r requirements.txt
	 python -m playwright install --with-deps
	 ```

3. (Optional) Set the base URL (defaults to https://the-internet.herokuapp.com):

	 - Unix:

		 ```bash
		 export PYTEST_BASE_URL=https://the-internet.herokuapp.com
		 ```

	 - Windows (PowerShell):

		 ```powershell
		 $env:PYTEST_BASE_URL = 'https://the-internet.herokuapp.com'
		 ```

4. If tests require authentication, set `USER` and `PASSWORD` environment variables before running tests. You can store these variables in `.env` file. Refer to `env.example` for example

5. Run the test suite with pytest. You may pass the Playwright `--browser` option (chromium|firefox|webkit). chromium is default value:

	 ```bash
	 pytest -v
	 # or explicitly choose a browser
	 pytest --browser firefox -v
	 ```

Examples:

```bash
# Run a specific test file
pytest tests/test_login.py -q

# Run by tag
pytest -m login

# Run on a specific environment
PYTEST_BASE_URL='http://...'  pytest

# Run tests with Firefox and verbose output
pytest --browser firefox -v
```

## Run tests in Docker

1. Build the test image (from repository root):

```bash
docker build -t the-internet-tests .
```

2. Run the image. Pass environment variables (like `USER`, `PASSWORD`, or `PYTEST_BASE_URL`) with `-e` and any pytest/Playwright flags after the image name.

```bash
# Example: run with Firefox, verbose output, and credentials
docker run --rm \
	-e USER=myuser \
	-e PASSWORD=mypassword \
	the-internet-tests --browser firefox -v
```

Notes:

- The Dockerfile installs Python dependencies and Playwright browsers (`python -m playwright install --with-deps`).
- The container's `ENTRYPOINT` runs `pytest`, so flags after the image name are forwarded to pytest.

## CI
Tests in CI run in parallel for chrome, firefox and webkit. `USER` and `PASSWORD` are kept in repository secrets

## Troubleshooting

- If Playwright browsers are missing locally, run `python -m playwright install --with-deps`.
- For tests that require `USER`/`PASSWORD`, ensure those env vars are set; `conftest.py` will raise an exception if missing.

---

Files:

- Tests live in the `tests/` folder and page objects in the `pages/` folder.