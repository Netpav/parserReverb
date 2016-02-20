import os
import sys

# Import classes
try:
    from src.ReverbParser import ReverbParser
    is_nltk = True
except ImportError, e:
    is_nltk = False

from src.ReverbBulkParser import ReverbBulkParser

# Get directory of the file.
current_dir = os.path.dirname(os.path.realpath(__file__))

# Set filepaths
reverb_filepath = os.path.abspath(current_dir+'/libs/reverb-latest.jar')
output_dir = current_dir + '/output'

## TESTING
#  Create the main object.
#reverb_parser = ReverbParser(reverb_filepath)
#reverb_parser = ReverbBulkParser()

# Select and parse input file
# input_filepath = os.path.abspath('input/r_input_10.txt')
# reverb_parser.process_file(input_filepath, output_dir)
# exit()

# If the file was run directly (as script).
if __name__ == '__main__':
    # # Module required for command line parsing.
    # import argparse
    #
    # # Parse the incoming arguments: ./run_reverb.py <input filepath> <output directory>
    # args_parser = argparse.ArgumentParser(description='Reverb caller and parser in Python')
    # args_parser.add_argument('infile', action='store', help='Path to the input file.',
    #                     metavar='<string>', nargs=1)
    # args_parser.add_argument('outdir', action='store', help='Path to the output directory.',
    #                     metavar='<string>', nargs=1)
    # args = args_parser.parse_args()
    # reverb_parser.process_file(args.infile[0], args.outdir[0])

    # Simple solution for all (even old) systems, but it doesn't check anything.

    # Get values
    op_mode = int(sys.argv[1])
    in_file = sys.argv[2]
    out_dir = sys.argv[3]

    # Create the correct object
    if op_mode == 1:
        if not is_nltk:
            exit('Module nltk is not installed, you cannot use mode 1.')
        reverb_parser = ReverbParser(reverb_filepath)
    elif op_mode == 2:
        reverb_parser = ReverbBulkParser(True)
    elif op_mode == 3:
        reverb_parser = ReverbBulkParser(False)
    else:
        exit('Unknown mode entered.')

    # Process file
    reverb_parser.process_file(in_file, out_dir)
