# Python Beginner

- [Python Beginner](#python-beginner)
  - [Getting Started](#getting-started)
    - [Cloning the Repository](#cloning-the-repository)
    - [Setting up a Virtual Environment and Installing the Package](#setting-up-a-virtual-environment-and-installing-the-package)
    - [Completing the Tasks](#completing-the-tasks)
  - [Task 1 - Writing functions, basic python and `pytest`](#task-1---writing-functions-basic-python-and-pytest)
  - [Task 2](#task-2)

## Getting Started

Try to work your way through all of this without using ChatGPT and referring to the actual docs or guides
on the packages you are using.

StackOverflow is a great resource, loads of questions and answers on there. That is mainly what people
used before ChatGPT was a thing.

### Cloning the Repository

Before setting up your environment, you need to clone the repository to your local machine. This will give you access to all the files and code necessary for the project.

1. **Clone the Repository:**
   Open your terminal and navigate to the directory where you want to store the project. Then, run the following command:
   ```sh
   git clone <repository-url>
   ```
   Replace `<repository-url>` with the actual URL of the repository. This command will create a new directory with the project files.

### Setting up a Virtual Environment and Installing the Package

A virtual environment is a self-contained directory that contains a Python installation for a particular version of Python, plus a number of additional packages. It allows you to manage dependencies for different projects separately.

2. **Create a Virtual Environment:**
   Navigate into the project directory you just cloned usign `cd`. To create a virtual environment, run the following command:
   ```sh
   python -m venv venv
   ```
   This command will create a new directory named `venv` inside your project directory. This directory will contain the Python interpreter and a copy of the pip tool.

3. **Activate the Virtual Environment:**
   To start using the virtual environment, you need to activate it. Run the following command:
   ```sh
   source venv/bin/activate
   ```
   After activation, your terminal prompt will change, indicating that you are now working within the virtual environment.

4. **Install the Package:**
   With the virtual environment activated, you can now install the package and its dependencies. This is done using the following command:
   ```sh
   pip install -e .
   ```
   The `-e` flag stands for "editable," which means that any changes you make to the code will be reflected immediately without needing to reinstall the package. This command reads the `pyproject.toml` file to install the package `pyanalytics` and its dependencies, such as `jupyter`, `numpy`, `pandas`, `matplotlib`, and `yfinance`.

5. **Verify the Installation:**
   To ensure everything is installed correctly, you can list all the installed packages in your virtual environment by running:
   ```sh
   pip list
   ```
   You should see `pyanalytics` along with its dependencies listed here.

6. **Deactivate the Virtual Environment:**
   When you are finished working, you can deactivate the virtual environment to return to your system's default Python environment. Simply run:
   ```sh
   deactivate
   ```
   This command will revert your terminal to the global Python environment, allowing you to work on other projects or tasks. You can re-activate the virtual environment using the `source venv/bin/activate` command. While working on this, stay within the the virtual environment so you have access to all the packages you installed with `pip install -e .`

### Completing the Tasks
A few things to keep in mind when completing the tasks
 - `git commit` and `git push` your answers regularly;
 - Do not `git push` to the main branch, push your answers to a separate branch;
 - Make use of a Jupyter notebook to test things and trial solutions. It is always easier to mess around in a Jupyter notebook than code it directly into the editor, unless it is a simple task.

## Task 1 - Writing functions, basic python and `pytest`
In this task, you will be writing Python functions and using pytest to test them. pytest is a simple testing framework for Python that allows you to write test cases to ensure your code works as expected.

**What is `pytest`?**. `pytest` is a tool that helps you test your Python code. It allows you to write test functions that check if your code is working correctly. If your code doesn't work as expected, `pytest` will let you know by showing which tests failed.

**Where to find the tests?** The test cases for your functions are located in the `tests/test_task1.py` file. This file contains test functions for each of the functions you need to implement. Each test function uses simple assertions to check if the output of your function matches the expected result.

**How to run the tests.** To run all the tests, open your terminal, navigate to the root directory of your project, and execute the following command: `pytest tests/test_task1.py` (make sure that your virtual environment is activated). 

**How to run a single test.** If you want to run a single test function, you can specify the test function name using the `-k` option. For example, to run only the `test_convert_radians_to_degrees` test, use: `pytest tests/test_task1.py -k test_convert_radians_to_degrees` which should be the only one that passes as it has already been done for you.

**Task:** Implement the remaining functions in `pyanalytics/task1.py` one by one, and run each test as you go. If you implement the functions correctly, then the tests should pass. If you get confused as to what the functions should do, read the test and it should help you understand the inputs and outputs of the functions. Do not use any packages except pre-installed python packages, `numpy` and `pandas`.

**`git commit` and `git push` as you go.** Commit your changes and push them to GitHub a you go. 

## Task 2
Work your way through the Jupyter notebook in `pyanalytics/task2_aapl_googl_analysis.ipynb`.
