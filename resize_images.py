import os
from PIL import Image

def optimize_image(input_path, output_path, min_kb=70, max_kb=90):
    img = Image.open(input_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    low, high = 1, 100
    best_quality = 80
    
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
            
    # Fallback to nearest if we couldn't hit exact range
    print(f"Fallback for {output_path} at size {os.path.getsize(output_path)/1024:.2f}KB")

images = [
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\home_cover_1785746365916.png", "home_cover.webp"),
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\billing_cover_1785746384270.png", "billing_cover.webp"),
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\pricing_cover_1785746401958.png", "pricing_cover.webp"),
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\resources_cover_1785746418283.png", "resources_cover.webp"),
    (r"C:\Users\YUKESH G\.gemini\antigravity-ide\brain\7cce27f4-97f7-450e-af9a-6984e6f6a917\contact_cover_1785746435807.png", "contact_cover.webp")
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
