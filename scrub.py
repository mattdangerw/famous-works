import sys
import re
import textwrap

print(sys.argv[1])

with open(sys.argv[1], 'r') as textfile:
    full_text = textfile.read()

# Remove line wraps
full_text = re.sub(r'(\S)\n(\S)', r'\1 \2', full_text)
# Remove extra spacing
full_text = re.sub(r'\n\s*\n', '\n\n', full_text)
# Remove leading whitespace
full_text = '\n'.join(map(lambda line: line.strip(), full_text.splitlines()))

with open(sys.argv[1], 'w') as textfile:
    textfile.write(full_text)

sys.exit(0)
