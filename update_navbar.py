import os
import re

files_to_fix = [
    'index.html',
    'BillingSolutions.html',
    'Pricing.html',
    'Resources.html',
    'Contact.html'
]

html_to_find = r'<li><a href="Login.html" class="btn btn-primary" style="padding: 0.5rem 1rem; color: #0f172a;">Login</a></li>\s*</ul>\s*<button class="hamburger">&#9776;</button>'

html_to_replace = '''<li class="mobile-only"><a href="Login.html" class="btn btn-primary" style="padding: 0.5rem 1rem; color: #0f172a;">Login</a></li>
            </ul>

            <div class="nav-actions">
                <a href="Login.html" class="btn btn-primary desktop-only" style="padding: 0.5rem 1.5rem; color: #0f172a; border-radius: 20px;">Login</a>
                <button class="hamburger">&#9776;</button>
            </div>'''

for file_name in files_to_fix:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We use regex substitution
    content = re.sub(html_to_find, html_to_replace, content)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navbar updated in HTML files")
