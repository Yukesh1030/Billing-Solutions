import os
import re

def inject_before_main_end(filename, injection_html):
    if not os.path.exists(filename):
        print(f"Skipping {filename}, not found.")
        return
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Find </main>
    idx = html.find('</main>')
    if idx == -1:
        print(f"Could not find </main> in {filename}")
        return
        
    final_html = html[:idx] + "\n" + injection_html + "\n" + html[idx:]
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)
        
    print(f"Injected sections into {filename}")

admin_html = """
            <!-- 1. Quick Actions Panel -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3>Quick Actions</h3>
                <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1rem;">
                    <a href="#" class="btn btn-primary"><i class="fa-solid fa-plus"></i> Create Invoice</a>
                    <a href="#" class="btn btn-outline"><i class="fa-solid fa-user-plus"></i> Add Customer</a>
                    <a href="#" class="btn btn-outline"><i class="fa-solid fa-file-export"></i> Generate Report</a>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 2. Recent Activity Feed -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Recent Activity</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="margin-bottom: 1rem; border-left: 2px solid var(--primary-color); padding-left: 10px;">
                            <p style="margin: 0; font-size: 0.9rem;"><strong>Acme Corp</strong> paid Invoice #INV-00124</p>
                            <small style="color: var(--text-muted);">10 mins ago</small>
                        </li>
                        <li style="margin-bottom: 1rem; border-left: 2px solid var(--primary-color); padding-left: 10px;">
                            <p style="margin: 0; font-size: 0.9rem;"><strong>Globex Inc</strong> upgraded to Pro Plan</p>
                            <small style="color: var(--text-muted);">1 hour ago</small>
                        </li>
                        <li style="border-left: 2px solid #ef4444; padding-left: 10px;">
                            <p style="margin: 0; font-size: 0.9rem;"><strong>Soylent Corp</strong> payment failed</p>
                            <small style="color: var(--text-muted);">2 hours ago</small>
                        </li>
                    </ul>
                </div>

                <!-- 3. Top Performing Plans -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Top Performing Plans</h3>
                    <div style="margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span>Pro Plan</span><span>55%</span>
                        </div>
                        <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; margin-bottom: 1rem;">
                            <div style="width: 55%; height: 100%; background: var(--primary-color); border-radius: 4px;"></div>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span>Enterprise</span><span>30%</span>
                        </div>
                        <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px; margin-bottom: 1rem;">
                            <div style="width: 30%; height: 100%; background: var(--primary-color); border-radius: 4px;"></div>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span>Basic Plan</span><span>15%</span>
                        </div>
                        <div style="width: 100%; height: 8px; background: rgba(255,255,255,0.1); border-radius: 4px;">
                            <div style="width: 15%; height: 100%; background: var(--primary-color); border-radius: 4px;"></div>
                        </div>
                    </div>
                </div>

                <!-- 4. Upcoming Renewals -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Upcoming Renewals (7 Days)</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="display: flex; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>Initech (Enterprise)</span> <span style="color: var(--text-muted);">Aug 10</span>
                        </li>
                        <li style="display: flex; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>Umbrella Corp (Pro)</span> <span style="color: var(--text-muted);">Aug 11</span>
                        </li>
                        <li style="display: flex; justify-content: space-between;">
                            <span>Massive Dynamic (Pro)</span> <span style="color: var(--text-muted);">Aug 12</span>
                        </li>
                    </ul>
                </div>
            </div>
"""

