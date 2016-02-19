import subprocess
from nltk.tokenize import sent_tokenize

## FUNCTIONS DEFINITON

# Function for running commands
def run_command(command, in_string):
    # Open process
    p = subprocess.Popen(command,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    # Write to process stdin and get its stdout.
    return p.communicate(input=in_string)[0].strip()

# Process one document
def process_document(doc_text):
    # Split document to sentences.
    sentences = sent_tokenize(doc_text)
    # Run every sentence through Reverb.
    sent_data = []
    for sentence in sentences:
        r_output = run_command('java -jar libs/reverb-latest.jar -q', sentence)
        if not r_output:
            continue
        r_items = r_output.split('\t')
        original_sentence = r_items[12].strip()
        triple = ' '.join(r_items[2:5]).strip()
        triple_normalized = ' '.join(r_items[15:18]).strip()
        sent_data.append([original_sentence, triple, triple_normalized])
    # Result
    return sent_data

## PERFORMANCE PART

# Read reviews file line by line.
input_file = open('reviews_10.txt')
output_file = open('output.txt', 'w')

for input_line in input_file:
    # Read a document
    items = input_line.split('\t')
    doc_class = items[0].strip()
    doc_text = items[1].strip()
    # Get document features
    doc_data = process_document(doc_text)
    if not doc_data:
        continue    # skip empty lists
    data_line = []
    # Join features to one line
    for (orig, triple_std, triple_norm) in doc_data:
        data_line.extend([orig, triple_std])
    # Create string from features
    str_line = ' | '.join(data_line)
    # Add class
    str_line = doc_class + '\t' + str_line
    print str_line
    # Write to file
    output_file.write(str_line + '\n')
