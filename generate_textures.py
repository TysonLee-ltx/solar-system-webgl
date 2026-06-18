import base64
import os
from pathlib import Path

texture_dir = Path("textures")

output_js = Path("textures_base64.js")

image_exts = {'.jpg','.jpeg','.png','.gif','.bmp'}

data = {}

for file in texture_dir.iterdir():
    if file.suffix.lower() in image_exts:
        with open(file,"rb") as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        ext = file.suffix.lower()
        mime = {
            '.jpg' : 'image/jpeg',
            '.jpeg' : 'image/jpeg',
            '.png' : 'image/png',
            '.gif' : 'image/gif',
            '.bmp' : 'image/bmp'
        }[ext]

        data[file.name] = f"data:{mime};base64,{b64}"

with open(output_js, "w", encoding="utf-8") as f:
    f.write("//自动生成的纹理 Base64 数据\n")
    f.write("const textureBase64 = {\n")
    for name,url in data.items():
        f.write(f'  "{name}":"{url}",\n')
    f.write("};\n")

print(f" 已生成 {output_js} ,包含 {len(data)} 个纹理")