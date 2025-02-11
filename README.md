
```markdown
# Python GUI application demo

This is just a quick simple demo to showcase using a Python-based graphical user interface (GUI) application. It simulates the functions to to load test script files, simulate test execution, view results, and save test results into a file. It does not actually perform any tests.

## Features

- Load test scripts from a file.
- Execute tests with a single click.
- View test results in real-time.
- Save test reports as text files.

## System Requirements

- Python (version 3.x)
- Tkinter library (included with Python)
- PyInstaller (for converting the script to an executable, if needed)

## Installation

1. Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install the required packages by running the following command in your command prompt or terminal:
   ```
   pip install tkinter
   ```

## Usage

1. Open the `DemoCleaningRobotTestTool.py` script in a Python IDE like Visual Studio Code or text editor.
2. Run the script to launch the GUI application.
3. Use the provided interface to load a python test script (default file type), start the test, and save the results.

### Interface Overview

- **Load Test Script**: Click this button to select and load a python test script file (default file type).
- **Start Test**: Click this button to execute the loaded test script.
- **Test Results**: View the output of the test execution here.
- **Save Test Result**: Click this button to save the test results to a .txt file.

## Building the Executable

To create a standalone executable (.exe) for Windows using PyInstaller, follow these steps:

1. Install PyInstaller if you haven't already:
   ```
   pip install pyinstaller
   ```
2. Navigate to the directory containing `DemoCleaningRobotTestTool.py`.
3. Run the following command:
   ```
   pyinstaller --onefile --windowed DemoCleaningRobotTestTool.py
   ```
4. The executable will be created in the `dist` directory.

## Contributing

If you have suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Credits

The basic code is initially generated by Generative AI for quick demo purpose, during manual test and debug, some of the code and functions were modified to enhanced by project owner.


```

