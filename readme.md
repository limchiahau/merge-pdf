PDF Merger

This scripts requires users to create an output and an input directory in the same folder as the script.

This script will merge the pdf's in input and place the output file in output.

## Installation

cd into the directory containing this script. Than run the commands below:

> mkdir input output  
> pipenv install --ignore-pipfile

## Usage

> pipenv shell
> python main.py <filename>

replace <filename> with the name of the output pdf. If filename is not given
the output pdf is named 'untitled.pdf'.

## Notes

The pdf's in the input folder will be combined in sorted order.

For example if there are 2 pdf's in the input folder named 1.pdf and 2.pdf respectively;
1.pdf will be placed in front of 2.pdf.
