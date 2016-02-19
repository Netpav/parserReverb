import os
import sys

from src.ReverbParser import ReverbParser

# Get directory of the file.
current_dir = os.path.dirname(os.path.realpath(__file__))

# Set filepaths
reverb_filepath = os.path.abspath(current_dir+'/libs/reverb-latest.jar')
# output_dir = current_dir

# Create the main object.
reverb_parser = ReverbParser(reverb_filepath)

# # Select and parse input file
# input_filepath = os.path.abspath('reviews_10.txt')
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

    # Simple solution for all (even old) systems.
    in_file = sys.argv[1]
    out_dir = sys.argv[2]

    reverb_parser.process_file(in_file, out_dir)



