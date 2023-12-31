# selenium-pytest-automation

Pytest Automation with Selenium

# Setup Instructions

## Python Setup

You can download the latest Python version from [Python.org](https://www.python.org/downloads/).

also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

You should also have a Python editor/IDE of your choice.
Good choices include [Visual Studio Code](https://code.visualstudio.com/docs/languages/python) and [PyCharm](https://www.jetbrains.com/pycharm/).

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of
[Microsoft Edge](https://www.microsoft.com/edge)
[Google Chrome](https://www.google.com/chrome/)
and [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).
You can use other browsers with Selenium WebDriver, but the course will use Microsoft Edge, Chrome and Firefox.

You will also need to install the latest versions of the WebDriver executables for these browsers: [EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) for Microsoft Edge, [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

EdgeDriver, ChromeDriver and geckodriver must be installed on the
[system path](<https://en.wikipedia.org/wiki/PATH_(variable)>).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the _Path_ environment variable.

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ msedgedriver
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup

1. Clone this repository.
2. Run `pipenv install` to install the dependencies.
3. Run `pipenv run python -m pytest` to verify that the framework can run tests.

### Project Setup Troubleshooting

A few people attempting to set up this project
encountered the following error when executing `pipenv run python -m pytest`:

```
ModuleNotFoundError: No module named 'atomicwrites'
```

- Upgrade Python to the latest versions. The following worked for me on Windows:
  - Python 3.11.4 (`python --version`)
  - pip 23.1.2 (`pip --version`)
  - pipenv 2023.7.11 (`pipenv --version`)
- Run `pipenv update` from within the project directory.

If upgrades don't work, try forcing package installation:

- Run `pipenv install pytest` from within the project directory.
- Run `pipenv install atomicwrites` from within the project directory.

If these steps don't work in your project, then try to run without pipenv:

- Install Python packages directly using `pip`.
- Run tests directly using `python -m pytest`.
