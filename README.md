 # ![Image](https://github.com/codzlab/pdfoz/blob/main/ui/icon.png) pdfoz by Codzlab 

pdfoz is a Python-based application developed by Codzlab that provides functionality for working with PDF files. Whether you need to extract text, merge multiple PDFs, split a PDF into separate pages, or perform other PDF manipulation tasks, pdfoz is here to simplify your workflow.

## Features

- **Opening PDF :** Opens the PDF 
- **Less Memory :** It uses very less `RAM`

> ## Upcoming Features

- **PDF Text Extraction**: Extract text content from PDF files.
- **PDF Merging**: Merge multiple PDF files into a single document.
- **PDF Splitting**: Split a PDF into separate pages or ranges of pages.
- **PDF Conversion**: Convert PDF files to other formats, such as text or images.
- **PDF Encryption**: Protect your PDF files by adding encryption and password protection.

## Installation

To install pdfoz, simply clone this repository:
```
git clone https://github.com/codzlab/pdfoz.git
```

Then, navigate to the pdfoz directory and install the dependencies using pip:

```
cd pdfoz
```
```
pip install -r requirements.txt
```


## Usage

pdfoz can be used both as a command-line tool and as a Python library.

>### Command-Line Usage (Currently Not Build)

To use pdfoz from the command line, run the `pdfoz.py` script followed by the desired command and any additional options:
```
python main.py <command> [options]
```

For example, to extract text from a PDF file:
```
python main.py extract --input file.pdf --output extracted_text.txt
```

For a list of available commands and options, use the `--help` flag:
```
python main.py --help
```

> ### Python Library Usage (Testing Phase)

You can also use pdfoz as a Python library by importing the relevant modules:

```python
from pdfoz import extractor

# Extract text from a PDF file
text = extractor.extract_text('file.pdf')

print(text)
```


## Contributing
Contributions to pdfoz are welcome! If you have ideas for new features, improvements, or bug fixes, please open an issue or submit a pull request on GitHub.

## License
pdfoz is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions, suggestions, or feedback, feel free to contact the developers at `codzlabsio+github@gmail.com`


Feel free to customize this template according to the specific details and features of your pdfoz application.


