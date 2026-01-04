import os
import shutil

SOURCE_TRAIN = "../data/train"
SOURCE_TEST  = "../data/test"

DEST_TRAIN = "../data/train_clean"
DEST_VAL   = "../data/val"

NUM_CLASSES = 6
IMG_EXTS = (".png", ".jpg", ".jpeg")

# Create destination folders
for base in [DEST_TRAIN, DEST_VAL]:
    for i in range(NUM_CLASSES):
        os.makedirs(os.path.join(base, str(i)), exist_ok=True)

def organize(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"❌ Source folder not found: {src_dir}")
        return

    for fname in os.listdir(src_dir):
        if not fname.lower().endswith(IMG_EXTS):
            continue

        parts = fname.split("_")
        if len(parts) < 2:
            continue

        label_part = parts[-1]  # e.g. "4L.png"
        label = label_part[0]   # dataset is 0–5

        if label.isdigit():
            src = os.path.join(src_dir, fname)
            dst = os.path.join(dest_dir, label, fname)
            shutil.move(src, dst)

# Run organization
organize(SOURCE_TRAIN, DEST_TRAIN)
organize(SOURCE_TEST, DEST_VAL)

print("✅ Dataset reorganized successfully!")
print("⚠️ Verify train_clean/ and val/ before deleting raw data.")