customers_html = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 1. Customer Demographics -->
                <div class="stat-card" data-aos="fade-up">
                    <div class="stat-details">
                        <p>Total Customers</p>
                        <h3>2,450</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-up">
                    <div class="stat-details">
                        <p>Active</p>
                        <h3 style="color: var(--primary-color);">2,100</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-up">
                    <div class="stat-details">
                        <p>Churned</p>
                        <h3 style="color: #ef4444;">150</h3>
                    </div>
                </div>
                <div class="stat-card" data-aos="fade-up">
                    <div class="stat-details">
                        <p>In Trial</p>
                        <h3 style="color: #3b82f6;">200</h3>
                    </div>
                </div>
            </div>

            <!-- 2. Recent Signups -->
            <div class="table-container" style="margin-top: 2rem;" data-aos="fade-up">
                <h3>Recent Signups</h3>
                <div style="display: flex; gap: 1rem; overflow-x: auto; padding-top: 1rem; padding-bottom: 1rem;">
                    <div style="min-width: 150px; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                        <div style="width:40px; height:40px; border-radius:50%; background:var(--primary-color); margin: 0 auto 0.5rem auto; display:flex; align-items:center; justify-content:center; color:var(--bg-dark); font-weight:bold;">S</div>
                        <h4>Stark Ind.</h4>
                        <small style="color: var(--text-muted);">2 hours ago</small>
                    </div>
                    <div style="min-width: 150px; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                        <div style="width:40px; height:40px; border-radius:50%; background:var(--primary-color); margin: 0 auto 0.5rem auto; display:flex; align-items:center; justify-content:center; color:var(--bg-dark); font-weight:bold;">W</div>
                        <h4>Wayne Ent.</h4>
                        <small style="color: var(--text-muted);">5 hours ago</small>
                    </div>
                    <div style="min-width: 150px; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                        <div style="width:40px; height:40px; border-radius:50%; background:var(--primary-color); margin: 0 auto 0.5rem auto; display:flex; align-items:center; justify-content:center; color:var(--bg-dark); font-weight:bold;">O</div>
                        <h4>Oscorp</h4>
                        <small style="color: var(--text-muted);">1 day ago</small>
                    </div>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 3. Plan Distribution -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Plan Distribution</h3>
                    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
                        <div style="width: 150px; height: 150px; border-radius: 50%; background: conic-gradient(var(--primary-color) 0% 55%, #3b82f6 55% 85%, #64748b 85% 100%);"></div>
                    </div>
                    <div style="display: flex; justify-content: center; gap: 1rem; margin-top: 1rem; font-size: 0.8rem;">
                        <span style="display:flex; align-items:center; gap:5px;"><div style="width:10px;height:10px;background:var(--primary-color);border-radius:50%;"></div> Pro (55%)</span>
                        <span style="display:flex; align-items:center; gap:5px;"><div style="width:10px;height:10px;background:#3b82f6;border-radius:50%;"></div> Enterprise (30%)</span>
                        <span style="display:flex; align-items:center; gap:5px;"><div style="width:10px;height:10px;background:#64748b;border-radius:50%;"></div> Basic (15%)</span>
                    </div>
                </div>

                <!-- 4. At-Risk Customers -->
                <div class="table-container" data-aos="fade-up">
                    <h3>At-Risk Customers</h3>
                    <table style="margin-top: 1rem;">
                        <thead>
                            <tr>
                                <th>Customer</th>
                                <th>Reason</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Soylent Corp</td>
                                <td style="color: #ef4444;">Payment Failed</td>
                            </tr>
                            <tr>
                                <td>Hooli</td>
                                <td style="color: #f59e0b;">No login (30 days)</td>
                            </tr>
                            <tr>
                                <td>Goliath Nat.</td>
                                <td style="color: #f59e0b;">Usage Dropped 50%</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
"""

invoices_html = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 1. Aging Summary -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Aging Summary</h3>
                    <div style="margin-top: 1rem; display: flex; flex-direction: column; gap: 1rem;">
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>1 - 30 Days</span><span>$5,200</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span>31 - 60 Days</span><span style="color: #f59e0b;">$1,800</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span>60+ Days</span><span style="color: #ef4444;">$1,400</span>
                        </div>
                    </div>
                </div>

                <!-- 2. Failed Payments Alerts -->
                <div class="table-container" style="border-left: 4px solid #ef4444;" data-aos="fade-up">
                    <h3 style="color: #ef4444;">Failed Payments Alerts</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="margin-bottom: 1rem;">
                            <p style="margin: 0;"><strong>#INV-00121 (Soylent Corp)</strong></p>
                            <small style="color: var(--text-muted);">Card declined - Insufficient funds</small>
                        </li>
                        <li>
                            <p style="margin: 0;"><strong>#INV-00098 (Hooli)</strong></p>
                            <small style="color: var(--text-muted);">Card expired</small>
                        </li>
                    </ul>
                </div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 3. Draft Invoices -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Draft Invoices</h3>
                    <table style="margin-top: 1rem;">
                        <thead>
                            <tr>
                                <th>Invoice ID</th>
                                <th>Customer</th>
                                <th>Amount</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>#INV-00129</td>
                                <td>Stark Ind.</td>
                                <td>$5,000.00</td>
                                <td><a href="#" style="color: var(--primary-color);">Send</a></td>
                            </tr>
                            <tr>
                                <td>#INV-00130</td>
                                <td>Wayne Ent.</td>
                                <td>$2,500.00</td>
                                <td><a href="#" style="color: var(--primary-color);">Send</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- 4. Payment Gateways Status -->
                <div class="table-container" data-aos="fade-up">
                    <h3>Payment Gateways</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem; margin-top: 1rem;">
                        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
                            <span><i class="fa-brands fa-stripe" style="font-size: 1.5rem; vertical-align: middle; margin-right: 10px;"></i> Stripe</span>
                            <span class="status paid">Connected</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
                            <span><i class="fa-brands fa-paypal" style="font-size: 1.5rem; vertical-align: middle; margin-right: 10px;"></i> PayPal</span>
                            <span class="status paid">Connected</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
                            <span><i class="fa-solid fa-building-columns" style="font-size: 1.2rem; vertical-align: middle; margin-right: 10px;"></i> Bank Transfer</span>
                            <span class="status pending">Pending Verification</span>
                        </div>
                    </div>
                </div>
            </div>
"""

