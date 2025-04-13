# playwright_demo
Playwright Demo using python testing against Wikipedia.com
=======
# Playwright Demo Automation Testing

## Overview

This project demonstrates how to automate web browser interactions using [Playwright](https://playwright.dev/). The tests are designed to ensure consistent and reliable functionality of web applications by simulating user actions and verifying behaviors.

## Project Structure

```
playwright_demo/
├── tests/               # Contains all the test scripts
│   └── example.spec.ts  # Sample test script
├── config/              # Configuration files
│   └── playwright.config.ts  # Playwright configuration file
├── package.json         # Project dependencies and scripts
├── tsconfig.json        # TypeScript configuration
├── pytest.ini           # pytest configuration (if applicable)
└── README.md            # This file
```

## Prerequisites

To get started with this project, make sure you have the following installed:

- **Python** (v3.7 or later)
- **Node.js** (v14.0 or later)
- **npm** (Node package manager)
- **pytest** (for running tests with pytest)

### Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/MarwanSultan/playwright_demo.git
cd playwright_demo
npm install
```

For pytest integration, you also need to install the Playwright pytest plugin:

```bash
pip install pytest-playwright
```

### Configure pytest

Create a `pytest.ini` file in the root of your project to configure pytest behavior:

```ini
[pytest]
addopts = --maxfail=1 --disable-warnings -q
```

This configuration will stop after the first failure, disable warnings, and make the output less verbose.

## Setup & Configuration

### Playwright Configuration File

Playwright configuration settings are defined in `playwright.config.ts`. This file includes the following:

- **Browsers**: Supported browsers (Chromium, Firefox, WebKit)
- **Timeouts**: Default timeouts for test execution
- **Base URL**: The base URL for your application (adjust if needed)

Example of the `playwright.config.ts` setup:

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 1,
  use: {
    baseURL: 'http://localhost:3000', // Set your app's base URL
    headless: true, // Run tests in headless mode
    browserName: 'chromium',
  },
});
```

### TypeScript Support

This project uses TypeScript. Ensure you have the required TypeScript dependencies:

```bash
npm install typescript ts-node --save-dev
```

## Running the Tests with pytest

To run Playwright tests using **pytest**, you can use the following command:

```bash
pytest
```

This command will automatically find all the test files (files starting with `test_` or ending with `_test.py`), and execute the test cases within.

### Running Tests in Specific Browser with pytest

If you want to run your tests in a specific browser, you can set the browser in the `pytest-playwright` settings. You can specify the browser in your test or through environment variables.

Example of running tests with `pytest` for a specific browser:

```bash
pytest --browser=chromium
pytest --browser=firefox
pytest --browser=webkit
```

### Running Tests in Headless Mode

By default, Playwright tests are run in headless mode. However, if you wish to run tests with the browser's UI for debugging purposes, set the `headless` configuration to `false` in your `playwright.config.ts`.

Example:

```typescript
use: {
  headless: false, // Run in headful mode (with UI)
}
```

### Running Tests with Debug Information

To run tests with debug information, you can use the following:

```bash
pytest --playwright-dump-console
```

This will dump the browser console logs, which can help diagnose test failures.

## Writing Tests with pytest

To write tests with pytest, you should use the `pytest-playwright` plugin. Here's an example of a basic test:

### Example Test (using pytest):

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

def test_title(browser):
    page = browser.new_page()
    page.goto("http://localhost:3000")
    title = page.title()
    assert title == "Playwright Demo"
    page.close()
```

### Notes:
- This test launches the Chromium browser, navigates to the specified URL, and checks if the page title matches the expected value.
- You can use Playwright's API (`sync_playwright`) to interact with the browser in a synchronous way in your pytest test cases.

## CI/CD Integration

This project can easily be integrated into a CI/CD pipeline. Below is an example configuration for GitHub Actions:

```yaml
name: Playwright Tests

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest-playwright
          npm install
      - run: npx playwright install
      - run: pytest
```

## Best Practices

- **Use Page Objects**: Organize selectors and actions into reusable objects for better maintainability.
- **Leverage Test Hooks**: Use before/after hooks to set up test data or clean up after tests.
- **Parallel Testing**: Run tests in parallel across multiple browser instances for faster feedback.
- **Reporting**: Configure test reports to track and analyze results (e.g., using Playwright’s built-in HTML reports or third-party tools like Allure).
- **Test Isolation**: Keep tests independent by resetting the application state between tests.
- **Headless Testing**: Run tests in headless mode for faster execution, especially in CI environments.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Ensure your code adheres to the existing style and includes relevant tests.

### Issues and Feedback

For any issues or feedback, please open an issue in the [GitHub repository](https://github.com/MarwanSultan/playwright_demo/issues).

## License

This project is licensed under the MIT License.
>>>>>>> playwright_demo
