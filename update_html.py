import os
import urllib.parse

cert_dir = r'C:\Users\Julman Waruwu\Documents\j&w-porto\assets\certificates'
html_file = r'C:\Users\Julman Waruwu\Documents\j&w-porto\index.html'

if not os.path.exists(cert_dir):
    print('Cert dir not found')
    exit()

files = os.listdir(cert_dir)
files = [f for f in files if f.endswith(('.pdf', '.jpg', '.png')) and f != 'ipb.png']

html_snippets = []
for i, f in enumerate(files):
    name_no_ext = os.path.splitext(f)[0]
    title = name_no_ext
    # some cleanups for title
    if title.startswith('Dicoding Certificate Competetion ['):
        title = title.replace('Dicoding Certificate Competetion [', '').replace(']', '').strip()
    if title.startswith('Udemy_Certificate ('):
        title = title.replace('Udemy_Certificate (', '').replace(')', '').strip()
    
    issuer = 'Certificate'
    if 'Dicoding' in f: issuer = 'Dicoding Indonesia'
    elif 'Udemy' in f: issuer = 'Udemy'
    elif 'HACTIV8' in f: issuer = 'HACKTIV8'
    elif 'CCNA' in f: issuer = 'Cisco Networking Academy'
    elif 'SIC' in f: issuer = 'Samsung'
    elif 'BCA' in f: issuer = 'BCA'
    
    icon = 'fa-solid fa-certificate'
    if 'AI' in title.upper() or 'Machine Learning' in title: icon = 'fa-solid fa-brain'
    elif 'Data' in title or 'SQL' in title.upper() or 'Query' in title: icon = 'fa-solid fa-database'
    elif 'Python' in title: icon = 'fa-brands fa-python'
    elif 'React' in title: icon = 'fa-brands fa-react'
    elif 'Network' in title: icon = 'fa-solid fa-network-wired'

    encoded_f = urllib.parse.quote(f)

    html = f'''                <!-- Cert {i+1}: {title} -->
                <div class=\"credential-item\" data-title=\"{title}\" data-issuer=\"{issuer}\" data-date=\"2024\" data-icon=\"{icon}\">
                    <span class=\"cred-year\">2024</span>
                    <div class=\"cred-main-info\">
                        <h4 class=\"cred-title\">{title}</h4>
                        <span class=\"cred-issuer\">{issuer}</span>
                    </div>
                    <a href=\"assets/certificates/{encoded_f}\" target=\"_blank\" class=\"cred-link-btn\" title=\"View Credential\"><i class=\"fa-solid fa-arrow-up-right-from-square\"></i></a>
                </div>'''
    html_snippets.append(html)

all_certs_html = '\n'.join(html_snippets)

with open(html_file, 'r', encoding='utf-8') as file:
    content = file.read()

start_marker = '            <div class=\"credentials-list\">'
end_marker = '            </div>\n        </section>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker, start_idx)

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx + len(start_marker)] + '\n' + all_certs_html + '\n' + content[end_idx:]
    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(new_content)
    print('Successfully updated HTML')
else:
    print('Markers not found')
