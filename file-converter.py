import markdown
import os
import sys


def execute_function(args):
    if args[1] == 'markdown':
        convert_markdwon_into_html(args[2], args[3])


def validator(args):
    # confirm the number of args
    if len(args) != 4:
        raise IndexError('You must specify three arguments')
    
    if args[2].isdigit():
        raise TypeError('Argument for input file is not string')
    
    if args[3].isdigit():
        raise TypeError('Argument for output file is not string')
    
    if not os.path.exists(args[2]):
        raise FileNotFoundError('Input file not found')


def convert_markdwon_into_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    html = markdown.markdown(content)

    with open(output_file, 'w', encoding='utf-8', errors='xmlcharrefreplace') as f:
        f.write(html)


if __name__ == '__main__':
    args = sys.argv
    validator(args)
    execute_function(args)
