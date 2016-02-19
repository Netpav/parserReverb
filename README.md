# Reverb parser
Script for parsing reverb output into correct document list.

## Usage
`python run_reverb.py <input file> <output dir>`

### Example
`python run_reverb.py reviews_10.txt output` ... subdirectory "output"

`python run_reverb.py reviews_10.txt .` ... current directory "."

### Problem
Processing 10 documents takes about 90 seconds, that means 90/10 = 9 seconds per document.

Processing 50,000 documents would take 50000 * 9 = 450 000 seconds = 125 hours = 5.2 days

Well, that's quite impractical.
