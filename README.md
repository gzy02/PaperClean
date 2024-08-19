
# PaperClean

**PaperClean** is a tool designed to clean and organize LaTeX files for academic papers. It simplifies the management of multiple `.tex` files by merging them into a single file, removing comments, and copying necessary dependent files to a specified output directory. This is especially useful when preparing a clean version of your paper for submission.

## Features

- **Merge `.tex` Files**: Automatically merges multiple LaTeX files into a single file.
- **Remove Comments**: Option to remove all comments from the LaTeX files.
- **Copy Dependencies**: Copies all dependent files (e.g., `.bib`, `.sty`, `.bst`) to the output directory.
- **Customizable Configuration**: Easily configure file paths and processing options.

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/gzy02/PaperClean.git
cd PaperClean
```

## Usage

1. Update the `config.py` file with your specific paths and preferences.

    ```python
    # Configuration file for the PaperClean script
    
    retain_file_extensions_list = [".bbl", ".tex", ".bst", ".sty", ".bib"]
    tex_dir = r"your tex directory"
    main_tex_name = "main.tex"
    output_dir = r"your output directory"
    remove_comments = True
    merge_tex = True    
    ```

2. Run the script:

    ```bash
    python PaperClean.py
    ```

   This will parse the main `.tex` file specified in `config.py`, remove comments (if enabled), merge `.tex` files (if enabled), and copy all dependent files to the output directory.

## Example

Suppose you have the following LaTeX project structure:

```
project_folder/
│
├── main.tex
├── chapter1.tex
├── chapter2.tex
├── references.bib
└── figures/
    ├── fig1.png
    └── fig2.png
```

After running `PaperClean.py`, the output directory will contain a cleaned and merged version of `main.tex`, along with all required files such as `references.bib` and the figures.

## Configuration Options

- **retain_file_extensions_list**: List of file extensions to retain in the output directory (e.g., `.bib`, `.sty`).
- **tex_dir**: Directory containing the LaTeX files.
- **main_tex_name**: Name of the main LaTeX file to be processed.
- **output_dir**: Directory where the cleaned files will be saved.
- **remove_comments**: Boolean option to remove comments from the LaTeX files.
- **merge_tex**: Boolean option to merge all `.tex` files into a single file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests with any improvements or suggestions.
