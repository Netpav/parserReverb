# Reverb parser
Script for parsing reverb output into correct documents list.

## Usage
`python run_reverb.py <mode> <input file> <output dir>`

Dependencies: For mode 1 is [nltk](https://pypi.python.org/pypi/nltk) module needed.

### Modes
* `1` ... Reverb processes individual sentences of the document. Input file is text file with documents (format: `<class>\t<text>`)
* `2` ... Reverb processes the whole text file with documents. Input file is pre-generated output from Reverb. This mode is much faster than mode 1.
* `3` ... Same as 2, but does not remove duplicates.

### Examples
`python run_reverb.py 1 input/reviews_10.txt output` ... Process individual sentences from file "input/reviews_10.txt" and save result to subdirectory "output".

`python run_reverb.py 2 r_input_10.txt .` ... Process whole documents from Reverb file and save result to current directory "."

### Problem of mode 1
Processing 10 documents takes about 90 seconds, that means 90/10 = 9 seconds per document.

Processing 50 000 documents would take 50 000 * 9 = 450 000 seconds = 125 hours = 5.2 days

Well, that's quite impractical.

### Problem of mode 2
God knows if it works properly, but it seems so :). I have no moral to write tests for this stuff.
