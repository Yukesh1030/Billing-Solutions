import os
import re

files_to_update = [
    'BillingSolutions.html',
    'Pricing.html',
    'Resources.html',
    'Contact.html'
]

for file_name in files_to_update:
    with open(file_name, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change text-align: center to text-align: left in .page-hero
    content = re.sub(r'(\.page-hero\s*\{[^}]*)text-align:\s*center;', r'\1text-align: left;', content)
    
    # Append the media query right before </style>
    if '.page-hero { text-align: center; }' not in content:
        media_query = "\n        @media (max-width: 768px) {\n            .page-hero { text-align: center; }\n        }\n    </style>"
        content = content.replace('    </style>', media_query)
    
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated subpages for mobile-only hero centering.")
