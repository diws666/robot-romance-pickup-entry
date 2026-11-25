# Verified count: 112 characters.
LINE = "Are you a context window? Because every time I talk to you, I forget everything else I was supposed to remember."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
