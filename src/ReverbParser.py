import subprocess
import os
import time

from nltk.tokenize import sent_tokenize


class ReverbParser(object):

    def __init__(self, reverb_filepath):
        """
        Constructor.
        :param reverb_filepath: Absolute path to Reverb JAR file.
        """
        # Define reverb command
        self.reverb_command = 'java -Xmx512m -jar ' + reverb_filepath + ' -q'

    def process_document(self, doc_text):
        """
        Process input document and return list of document features.
        :param doc_text: input text (may contain multiple sentences).
        :return: list of documents features.
        """
        # Split document to sentences.
        sentences = sent_tokenize(doc_text)
        # Run every sentence through Reverb.
        sent_data = []
        for sentence in sentences:
            r_output = self.run_command(self.reverb_command, sentence)
            if not r_output:
                continue
            r_items = r_output.split('\t')
            original_sentence = r_items[12].strip()
            triple = ' '.join(r_items[2:5]).strip()
            triple_normalized = ' '.join(r_items[15:18]).strip()
            sent_data.append([original_sentence, triple, triple_normalized])
        # Result
        return sent_data

    def process_file(self, input_filepath, output_dir):
        """
        Read input file, process every line in Reverb and write result to output file.
        :param input_filepath: Path to the input file.
        :param output_dir: Path to the output directory.
        :return: nothing
        """
        # Prepare files
        input_file = open(input_filepath)
        input_filename = os.path.basename(input_filepath).split('.')[0]
        output_filename = input_filename + '_reverb.txt'
        output_filepath = os.path.abspath(output_dir + '/' + output_filename)
        output_file = open(output_filepath, 'w')
        # Print information
        print('>>>>NEW FILE')
        print('- Reading from file: %s') % input_filepath
        print('- Writing to file: %s') % output_filepath
        start_time = time.time()
        # Read input file line by line.
        for input_line in input_file:
            # Read a document.
            items = input_line.split('\t')
            doc_class = items[0].strip()
            doc_text = items[1].strip()
            # Get document features.
            doc_data = self.process_document(doc_text)
            if not doc_data:
                continue    # skip empty lists
            data_line = []
            # Join features to one line.
            for (orig, triple_std, triple_norm) in doc_data:
                data_line.extend([orig, triple_std])
            # Create string from features.
            str_line = ' | '.join(data_line)
            # Add document class.
            str_line = doc_class + '\t' + str_line
            print str_line
            # Write to output file.
            output_file.write(str_line + '\n')
        # Show success
        print('>>ALL SAVED')
        run_time = time.time() - start_time
        print('>>Script run time for the file: %d seconds') % run_time

    @staticmethod
    def run_command(command, in_string):
        """
        Function for running commands in command line.
        :param command:
        :param in_string: input
        :return: output
        """
        # Open process
        p = subprocess.Popen(command,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        # Write to process stdin and get its stdout.
        return p.communicate(input=in_string)[0].strip()
