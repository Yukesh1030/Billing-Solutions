import os

def create_client_page(filename, title, content_html, active_sidebar_link):
    # Read ClientDashboard.html
    with open('ClientDashboard.html', 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Inject AOS CSS if not present
    if 'aos.css' not in html:
        html = html.replace('</head>', '    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n</head>')
        
    # Inject AOS JS if not present
    if 'aos.js' not in html:
        html = html.replace('</body>', '    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script>AOS.init({ duration: 800, once: true });</script>\n</body>')
        
    # Replace Title
    html = html.replace('<title>Client Dashboard - STACKLY</title>', f'<title>{title} - STACKLY</title>')
    
    # We must reset active classes
    html = html.replace('class="active"><i class="fa-solid fa-house"></i> Home</a>', '><i class="fa-solid fa-house"></i> Home</a>')
    
    # Update sidebar active state and ensure correct links
    # Convert standard 404 links to the actual pages for the sidebar
    html = html.replace('href="404.html"><i class="fa-solid fa-file-invoice"></i> My Invoices</a>', 'href="ClientInvoices.html"><i class="fa-solid fa-file-invoice"></i> My Invoices</a>')
    html = html.replace('href="404.html"><i class="fa-solid fa-credit-card"></i> Payment Methods</a>', 'href="ClientPaymentMethods.html"><i class="fa-solid fa-credit-card"></i> Payment Methods</a>')
    html = html.replace('href="404.html"><i class="fa-solid fa-rotate"></i> Subscriptions</a>', 'href="ClientSubscriptions.html"><i class="fa-solid fa-rotate"></i> Subscriptions</a>')
    html = html.replace('href="404.html"><i class="fa-solid fa-user"></i> Profile</a>', 'href="ClientProfile.html"><i class="fa-solid fa-user"></i> Profile</a>')

    if active_sidebar_link == 'Home':
        html = html.replace('><i class="fa-solid fa-house"></i> Home</a>', 'class="active"><i class="fa-solid fa-house"></i> Home</a>')
    elif active_sidebar_link == 'My Invoices':
        html = html.replace('href="ClientInvoices.html"><i class="fa-solid fa-file-invoice"></i> My Invoices</a>', 'href="ClientInvoices.html" class="active"><i class="fa-solid fa-file-invoice"></i> My Invoices</a>')
    elif active_sidebar_link == 'Payment Methods':
        html = html.replace('href="ClientPaymentMethods.html"><i class="fa-solid fa-credit-card"></i> Payment Methods</a>', 'href="ClientPaymentMethods.html" class="active"><i class="fa-solid fa-credit-card"></i> Payment Methods</a>')
    elif active_sidebar_link == 'Subscriptions':
        html = html.replace('href="ClientSubscriptions.html"><i class="fa-solid fa-rotate"></i> Subscriptions</a>', 'href="ClientSubscriptions.html" class="active"><i class="fa-solid fa-rotate"></i> Subscriptions</a>')
    elif active_sidebar_link == 'Profile':
        html = html.replace('href="ClientProfile.html"><i class="fa-solid fa-user"></i> Profile</a>', 'href="ClientProfile.html" class="active"><i class="fa-solid fa-user"></i> Profile</a>')

    # Replace main content
    start_main = html.find('<main class="main-content">') + len('<main class="main-content">')
    end_main = html.find('</main>')
    
    final_html = html[:start_main] + '\n' + content_html + '\n        ' + html[end_main:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Created {filename}")

home_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">Welcome back!</h2>

            <!-- Original Stats (Updated with AOS) -->
            <div class="stat-grid">
                <div class="stat-card" data-aos="fade-up" data-aos-delay="100">
                    <div class="stat-icon"><i class="fa-solid fa-file-invoice-dollar"></i></div>
                    <div class="stat-details">
                        <p>Amount Due</p>
                        <h3 style="color: #f1c40f;">$450.00</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-up" data-aos-delay="200">
                    <div class="stat-icon"><i class="fa-solid fa-check-double"></i></div>
                    <div class="stat-details">
                        <p>Total Paid</p>
                        <h3>$12,400.00</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-up" data-aos-delay="300">
                    <div class="stat-icon"><i class="fa-solid fa-rotate"></i></div>
                    <div class="stat-details">
                        <p>Active Subscription</p>
                        <h3>Pro Plan</h3>
                    </div>
                </div>
            </div>

            <!-- Original Invoices Table (Updated with AOS) -->
            <div class="table-container" data-aos="fade-up" data-aos-delay="400">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0;">My Invoices</h3>
                    <a href="404.html" class="btn btn-outline" style="padding: 0.4rem 1rem; font-size: 0.85rem;">View All</a>
                </div>
                <div style="overflow-x: auto;">
                    <table>
                        <thead>
                            <tr>
                                <th>Invoice ID</th>
                                <th>Description</th>
                                <th>Amount</th>
                                <th>Date</th>
                                <th>Status</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#INV-00125</td>
                                <td>Monthly Pro Subscription</td>
                                <td>$450.00</td>
                                <td>Aug 01, 2026</td>
                                <td><span class="status pending">Pending</span></td>
                                <td><a href="404.html" style="color:var(--primary-color); text-decoration:none;"><i class="fa-solid fa-credit-card"></i> Pay Now</a></td>
                            </tr>
                            <tr>
                                <td>#INV-00110</td>
                                <td>Monthly Pro Subscription</td>
                                <td>$450.00</td>
                                <td>Jul 01, 2026</td>
                                <td><span class="status paid">Paid</span></td>
                                <td><a href="404.html" style="color:var(--text-muted);"><i class="fa-solid fa-download"></i> PDF</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- 1. Quick Links Panel -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3>Quick Actions</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
                    <a href="404.html" class="btn btn-primary"><i class="fa-solid fa-credit-card"></i> Pay Balance</a>
                    <a href="404.html" class="btn btn-outline"><i class="fa-solid fa-pen"></i> Update Payment Method</a>
                    <a href="404.html" class="btn btn-outline"><i class="fa-solid fa-arrow-up"></i> Upgrade Plan</a>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 2. Recent Account Activity -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Recent Activity</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="margin-bottom: 1rem; border-left: 2px solid var(--primary-color); padding-left: 10px;">
                            <p style="margin: 0; font-size: 0.9rem;">Invoice #INV-00110 Paid</p>
                            <small style="color: var(--text-muted);">Jul 02, 2026</small>
                        </li>
                        <li style="border-left: 2px solid var(--primary-color); padding-left: 10px;">
                            <p style="margin: 0; font-size: 0.9rem;">Profile Updated</p>
                            <small style="color: var(--text-muted);">Jun 28, 2026</small>
                        </li>
                    </ul>
                </div>

                <!-- 3. Usage Metrics -->
                <div class="table-container" data-aos="fade-up">
                    <h3>API Usage</h3>
                    <div style="margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span>Requests</span><span>85,000 / 100k</span>
                        </div>
                        <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; margin-bottom: 1rem;">
                            <div style="width: 85%; height: 100%; background: var(--primary-color); border-radius: 4px;"></div>
                        </div>
                    </div>
                </div>

                <!-- 4. Current Plan Summary -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Your Plan</h3>
                    <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; margin-top: 1rem; border: 1px solid var(--primary-color);">
                        <h2 style="color: var(--primary-color); margin: 0 0 0.5rem 0;">Pro Tier</h2>
                        <p style="color: var(--text-muted); margin-bottom: 1rem;">Next billing date: <strong>Sep 01, 2026</strong></p>
                        <a href="404.html" style="color: var(--text-main); font-weight: bold;"><i class="fa-solid fa-arrow-right"></i> Manage Subscription</a>
                    </div>
                </div>
            </div>
"""

invoices_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">My Invoices</h2>

            <!-- 1. Year-to-Date Spending -->
            <div class="stat-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin-bottom: 2rem;">
                <div class="stat-card" data-aos="fade-left" data-aos-delay="100">
                    <div class="stat-details">
                        <p>Total Spent (YTD)</p>
                        <h3>$6,750</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-left" data-aos-delay="200">
                    <div class="stat-details">
                        <p>Next Estimated Bill</p>
                        <h3 style="color: var(--primary-color);">$450</h3>
                    </div>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                
                <!-- 2. Upcoming Invoice Preview -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Next Invoice Preview</h3>
                    <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed var(--glass-border); padding-bottom: 0.5rem; margin-bottom: 0.5rem;">
                            <span>Pro Plan Base</span><span>$450.00</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px dashed var(--glass-border); padding-bottom: 0.5rem; margin-bottom: 1rem;">
                            <span>API Overage</span><span>$0.00</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; font-weight: bold; font-size: 1.2rem;">
                            <span>Estimated Total</span><span style="color: var(--primary-color);">$450.00</span>
                        </div>
                    </div>
                </div>

                <!-- 3. Dispute / Support Box -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Need Help?</h3>
                    <div style="margin-top: 1rem;">
                        <p style="color: var(--text-muted); margin-bottom: 1rem;">Notice an issue with your billing statement? Our support team is here to help.</p>
                        <a href="404.html" class="btn btn-outline" style="width: 100%;"><i class="fa-solid fa-headset"></i> Contact Billing Support</a>
                    </div>
                </div>

            </div>

            <!-- 4. Download History Table -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
                    <h3 style="margin: 0;">Full Invoice History</h3>
                    <a href="404.html" class="btn btn-primary" style="padding: 0.4rem 1rem; font-size: 0.85rem;"><i class="fa-solid fa-download"></i> Export All (CSV)</a>
                </div>
                <div style="overflow-x: auto;">
                    <table>
                        <thead>
                            <tr>
                                <th>Invoice ID</th>
                                <th>Date Issued</th>
                                <th>Amount</th>
                                <th>Status</th>
                                <th>Document</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#INV-00125</td>
                                <td>Aug 01, 2026</td>
                                <td>$450.00</td>
                                <td><span class="status pending">Pending</span></td>
                                <td><a href="404.html" style="color:var(--text-muted);"><i class="fa-solid fa-file-pdf"></i> Download</a></td>
                            </tr>
                            <tr>
                                <td>#INV-00110</td>
                                <td>Jul 01, 2026</td>
                                <td>$450.00</td>
                                <td><span class="status paid">Paid</span></td>
                                <td><a href="404.html" style="color:var(--text-muted);"><i class="fa-solid fa-file-pdf"></i> Download</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

payment_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">Payment Methods</h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                
                <!-- 1. Default Payment Method Mockup -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Default Payment Method</h3>
                    <div style="width: 100%; height: 180px; background: linear-gradient(135deg, #2c3e50, #3498db); border-radius: 12px; padding: 1.5rem; position: relative; color: white; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
                        <i class="fa-brands fa-cc-visa" style="font-size: 2.5rem; position: absolute; top: 1.5rem; right: 1.5rem;"></i>
                        <div style="position: absolute; bottom: 1.5rem; left: 1.5rem;">
                            <p style="margin: 0; font-family: monospace; font-size: 1.2rem; letter-spacing: 2px;">**** **** **** 4242</p>
                            <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem; opacity: 0.8;">Expires 12/28</p>
                        </div>
                    </div>
                </div>

                <!-- 2. Billing Address -->
                <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Billing Address</h3>
                    <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; margin-top: 1rem; border: 1px solid var(--glass-border);">
                        <p style="margin: 0 0 0.5rem 0; color: var(--text-main);"><strong>Acme Corp HQ</strong></p>
                        <p style="margin: 0 0 0.5rem 0; color: var(--text-muted);">123 Innovation Drive</p>
                        <p style="margin: 0 0 0.5rem 0; color: var(--text-muted);">Suite 400</p>
                        <p style="margin: 0; color: var(--text-muted);">San Francisco, CA 94103</p>
                        <a href="404.html" class="btn btn-outline" style="margin-top: 1rem; width: 100%;">Edit Address</a>
                    </div>
                </div>

            </div>

            <!-- 3. Add New Method Form -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3 style="margin-bottom: 1rem;">Add New Card</h3>
                <form class="redirect-404 dashboard-form" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                    <div style="grid-column: 1 / -1;">
                        <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Name on Card</label>
                        <input type="text" required placeholder="John Doe" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                    </div>
                    <div style="grid-column: 1 / -1;">
                        <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Card Number</label>
                        <input type="text" required placeholder="0000 0000 0000 0000" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                    </div>
                    <div>
                        <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Expiry Date</label>
                        <input type="text" required placeholder="MM/YY" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                    </div>
                    <div>
                        <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">CVC</label>
                        <input type="text" required placeholder="123" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                    </div>
                    <div style="grid-column: 1 / -1; margin-top: 1rem;">
                        <button type="submit" class="btn btn-primary" style="padding: 0.75rem 2rem;">Save Card</button>
                    </div>
                </form>
            </div>

            <!-- 4. Backup Payment Methods Table -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3>Saved Payment Methods</h3>
                <div style="overflow-x: auto; margin-top: 1rem;">
                    <table>
                        <thead>
                            <tr>
                                <th>Method</th>
                                <th>Expires</th>
                                <th>Status</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><i class="fa-brands fa-cc-visa" style="margin-right:10px;"></i> Visa ending in 4242</td>
                                <td>12/2028</td>
                                <td><span class="status paid">Default</span></td>
                                <td><span style="color: var(--text-muted);">None</span></td>
                            </tr>
                            <tr>
                                <td><i class="fa-brands fa-cc-mastercard" style="margin-right:10px;"></i> Mastercard ending in 5555</td>
                                <td>08/2025</td>
                                <td><span class="status pending">Backup</span></td>
                                <td><a href="404.html" style="color: #ef4444;">Remove</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

subscriptions_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">Subscriptions</h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                
                <!-- 1. Plan Comparison -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Your Plan: Pro</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>Monthly Price</span><span>$450.00</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>Included Seats</span><span>10</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>API Requests</span><span>100k / month</span>
                        </div>
                        <a href="404.html" class="btn btn-primary" style="margin-top: 1rem; width: 100%; text-align: center;">Upgrade to Enterprise</a>
                    </div>
                </div>

                <!-- 2. Add-Ons & Modules -->
                <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Active Add-Ons</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
                            <span><i class="fa-solid fa-server" style="margin-right: 10px; color: var(--primary-color);"></i> Extra 50GB Storage</span>
                            <span style="font-weight: bold;">$50/mo</span>
                        </li>
                        <li style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
                            <span><i class="fa-solid fa-headset" style="margin-right: 10px; color: var(--text-muted);"></i> Priority 24/7 Support</span>
                            <a href="404.html" class="btn btn-outline" style="padding: 0.3rem 0.8rem; font-size: 0.8rem;">Add for $100</a>
                        </li>
                    </ul>
                </div>

            </div>

            <!-- 3. Cancellation Options -->
            <div class="table-container" style="margin-top: 2rem; border-left: 4px solid #f59e0b;" data-aos="fade-up">
                <h3 style="color: #f59e0b;">Manage Subscription</h3>
                <p style="color: var(--text-muted); margin-top: 1rem;">You can pause your subscription for up to 3 months without losing your data, or cancel completely.</p>
                <div style="display: flex; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap;">
                    <a href="404.html" class="btn btn-outline">Pause Subscription</a>
                    <a href="404.html" class="btn" style="background: transparent; border: 1px solid #ef4444; color: #ef4444;">Cancel Plan</a>
                </div>
            </div>

            <!-- 4. Renewal History -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3>Subscription History</h3>
                <div style="overflow-x: auto; margin-top: 1rem;">
                    <table>
                        <thead>
                            <tr>
                                <th>Date</th>
                                <th>Event</th>
                                <th>Details</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Jan 01, 2026</td>
                                <td><span class="status paid">Plan Upgrade</span></td>
                                <td>Basic -> Pro ($450/mo)</td>
                            </tr>
                            <tr>
                                <td>Feb 15, 2025</td>
                                <td><span class="status pending">Add-on Added</span></td>
                                <td>Extra Storage ($50/mo)</td>
                            </tr>
                            <tr>
                                <td>Aug 01, 2024</td>
                                <td><span class="status paid">Account Created</span></td>
                                <td>Basic Plan ($150/mo)</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

profile_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">My Profile</h2>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">
                
                <!-- 1. Personal Information Form -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Personal Information</h3>
                    <form class="redirect-404 dashboard-form" style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Full Name</label>
                            <input type="text" required value="John Doe" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Job Title</label>
                            <input type="text" required value="VP of Finance" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Phone Number</label>
                            <input type="text" value="+1 (555) 123-4567" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <button type="submit" class="btn btn-primary" style="align-self: flex-start; margin-top: 1rem;">Update Profile</button>
                    </form>
                </div>

                <!-- 2. Password & Security -->
                <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Security</h3>
                    <form class="redirect-404 dashboard-form" style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Current Password</label>
                            <input type="password" required placeholder="••••••••" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">New Password</label>
                            <input type="password" required placeholder="••••••••" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <button type="submit" class="btn btn-outline" style="align-self: flex-start; margin-top: 1rem;">Change Password</button>
                    </form>
                </div>

            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                
                <!-- 3. Email Preferences -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Email Preferences</h3>
                    <div style="display: flex; flex-direction: column; gap: 1.5rem; margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h4>Billing Receipts</h4>
                                <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">Receive a PDF receipt after every payment.</p>
                            </div>
                            <div style="width: 50px; height: 26px; background: var(--primary-color); border-radius: 13px; position: relative; cursor: pointer;">
                                <div style="width: 22px; height: 22px; background: white; border-radius: 50%; position: absolute; top: 2px; right: 2px;"></div>
                            </div>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <h4>Product Updates</h4>
                                <p style="color: var(--text-muted); font-size: 0.9rem; margin: 0;">Get notified about new features.</p>
                            </div>
                            <div style="width: 50px; height: 26px; background: rgba(255,255,255,0.1); border-radius: 13px; position: relative; cursor: pointer; border: 1px solid var(--glass-border);">
                                <div style="width: 22px; height: 22px; background: var(--text-muted); border-radius: 50%; position: absolute; top: 1px; left: 2px;"></div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 4. Data Export -->
                <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Data & Privacy</h3>
                    <p style="color: var(--text-muted); margin-bottom: 1.5rem;">You have the right to request a copy of all your personal data stored on our servers, or request complete deletion.</p>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="404.html" class="btn btn-primary"><i class="fa-solid fa-download"></i> Request Data Export</a>
                        <a href="404.html" class="btn" style="background: transparent; border: 1px solid #ef4444; color: #ef4444;">Delete Account</a>
                    </div>
                </div>

            </div>
"""

create_client_page('ClientDashboard.html', 'Client Dashboard', home_content, 'Home')
create_client_page('ClientInvoices.html', 'My Invoices', invoices_content, 'My Invoices')
create_client_page('ClientPaymentMethods.html', 'Payment Methods', payment_content, 'Payment Methods')
create_client_page('ClientSubscriptions.html', 'Subscriptions', subscriptions_content, 'Subscriptions')
create_client_page('ClientProfile.html', 'Profile', profile_content, 'Profile')
