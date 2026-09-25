"""Resize the photos to the sizes the layout actually uses and emit WebP
alongside optimised JPEG fallbacks.

The originals were 960x1280 or larger regardless of how small they render —
the gallery thumbnails in particular were shipping about ten times the pixels
they display. Targets below are roughly 2x the CSS display width, so the
images stay sharp on retina screens without the waste.

Re-run after replacing any photo:  python optimize-images.py
"""

import os
from PIL import Image

# filename stem -> target width in pixels (height follows the aspect ratio)
# filename stem -> (target width, webp quality)
# The hero is the Largest Contentful Paint image, so it keeps the most
# quality. Gallery tiles render about 270px wide, so they need far less.
TARGETS = {
    "photo-hero-portrait": (760, 80),
    "photo-about-main": (760, 78),
    "photo-about-float": (520, 76),
    "photo-feature-wedding": (900, 78),
    "photo-feature-destination": (800, 78),
    "photo-gallery-1": (560, 74),
    "photo-gallery-2": (560, 74),
    "photo-gallery-3": (560, 74),
    "photo-gallery-4": (560, 74),
    "photo-gallery-5": (560, 74),
    "photo-gallery-6": (560, 74),
    "photo-gallery-7": (560, 74),
    "photo-gallery-8": (560, 74),
}

JPEG_QUALITY = 80

before = after = 0
print(f"{'file':<34}{'was':>9}{'jpg':>9}{'webp':>9}  dimensions")
print("-" * 74)

for stem, (target_w, webp_quality) in TARGETS.items():
    src = os.path.join("images", stem + ".jpg")
    if not os.path.exists(src):
        print(f"{stem:<34}  MISSING, skipped")
        continue

    original_size = os.path.getsize(src)
    before += original_size

    img = Image.open(src)
    img = img.convert("RGB")

    if img.width > target_w:
        target_h = round(img.height * target_w / img.width)
        img = img.resize((target_w, target_h), Image.LANCZOS)

    img.save(src, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

    webp = os.path.join("images", stem + ".webp")
    img.save(webp, "WEBP", quality=webp_quality, method=6)

    jpg_size = os.path.getsize(src)
    webp_size = os.path.getsize(webp)
    after += webp_size

    print(
        f"{stem:<34}{original_size//1024:>7}KB{jpg_size//1024:>7}KB"
        f"{webp_size//1024:>7}KB  {img.width}x{img.height}"
    )

print("-" * 74)
print(f"photos, modern browsers: {before//1024} KB -> {after//1024} KB "
      f"({100 - after * 100 // before}% smaller)")