reports_html = """
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                <!-- 1. MRR Breakdown -->
                <div class="table-container" data-aos="zoom-in">
                    <h3 style="margin-bottom: 1rem;">MRR by Tier</h3>
                    <div style="display: flex; flex-direction: column; gap: 1rem;">
                        <div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><small>Enterprise</small><small>$25,000</small></div>
                            <div style="width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px;"><div style="width: 60%; height: 100%; background: var(--primary-color); border-radius: 5px;"></div></div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><small>Pro</small><small>$12,000</small></div>
                            <div style="width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px;"><div style="width: 30%; height: 100%; background: #3b82f6; border-radius: 5px;"></div></div>
                        </div>
                        <div>
                            <div style="display: flex; justify-content: space-between; margin-bottom: 5px;"><small>Basic</small><small>$5,500</small></div>
                            <div style="width: 100%; height: 10px; background: rgba(255,255,255,0.1); border-radius: 5px;"><div style="width: 15%; height: 100%; background: #64748b; border-radius: 5px;"></div></div>
                        </div>
                    </div>
                </div>

                <!-- 2. Customer Acquisition Cost (CAC) -->
                <div class="table-container" data-aos="zoom-in">
                    <h3 style="margin-bottom: 1rem;">CAC vs LTV</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; height: 100px;">
                        <div style="text-align: center;">
                            <p style="color: var(--text-muted); font-size: 0.9rem;">Avg. CAC</p>
                            <h2 style="color: #ef4444;">$150</h2>
                        </div>
                        <div style="text-align: center;">
                            <i class="fa-solid fa-arrow-right-arrow-left" style="font-size: 1.5rem; color: var(--glass-border);"></i>
                        </div>
                        <div style="text-align: center;">
                            <p style="color: var(--text-muted); font-size: 0.9rem;">Avg. LTV</p>
                            <h2 style="color: var(--primary-color);">$2,400</h2>
                        </div>
                    </div>
                    <div style="text-align: center; color: var(--primary-color); margin-top: 1rem;"><i class="fa-solid fa-arrow-trend-up"></i> Healthy Ratio (16x)</div>
                </div>

                <!-- 3. Trial Conversion Rate -->
                <div class="table-container" data-aos="zoom-in">
                    <h3 style="margin-bottom: 1rem;">Trial Conversion</h3>
                    <div style="text-align: center; padding: 2rem 0;">
                        <h1 style="font-size: 4rem; color: var(--primary-color); margin: 0;">42%</h1>
                        <p style="color: var(--text-muted); margin-top: 1rem;">Of trials converted to paid plans this month.</p>
                    </div>
                </div>

                <!-- 4. Top Revenue Regions -->
                <div class="table-container" data-aos="zoom-in">
                    <h3 style="margin-bottom: 1rem;">Top Regions</h3>
                    <ul style="list-style: none; padding: 0; margin-top: 1rem;">
                        <li style="display: flex; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span><i class="fa-solid fa-earth-americas" style="margin-right: 10px;"></i> North America</span> <span>$28,000</span>
                        </li>
                        <li style="display: flex; justify-content: space-between; margin-bottom: 1rem; border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem;">
                            <span><i class="fa-solid fa-earth-europe" style="margin-right: 10px;"></i> Europe</span> <span>$10,500</span>
                        </li>
                        <li style="display: flex; justify-content: space-between;">
                            <span><i class="fa-solid fa-earth-asia" style="margin-right: 10px;"></i> Asia Pacific</span> <span>$4,000</span>
                        </li>
                    </ul>
                </div>
            </div>
"""

