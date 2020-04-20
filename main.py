import PyPDF2 as pdf
import pathlib
import sys
import itertools
import functools
import io
import contextlib


OUTPUT_DIR = pathlib.Path('output')
INPUT_DIR = pathlib.Path('input')


def get_pdf_files(dir):
    return list(sorted(list(dir.iterdir())))

def to_pages(file):
    reader = pdf.PdfFileReader(file)
    pages = [reader.getPage(page) for page in range(reader.getNumPages())]
    return pages

def merge_pdf(pdf_files):
    pages = map(to_pages, pdf_files)
    pages = itertools.chain.from_iterable(pages)

    writer = pdf.PdfFileWriter()
    for p in pages:
        writer.addPage(p)

    return writer


def remove_if_already_exists(file):
    try:
        file.unlink()
    except:
        pass

def save(filename, writer):
    pdf_file = OUTPUT_DIR / filename

    try:
        pdf_file = io.FileIO(pdf_file, mode='w')
    except:
        pdf_file.unlink()
        pdf_file = io.FileIO(pdf_file, mode='w')


    writer.write(pdf_file)


def get_filename():
    try:
        filename = sys.argv[1]
    except:
        filename = 'untitled.pdf'

    return filename


def main():
    pdf_name = get_filename()

    pdf_files = get_pdf_files(INPUT_DIR)

    with contextlib.ExitStack() as stack:
        # open each file and put them into the stack.
        # the stack will close the files automatically 
        pdf_files = [path.open(mode='rb') for path in pdf_files]
        pdf_files = map(stack.enter_context, pdf_files)

        output_pdf = merge_pdf(pdf_files)
        save(pdf_name, output_pdf)

main()
