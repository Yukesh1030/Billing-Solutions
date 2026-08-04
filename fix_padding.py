import os
import re

files_to_fix = [
    'index.html',
    'BillingSolutions.html',
    'Pricing.html',
    'Resources.html',
    'Contact.html',
    'Signup.html'
]

for file_name in files_to_fix:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(r'padding:\s*(\d+rem)\s+0;', r'padding: \1 2rem;', content)
    content = re.sub(r'padding:\s*(\d+rem)\s+0\s*}', r'padding: \1 2rem }', content)
    content = re.sub(r'padding:\s*(\d+rem)\s+0\s+(\d+rem);', r'padding: \1 2rem \2;', content)
    content = re.sub(r'padding:\s*(\d+px)\s+0\s+(\d+px);', r'padding: \1 2rem \2;', content)
    content = re.sub(r'padding:\s*(\d+px)\s+0;', r'padding: \1 2rem;', content)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)
print("Done")
