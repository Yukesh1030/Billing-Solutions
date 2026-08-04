import os
import re

files_to_fix = [
    'index.html',
    'BillingSolutions.html',
    'Pricing.html',
    'Resources.html',
    'Contact.html'
]

html_to_find = r'<h4>Quick Links</h4>\s*<ul class="footer-links">\s*<li><a href="index.html">Home</a></li>\s*<li><a href="BillingSolutions.html">Solutions</a></li>\s*<li><a href="Pricing.html">Pricing</a></li>\s*<li><a href="Resources.html">Resources</a></li>\s*</ul>'

html_to_replace = '''<h4>Quick Links</h4>
                    <ul class="footer-links">
                        <li><a href="index.html">Home</a></li>
                        <li><a href="BillingSolutions.html">Billing Solutions</a></li>
                        <li><a href="Pricing.html">Pricing</a></li>
                        <li><a href="Resources.html">Resources</a></li>
                        <li><a href="Contact.html">Contact</a></li>
                    </ul>'''

for file_name in files_to_fix:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = re.sub(html_to_find, html_to_replace, content)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footer Quick Links updated in all files.")
