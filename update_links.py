import os
import re

files_to_check = ['index.html', 'BillingSolutions.html', 'Pricing.html', 'Resources.html', 'Contact.html', '404.html']
exclude_hrefs = ['Login.html', 'Signup.html', 'AdminDashboard.html', 'ClientDashboard.html', '404.html', '#']

for filename in files_to_check:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # We want to replace href inside <a> tags, but NOT inside <nav> or <footer>.
    # We can do this by iterating through the string and keeping track of whether we are inside nav or footer.
    
    result = []
    in_nav = False
    in_footer = False
    
    i = 0
    while i < len(html):
        if html[i:i+4].lower() == '<nav':
            in_nav = True
        elif html[i:i+6].lower() == '</nav>':
            in_nav = False
        elif html[i:i+7].lower() == '<footer':
            in_footer = True
        elif html[i:i+9].lower() == '</footer>':
            in_footer = False
            
        if html[i:i+2].lower() == '<a' and not in_nav and not in_footer:
            # find the end of the a tag
            end_tag = html.find('>', i)
            if end_tag != -1:
                a_tag = html[i:end_tag+1]
                # extract href
                href_match = re.search(r'href="([^"]+)"', a_tag)
                if href_match:
                    href_val = href_match.group(1)
                    if href_val not in exclude_hrefs:
                        # replace href
                        new_a_tag = re.sub(r'href="[^"]+"', 'href="404.html"', a_tag)
                        result.append(new_a_tag)
                        i = end_tag + 1
                        continue
        
        result.append(html[i])
        i += 1
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(result))

print("Links updated successfully.")
