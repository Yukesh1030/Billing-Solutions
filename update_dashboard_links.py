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
        
    # We want to replace all href="#" or any href that isn't pointing to a dashboard page,
    # but the simplest way without breaking navigation is to just do it via simple string replacement
    # for the specific quick actions and mock data tables we just added.
    
    # Injected links like <a href="#" ...
    content = content.replace('href="#"', 'href="404.html"')
    content = content.replace("href='#'", 'href="404.html"')
    
    # We must RESTORE the Overview and Logout links if they were broken
    content = content.replace('href="404.html" class="active"><i class="fa-solid fa-gauge"></i> Overview</a>', 'href="AdminDashboard.html" class="active"><i class="fa-solid fa-gauge"></i> Overview</a>')
    
    # For ClientDashboard Home link
    content = content.replace('href="404.html" class="active"><i class="fa-solid fa-house"></i> Home</a>', 'href="ClientDashboard.html" class="active"><i class="fa-solid fa-house"></i> Home</a>')
    
    # The logout link should point to Login.html, wait, dashboard.js handles logout via click event,
    # but let's make sure its href is '#' so the event fires without navigating to 404, OR we just let it go to Login.html
    # In dashboard.js, logoutBtn intercepts click and goes to Login.html anyway, so href="404.html" is fine, but let's fix it just in case:
    content = content.replace('id="logoutBtn" href="404.html"', 'id="logoutBtn" href="#"')
    content = content.replace('href="404.html" id="logoutBtn"', 'href="#" id="logoutBtn"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated links in {filename}")

