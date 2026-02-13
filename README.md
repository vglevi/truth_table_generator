# Truth table generator

A CLI tool for generating truth tables of propositional formulas

## Installation

1. Get a Python 3 version if you don't have one. I reccomend using Python 3.13, since the program was written in that version.
2. Clone this repo
3. cd in it
4. If you want to ensure to run the program in the recommended version, get the uv project/package manager
5. Run the program:
Run with uv:
```
uv run main.py "<formula>"
```
Or just simply:
```
python3 main.py "<formula>"
```

## Usage

The operators are:

- ```~```: not
- ```&```: and
- ```|```: or
- ```->```: if
- ```<->```: iff

The precedence of the operators follows the conventions, i.e. ```~``` has the highest and ```<->``` has the lowest precedence. The output will always indicate the order of operations by paranthesis.

You can owerwrite the order of operations by using ```( )```

You can use as many spaces as you want, they will be ignored. The output will have always the same format: 1 space around binary operators, otherwise 0.

The variables can be any number of characters long but they can't contain the operator symbols, parantheses and space
