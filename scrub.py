"""
Simple script to remove hard wraps, leading whitespace and
"""

from __future__ import print_function
import sys
import re
import os

inpath = sys.argv[1]
outpath = os.path.join(os.path.dirname(inpath), 'scrubbed.txt')
print('Input:', inpath)
print('Output:', outpath)

with open(inpath, 'r') as in, open(outpath, 'w') as b:
    for line in infile:
        outfile.write(line)

# # Remove line wraps
# full_text = re.sub(r'(\S)\n(\S)', r'\1 \2', full_text)
# # Remove extra spacing
# full_text = re.sub(r'\n\s*\n', '\n\n', full_text)
# # Remove leading whitespace
# full_text = '\n'.join(map(lambda line: line.strip(), full_text.splitlines()))