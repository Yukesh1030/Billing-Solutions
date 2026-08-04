import os

dashboard_files = [
    'AdminDashboard.html',
    'ClientDashboard.html',
    'Customers.html',
    'Invoices.html',
    'Reports.html',
    'Settings.html'
]

for filename in dashboard_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find and replace <span>STACKLY</span> inside the sidebar header
    # It looks like:
    # <div class="sidebar-header">
    #     <img src="assets/Brand-logo.webp" alt="Logo">
    #     <span>STACKLY</span>
    # </div>
    
    # We can just replace the exact span string
    content = content.replace('<span>STACKLY</span>', '')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Removed STACKLY span from {filename}")

