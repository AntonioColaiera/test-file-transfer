# FileGenerator App

This is a Python application for creating temporary file data for use in testing file transfer, in the specification it fictitiously determines the days of the year in which the noise pollution threshold in Milan was exceeded with the related audio file.
There are two modules present(with the relevant comments in the code):


### file_generator.py

The file_generator.py file is a program that generates a folder and subfolder structure, and creates random files within these subfolders.

The main functions in the file_generator.py file are:

-create_folder(folder_name): Creates a folder if it doesn’t already exist.
-create_subfolders(main_folder, start_year, number_of_subfolders): Creates a random number of subfolders within a main folder.
-create_files(folder_path, year): Creates a random number of files within a given folder.

### test.py

The test.py file contains tests for the create_folder and create_subfolders functions.

The main test functions in the test.py file are:

-test_create_folder(): Tests the create_folder function.
-test_create_subfolders(): Tests the create_subfolders function.

## Requirements

- Python 3.6 or later.

## Installation

1. Clone or copy the repository to your local machine.

2. Navigate to the project directory.

3. There are no external libraries required for this project, so you can run the Python files directly.

## Usage

- To run the main program, navigate to the project directory and run the following command:

```bash
python3 file_generator.py 
```

- To run the tests, use the following command:

```bash
python3 -m unittest test.py
```
