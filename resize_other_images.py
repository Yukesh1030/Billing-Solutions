import os
from PIL import Image

def optimize_image(input_path, output_path, min_kb=70, max_kb=90):
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    low, high = 1, 100
    
    for i in range(10):
        mid = (low + high) // 2
        img.save(output_path, 'WEBP', quality=mid)
        size_kb = os.path.getsize(output_path) / 1024
        
        if min_kb <= size_kb <= max_kb:
            print(f"Success! {output_path} is {size_kb:.2f}KB at quality {mid}")
            return
        elif size_kb < min_kb:
            low = mid + 1
        else:
            high = mid - 1
            
    print(f"Fallback for {output_path} at size {os.path.getsize(output_path)/1024:.2f}KB")

images = [
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\ai_growth_1785817547203.png", "ai_growth.webp"),
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\global_map_1785817564262.png", "global_map.webp")
]

output_dir = r"d:\yukesh\projects\Billing Solutions\assets"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for in_path, out_name in images:
    out_path = os.path.join(output_dir, out_name)
    try:
        optimize_image(in_path, out_path)
    except Exception as e:
        print(f"Failed to process {in_path}: {e}")