settings_html = """
            <div style="display: grid; grid-template-columns: 1fr; gap: 1.5rem; margin-top: 1.5rem;">
                
                <!-- 1. Security & 2FA -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Security</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--glass-border); padding-bottom: 1rem; margin-bottom: 1rem; flex-wrap: wrap; gap: 1rem;">
                        <div>
                            <h4>Two-Factor Authentication (2FA)</h4>
                            <p style="color: var(--text-muted); font-size: 0.9rem;">Add an extra layer of security to your account.</p>
                        </div>
                        <button class="btn btn-primary" style="padding: 0.5rem 1rem;">Enable 2FA</button>
                    </div>
                    <div>
                        <h4>Active Sessions</h4>
                        <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1rem;">Manage devices currently logged in to your account.</p>
                        <div style="display: flex; justify-content: space-between; background: rgba(255,255,255,0.05); padding: 1rem; border-radius: 8px;">
                            <span><i class="fa-solid fa-laptop" style="margin-right:10px;"></i> Mac OS - Chrome (Current)</span>
                            <a href="#" style="color: #ef4444;">Revoke</a>
                        </div>
                    </div>
                </div>

                <!-- 2. Team Management -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Team Members</h3>
                    <form class="redirect-404 dashboard-form" style="display: flex; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap;">
                        <input type="email" required placeholder="member@company.com" style="flex: 1; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main); min-width: 200px;">
                        <select required style="padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                            <option value="">Select Role</option>
                            <option value="admin">Admin</option>
                            <option value="editor">Editor</option>
                            <option value="viewer">Viewer</option>
                        </select>
                        <button type="submit" class="btn btn-primary" style="padding: 0.5rem 1rem;">Invite</button>
                    </form>
                    <table style="margin-top: 1rem;">
                        <thead>
                            <tr>
                                <th>User</th>
                                <th>Role</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>admin@stackly.com</td>
                                <td>Admin</td>
                                <td style="color: var(--text-muted);">Owner</td>
                            </tr>
                            <tr>
                                <td>finance@stackly.com</td>
                                <td>Editor</td>
                                <td><a href="#" style="color: #ef4444;">Remove</a></td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- 3. Integrations & API -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">Integrations</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem;">
                        <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                            <i class="fa-brands fa-slack" style="font-size: 2rem; color: #E01E5A; margin-bottom: 1rem;"></i>
                            <h4>Slack</h4>
                            <button class="btn btn-outline" style="width: 100%; margin-top: 1rem; padding: 0.5rem;">Connect</button>
                        </div>
                        <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                            <i class="fa-brands fa-stripe" style="font-size: 2rem; color: #635bff; margin-bottom: 1rem;"></i>
                            <h4>Stripe</h4>
                            <button class="btn btn-primary" style="width: 100%; margin-top: 1rem; padding: 0.5rem; background: rgba(255,255,255,0.1); color: var(--text-main);">Connected</button>
                        </div>
                        <div style="background: rgba(255,255,255,0.05); padding: 1.5rem; border-radius: 8px; text-align: center; border: 1px solid var(--glass-border);">
                            <img src="https://cdn.iconscout.com/icon/free/png-256/zapier-282245.png" alt="Zapier" style="height: 32px; filter: grayscale(100%) brightness(200%); margin-bottom: 1rem;">
                            <h4>Zapier</h4>
                            <button class="btn btn-outline" style="width: 100%; margin-top: 1rem; padding: 0.5rem;">Connect</button>
                        </div>
                    </div>
                </div>

                <!-- 4. System Preferences -->
                <div class="table-container" data-aos="fade-up">
                    <h3 style="margin-bottom: 1rem;">System Preferences</h3>
                    <form class="redirect-404 dashboard-form">
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-bottom: 1rem;">
                            <div>
                                <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Default Currency</label>
                                <select required style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                                    <option value="USD">USD ($)</option>
                                    <option value="EUR">EUR (€)</option>
                                    <option value="GBP">GBP (£)</option>
                                </select>
                            </div>
                            <div>
                                <label style="display: block; color: var(--text-muted); margin-bottom: 0.5rem;">Timezone</label>
                                <select required style="width: 100%; padding: 0.5rem 1rem; border-radius: 6px; background: rgba(255,255,255,0.05); border: 1px solid var(--glass-border); color: var(--text-main);">
                                    <option value="UTC">UTC</option>
                                    <option value="EST">Eastern Time (EST)</option>
                                    <option value="PST">Pacific Time (PST)</option>
                                </select>
                            </div>
                        </div>
                        <button type="submit" class="btn btn-primary" style="padding: 0.5rem 1rem;">Save Preferences</button>
                    </form>
                </div>
            </div>
"""

inject_before_main_end('AdminDashboard.html', admin_html)
inject_before_main_end('Customers.html', customers_html)
inject_before_main_end('Invoices.html', invoices_html)
inject_before_main_end('Reports.html', reports_html)
inject_before_main_end('Settings.html', settings_html)

