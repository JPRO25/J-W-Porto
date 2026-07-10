import os
import urllib.parse

cert_dir = r'C:\Users\Julman Waruwu\Documents\j&w-porto\assets\certificates'
html_file = r'C:\Users\Julman Waruwu\Documents\j&w-porto\index.html'

if not os.path.exists(cert_dir):
    print('Cert dir not found')
    exit()

files = os.listdir(cert_dir)
files = [f for f in files if f.endswith(('.pdf', '.jpg', '.png')) and f != 'ipb.png']

priority = [
    "CCNA_Introduction_to_Networks.pdf",
    "Samsung_Innovation_Campus_Batch_6.pdf",
    "Hacktiv8_FrontEnd_React.pdf",
    "Dicoding_Generative_AI.pdf",
    "Dicoding_Data_Science_Fundamentals.pdf",
    "Dicoding_AI_Fundamentals.pdf"
]

def sort_key(f):
    if f in priority:
        return (0, priority.index(f))
    return (1, f)

files.sort(key=sort_key)

html_snippets = []
html_snippets.append('            <div class="cert-grid">')

for i, f in enumerate(files):
    name_no_ext = os.path.splitext(f)[0]
    title = name_no_ext.replace('_', ' ')
    
    issuer = 'Certificate'
    if 'Dicoding' in f: issuer = 'Dicoding Indonesia'
    elif 'Udemy' in f: issuer = 'Udemy'
    elif 'Hacktiv8' in f: issuer = 'HACKTIV8'
    elif 'CCNA' in f: issuer = 'Cisco Networking Academy'
    elif 'Samsung' in f: issuer = 'Samsung'
    elif 'BCA' in f: issuer = 'BCA'
    
    icon = 'fa-solid fa-award'
    if 'AI' in title.upper() or 'Machine Learning' in title: icon = 'fa-solid fa-brain'
    elif 'Data' in title or 'SQL' in title.upper() or 'Query' in title: icon = 'fa-solid fa-database'
    elif 'Python' in title: icon = 'fa-brands fa-python'
    elif 'React' in title: icon = 'fa-brands fa-react'
    elif 'Network' in title: icon = 'fa-solid fa-network-wired'

    encoded_f = urllib.parse.quote(f)
    hidden_class = " hidden-cert" if i >= 6 else ""

    # Using a card design for certificates
    html = f'''                <!-- Cert {i+1}: {title} -->
                <a href=\"assets/certificates/{encoded_f}\" target=\"_blank\" class=\"cert-card{hidden_class}\" title=\"View {title}\">
                    <div class=\"cert-card-header\">
                        <i class=\"{icon} cert-icon\"></i>
                        <span class=\"cert-year\">2024</span>
                    </div>
                    <div class=\"cert-card-body\">
                        <h4 class=\"cert-title\">{title}</h4>
                        <span class=\"cert-issuer\">{issuer}</span>
                    </div>
                </a>'''
    html_snippets.append(html)

html_snippets.append('            </div>') # close cert-grid

if len(files) > 6:
    html_snippets.append(f'''                <div class="see-all-certs-container" style="text-align: center; width: 100%; margin-top: 2.5rem;">
                    <button id="seeAllCertsBtn" class="btn-primary" style="padding: 0.8rem 2rem; font-size: 1rem; cursor: pointer; border-radius: 5px; border: none; background: #00ff88; color: #1a1a2e; font-weight: 700;">View All Certificates</button>
                </div>''')

all_certs_html = '\n'.join(html_snippets)

with open(html_file, 'r', encoding='utf-8') as file:
    content = file.read()

# We need to replace the old <div class="credentials-list"> block
# In the original file, it might be <div class="credentials-list"> or <div class="cert-grid"> if run multiple times
start_marker = '            <div class=\"certificates-list\">'
if start_marker not in content:
    start_marker = '            <div class=\"cert-grid\">'

end_marker = '        </section>'

start_idx = content.find(start_marker)
# Find the exact </section> that closes the credentials-sec section
if start_idx != -1:
    end_idx = content.find(end_marker, start_idx)
    if end_idx != -1:
        new_content = content[:start_idx] + all_certs_html + '\n' + content[end_idx:]
        with open(html_file, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print('Successfully updated HTML')
    else:
        print('End marker not found')
else:
    print('Start marker not found')
