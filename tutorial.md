# Visualization Tool Documentation

## Overview
This tool provides functionality to visualize training and testing results by plotting data from `.npy` files. It features an interactive command-line interface with continuous visualization capabilities and control options.

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

### Interactive Workflow

1. **Initial Setup**
   - **Visualization Type Selection**
     - Enter the type of visualization (`train` or `test`)
   - **Result Directory Path**
     - Provide the absolute path to the directory containing your result files
     - Must be an absolute path (e.g., `/home/user/results` or `C:\Users\user\results`)

2. **Continuous Visualization Control**
   After each visualization, you'll be prompted to choose an action:
   - `continue`: Continue visualizing the current data
   - `reset`: Reset parameters (type and path)
   - `exit`: Exit the program

### Example Workflow
```bash
$ python script_name.py visualize
Please enter the type of visualization ('train' or 'test'): train
Please enter the absolute path to the result directory: /home/user/results
[Visualization is displayed]
Choose an action: continue
[Visualization is updated]
Choose an action: reset
[Return to type selection]
```

## Error Handling

### Input Validation
1. **Invalid Visualization Type**
   - Occurs when entering a type other than 'train' or 'test'
   - Error message: "Invalid type. Please use 'train' or 'test'."

2. **Invalid Path**
   - Occurs when the provided path is not absolute
   - Error message: "The path must be an absolute path."

3. **Non-existent Path**
   - Occurs when the specified directory doesn't exist
   - Error message: "The path {path} does not exist."

### Program Interruption
- Keyboard Interrupt (Ctrl+C) is handled gracefully
- Displays message: "Operation cancelled. Exiting."

### Other Errors
- Unexpected errors are caught and displayed with appropriate messages
- Program exits gracefully after error display

## Function Details

### `visualize_once(type: str, path: Path)`
Helper function that performs a single visualization.
- **Parameters:**
  - `type`: Visualization type ('train' or 'test')
  - `path`: Path object pointing to result directory
- **Behavior:**
  - Calls appropriate plotting function based on type
  - Returns to action prompt after completion

### `visualize()`
Main function that manages the visualization workflow.
- **Features:**
  - Interactive parameter input
  - Continuous visualization loop
  - Action control system
  - Comprehensive error handling

## Control Flow
1. Program starts → Type selection → Path input
2. Visualization loop:
   - Display visualization
   - Prompt for action
   - Based on action:
     - `continue`: Repeat visualization
     - `reset`: Return to type selection
     - `exit`: End program
3. Error handling at any step returns to appropriate point or exits

## Notes
- The tool requires a custom `plotter` module with implemented plotting functions
- All paths must be absolute to ensure consistent behavior
- The program can be interrupted at any time using Ctrl+C
- Invalid actions will cause the program to exit
