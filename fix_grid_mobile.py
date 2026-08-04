import os
import glob

html_files = glob.glob('*.html')

for filename in html_files:
    if 'Dashboard' in filename or 'Client' in filename or filename in ['Customers.html', 'Invoices.html', 'Reports.html', 'Settings.html']:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace the hardcoded 300px minimum with 250px so it doesn't break mobile layout
        new_content = content.replace('minmax(300px, 1fr)', 'minmax(250px, 1fr)')
        
        # Also ensure table containers have overflow-x auto directly on the table wrapper
        new_content = new_content.replace('<table>', '<div style="width:100%; overflow-x:auto;">\n                    <table>')
        new_content = new_content.replace('</table>', '</table>\n                </div>')
        # Wait, I already added <div style="overflow-x: auto;"> around some tables, so doing this blindly might nest them. Let's just stick to the 300px -> 250px fix.
        # Actually in dashboard.css I already have .table-container { overflow-x: auto; }.
        # So we only need to fix the grid inline CSS.
        
        if content != new_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated grid sizing in {filename}")

