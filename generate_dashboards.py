import os

def create_page(filename, title, content_html, active_sidebar_link):
    # Read AdminDashboard.html
    with open('AdminDashboard.html', 'r', encoding='utf-8') as f:
        admin_html = f.read()
        
    # Replace Title
    admin_html = admin_html.replace('<title>Admin Dashboard - STACKLY</title>', f'<title>{title} - STACKLY</title>')
    
    # Update sidebar active state
    # First, remove active from all
    admin_html = admin_html.replace('class="active"><i class="fa-solid fa-gauge"></i> Overview</a>', '><i class="fa-solid fa-gauge"></i> Overview</a>')
    
    # Then add active to the target link
    if active_sidebar_link == 'Customers':
        admin_html = admin_html.replace('href="Customers.html"><i class="fa-solid fa-users"></i> Customers</a>', 'href="Customers.html" class="active"><i class="fa-solid fa-users"></i> Customers</a>')
    elif active_sidebar_link == 'Invoices':
        admin_html = admin_html.replace('href="Invoices.html"><i class="fa-solid fa-file-invoice"></i> Invoices</a>', 'href="Invoices.html" class="active"><i class="fa-solid fa-file-invoice"></i> Invoices</a>')
    elif active_sidebar_link == 'Reports':
        admin_html = admin_html.replace('href="Reports.html"><i class="fa-solid fa-chart-line"></i> Reports</a>', 'href="Reports.html" class="active"><i class="fa-solid fa-chart-line"></i> Reports</a>')
    elif active_sidebar_link == 'Settings':
        admin_html = admin_html.replace('href="Settings.html"><i class="fa-solid fa-gear"></i> Settings</a>', 'href="Settings.html" class="active"><i class="fa-solid fa-gear"></i> Settings</a>')

    # Replace main content
    start_main = admin_html.find('<main class="main-content">') + len('<main class="main-content">')
    end_main = admin_html.find('</main>')
    
    final_html = admin_html[:start_main] + '\n' + content_html + '\n        ' + admin_html[end_main:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Created {filename}")

customers_content = """
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;" data-aos="fade-right">
                <h2>Customers</h2>
                <button class="btn btn-primary" style="padding: 0.5rem 1rem;"><i class="fa-solid fa-plus"></i> Add Customer</button>
            </div>

            <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
                    <div style="position: relative; width: 100%; max-width: 300px;">
                        <i class="fa-solid fa-search" style="position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: var(--text-muted);"></i>
                        <input type="text" placeholder="Search customers..." style="width: 100%; padding: 0.5rem 1rem 0.5rem 2.5rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                    </div>
                </div>
                <div style="overflow-x: auto;">
                    <table>
                        <thead>
                            <tr>
                                <th>Name</th>
                                <th>Email</th>
                                <th>Plan</th>
                                <th>Status</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Acme Corp</td>
                                <td>billing@acmecorp.com</td>
                                <td>Enterprise</td>
                                <td><span class="status paid">Active</span></td>
                                <td>
                                    <a href="404.html" style="color: var(--text-muted); margin-right: 10px;"><i class="fa-solid fa-pen"></i></a>
                                    <a href="404.html" style="color: #ef4444;"><i class="fa-solid fa-trash"></i></a>
                                </td>
                            </tr>
                            <tr>
                                <td>Globex Inc</td>
                                <td>finance@globex.com</td>
                                <td>Pro</td>
                                <td><span class="status paid">Active</span></td>
                                <td>
                                    <a href="404.html" style="color: var(--text-muted); margin-right: 10px;"><i class="fa-solid fa-pen"></i></a>
                                    <a href="404.html" style="color: #ef4444;"><i class="fa-solid fa-trash"></i></a>
                                </td>
                            </tr>
                            <tr>
                                <td>Soylent Corp</td>
                                <td>accounts@soylent.com</td>
                                <td>Basic</td>
                                <td><span class="status pending">Past Due</span></td>
                                <td>
                                    <a href="404.html" style="color: var(--text-muted); margin-right: 10px;"><i class="fa-solid fa-pen"></i></a>
                                    <a href="404.html" style="color: #ef4444;"><i class="fa-solid fa-trash"></i></a>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

invoices_content = """
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;" data-aos="fade-right">
                <h2>Invoices</h2>
                <button class="btn btn-primary" style="padding: 0.5rem 1rem;"><i class="fa-solid fa-plus"></i> Create Invoice</button>
            </div>

            <!-- Stats -->
            <div class="stat-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin-bottom: 2rem;">
                <div class="stat-card" data-aos="fade-left" data-aos-delay="100">
                    <div class="stat-details">
                        <p>Total Outstanding</p>
                        <h3>$12,450</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-left" data-aos-delay="200">
                    <div class="stat-details">
                        <p>Overdue</p>
                        <h3 style="color: #ef4444;">$3,200</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-left" data-aos-delay="300">
                    <div class="stat-details">
                        <p>Paid This Month</p>
                        <h3 style="color: var(--primary-color);">$28,100</h3>
                    </div>
                </div>
            </div>

            <div class="table-container" data-aos="fade-up" data-aos-delay="400">
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem; flex-wrap: wrap;">
                    <select style="padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        <option value="">All Statuses</option>
                        <option value="paid">Paid</option>
                        <option value="pending">Pending</option>
                        <option value="overdue">Overdue</option>
                    </select>
                </div>
                <div style="overflow-x: auto;">
                    <table>
                        <thead>
                            <tr>
                                <th>Invoice ID</th>
                                <th>Customer</th>
                                <th>Amount</th>
                                <th>Issue Date</th>
                                <th>Due Date</th>
                                <th>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#INV-00128</td>
                                <td>Acme Corp</td>
                                <td>$1,500.00</td>
                                <td>Aug 05, 2026</td>
                                <td>Sep 05, 2026</td>
                                <td><span class="status pending">Pending</span></td>
                            </tr>
                            <tr>
                                <td>#INV-00127</td>
                                <td>Initech</td>
                                <td>$890.00</td>
                                <td>Jul 25, 2026</td>
                                <td>Aug 25, 2026</td>
                                <td><span class="status paid">Paid</span></td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

reports_content = """
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; flex-wrap: wrap; gap: 1rem;" data-aos="fade-right">
                <h2>Reports & Analytics</h2>
                <div style="display: flex; gap: 1rem;">
                    <button class="btn btn-outline" style="padding: 0.5rem 1rem;"><i class="fa-solid fa-download"></i> CSV</button>
                    <button class="btn btn-outline" style="padding: 0.5rem 1rem;"><i class="fa-solid fa-file-pdf"></i> PDF</button>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem;">
                
                <div class="table-container" data-aos="zoom-in" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Revenue Growth</h3>
                    <!-- Chart Mockup -->
                    <div style="width: 100%; height: 250px; border-bottom: 1px solid var(--glass-border); border-left: 1px solid var(--glass-border); position: relative; display: flex; align-items: flex-end; justify-content: space-around; padding-bottom: 10px;">
                        <div style="width: 15%; height: 40%; background: var(--primary-color); border-radius: 4px 4px 0 0; opacity: 0.7;"></div>
                        <div style="width: 15%; height: 60%; background: var(--primary-color); border-radius: 4px 4px 0 0; opacity: 0.8;"></div>
                        <div style="width: 15%; height: 50%; background: var(--primary-color); border-radius: 4px 4px 0 0; opacity: 0.75;"></div>
                        <div style="width: 15%; height: 85%; background: var(--primary-color); border-radius: 4px 4px 0 0; opacity: 0.9;"></div>
                        <div style="width: 15%; height: 100%; background: var(--primary-color); border-radius: 4px 4px 0 0;"></div>
                    </div>
                </div>

                <div class="table-container" data-aos="zoom-in" data-aos-delay="200">
                    <h3 style="margin-bottom: 1rem;">Subscriber Churn</h3>
                    <!-- Chart Mockup Line -->
                    <div style="width: 100%; height: 250px; background: linear-gradient(180deg, rgba(239, 68, 68, 0.2) 0%, transparent 100%); border-radius: 8px; position: relative; overflow: hidden; border-bottom: 1px solid var(--glass-border); border-left: 1px solid var(--glass-border);">
                        <!-- SVG path to simulate line chart -->
                        <svg viewBox="0 0 100 100" preserveAspectRatio="none" style="width: 100%; height: 100%;">
                            <path d="M0,80 L20,70 L40,90 L60,50 L80,60 L100,20" fill="none" stroke="#ef4444" stroke-width="2" />
                        </svg>
                    </div>
                </div>
            </div>
"""

settings_content = """
            <h2 style="margin-bottom: 2rem;" data-aos="fade-right">Settings</h2>

            <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem;">
                
                <div class="table-container" data-aos="fade-up" data-aos-delay="100">
                    <h3 style="margin-bottom: 1rem;">Profile Settings</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Full Name</label>
                            <input type="text" value="Admin User" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                        <div>
                            <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Email Address</label>
                            <input type="email" value="admin@stackly.com" style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                        </div>
                    </div>
                    <button class="btn btn-primary" style="margin-top: 1rem; padding: 0.5rem 1rem;">Save Changes</button>
                </div>

                <div class="table-container" data-aos="fade-up" data-aos-delay="200">
                    <h3 style="margin-bottom: 1rem;">Notifications</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--glass-border); padding-bottom: 1rem; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
                        <div>
                            <h4>Email Alerts</h4>
                            <p style="color: var(--text-muted); font-size: 0.9rem;">Receive email when an invoice is paid.</p>
                        </div>
                        <div style="width: 50px; height: 26px; background: var(--primary-color); border-radius: 13px; position: relative; cursor: pointer;">
                            <div style="width: 22px; height: 22px; background: white; border-radius: 50%; position: absolute; top: 2px; right: 2px;"></div>
                        </div>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                        <div>
                            <h4>Weekly Summary</h4>
                            <p style="color: var(--text-muted); font-size: 0.9rem;">Receive a weekly report of revenue.</p>
                        </div>
                        <div style="width: 50px; height: 26px; background: rgba(255,255,255,0.1); border-radius: 13px; position: relative; cursor: pointer; border: 1px solid var(--glass-border);">
                            <div style="width: 22px; height: 22px; background: var(--text-muted); border-radius: 50%; position: absolute; top: 1px; left: 2px;"></div>
                        </div>
                    </div>
                </div>

            </div>
"""

create_page('Customers.html', 'Customers', customers_content, 'Customers')
create_page('Invoices.html', 'Invoices', invoices_content, 'Invoices')
create_page('Reports.html', 'Reports', reports_content, 'Reports')
create_page('Settings.html', 'Settings', settings_content, 'Settings')
