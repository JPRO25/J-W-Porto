import re

with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Update siro
content = re.sub(
    r'(siro:\s*\{\s*title:[^\n]+,\s*tag:[^\n]+,\s*videoFormat:\s*")([^"]+)(",)',
    r'\1portrait\3\n        reelId: "DCtsULoyzDw",',
    content
)

# Update bluecheck
content = re.sub(
    r'(bluecheck:\s*\{\s*title:[^\n]+,\s*tag:[^\n]+,\s*videoFormat:\s*")([^"]+)(",)',
    r'\1portrait\3\n        reelId: "DaSWXxUpJLh",',
    content
)

# Update the placeholder
old_placeholder = """        videoSection = `
            <div class="modal-video-placeholder">
                <i class="fa-solid fa-laptop-code" style="color: #c85a3c;"></i>
                <span>Video Dokumentasi Desktop (16:9)</span>
            </div>
        `;"""
        
new_placeholder = """        videoSection = `
            <div class="modal-video-placeholder" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; background: rgba(255,255,255,0.02); border: 1px dashed rgba(255,255,255,0.1); border-radius: 12px; padding: 3rem; text-align: center;">
                <i class="fa-solid fa-video-slash" style="font-size: 2rem; color: #c85a3c;"></i>
                <span style="color: #888; font-size: 0.9rem; font-style: italic;">Status: Belum Update<br>(masih mengumpulkan asset video)</span>
            </div>
        `;"""

content = content.replace(old_placeholder, new_placeholder)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated script.js")
