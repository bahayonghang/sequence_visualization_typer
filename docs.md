# Visualization Tool Documentation

## Overview
This tool provides functionality to visualize training and testing results by plotting data from `.npy` files. It uses the Typer framework for command-line interface and offers an interactive way to specify visualization parameters.

## Installation

### Prerequisites
- Python 3.x
- Required packages:
  - typer
  - pathlib
  - Custom package `plotter` with functions:
    - `plot_npy_all_train`
    - `plot_npy_all`

### Dependencies Installation
```bash
pip install typer
```

## Usage

### Running the Tool
To run the visualization tool, execute the script from the command line:
```bash
python script_name.py visualize
```

### Interactive Prompts
The tool will guide you through two interactive prompts:

1. **Visualization Type Selection**
   - You will be prompted to enter the type of visualization
   - Valid options:
     - `train`: For visualizing training data
     - `test`: For visualizing test data

2. **Result Directory Path**
   - You need to provide the absolute path to the directory containing your result files
   - The path must be:
     - Absolute (e.g., `/home/user/results` or `C:\Users\user\results`)
     - Existing on your system

### Examples
```bash
$ python script_name.py visualize
Please enter the type of visualization ('train' or 'test'): train
Please enter the absolute path to the result directory: /home/user/results
```

## Error Handling
The tool includes comprehensive error handling for various scenarios:

1. **Invalid Visualization Type**
   - If you enter a type other than 'train' or 'test'
   - Error message: "Invalid type. Please use 'train' or 'test'."

2. **Invalid Path**
   - If the provided path is not absolute
   - Error message: "The path must be an absolute path."

3. **Non-existent Path**
   - If the specified directory doesn't exist
   - Error message: "The path {path} does not exist."

4. **Unexpected Errors**
   - All other unexpected errors are caught and displayed with appropriate messages

## Function Details

### `visualize()`
Main function that handles the visualization process.

**Operations:**
1. Prompts for visualization type
2. Prompts for result directory path
3. Validates inputs
4. Calls appropriate plotting function based on type:
   - `plot_npy_all_train()` for training data
   - `plot_npy_all()` for test data

## Notes
- The tool expects the presence of a custom `plotter` module with implemented plotting functions
- All paths must be absolute to ensure consistent behavior across different operating systems
- The tool provides immediate feedback for any errors encountered during execution