import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove color from devicons to show their original colors
# We find class="devicon-... and style="..." and remove `color: var(--accent-cyan);`
content = re.sub(r'(class="devicon-[^"]+"[^>]*style="[^"]*)color:\s*var\(--accent-cyan\);\s*', r'\1', content)

# Restore specific colors for FontAwesome icons
content = content.replace('class="fa-solid fa-brain" style="font-size: 1.8rem; color: var(--accent-cyan);"', 'class="fa-solid fa-brain skill-icon" style="font-size: 1.8rem; color: #e28a07;"')
content = content.replace('class="fa-solid fa-print" style="font-size: 1.8rem; color: var(--accent-cyan);"', 'class="fa-solid fa-print skill-icon" style="font-size: 1.8rem; color: #9333ea;"')

# Clean up empty style attributes if any (optional, but good practice)
content = content.replace('style="font-size: 1.8rem; "', 'style="font-size: 1.8rem;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
