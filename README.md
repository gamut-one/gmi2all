Gemini 2 All
============

Gemini 2 All, or `gmi2all` is a simple tool to translate [Gemini](http://gemini.circumlunar.space) documents to a mix of other formats. 

Supported Formats
-----------------

* HTML
* Gophernicus-style Gophermaps
* Plaintext

Why
---

Creating multiple copies of the same site in different formats can be a pain to manage without some sort of framework to build them with. As tooling didn't exist for at least one combination we required, it was easier to work with Gemini as the source format and convert to other formats as needed.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gmi2all.

```bash
pip install gmi2all
```

## Usage

```
usage: gmi2all.py [-h] [--version] [-f FORMAT] [-o OUTPUT] [--stylesheet STYLESHEET] [--fixed-width-p] [--width WIDTH] file

positional arguments:
  file

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -f FORMAT, --format FORMAT
                        output format
  -o OUTPUT, --output OUTPUT
                        output filename
  --stylesheet STYLESHEET
                        Name of a stylesheet to link in the header of HTML documents
  --fixed-width-p       Limit the length of lines in a paragraph by the width value
  --width WIDTH         Column width to use for Gopher and Plain
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

