from pathlib import Path

# Dataset path relative to this Python file
base = Path(__file__).resolve().parent / "Description and Sample of the DataSet-20261006"

image_dir = base / "VOIs" / "image"
mask_dir = base / "VOIs" / "nodule_mask"

# Verify directories
print("Dataset exists:", base.exists())
print("Image directory exists:", image_dir.exists())
print("Mask directory exists:", mask_dir.exists())

if not image_dir.is_dir() or not mask_dir.is_dir():
    raise FileNotFoundError("Image or mask directory not found. Check dataset structure.")

# Collect filenames
images = {
    p.name for p in image_dir.glob("*.nii.gz")
}

masks = {
    p.name for p in mask_dir.glob("*.nii.gz")
}

print("\nImages:", len(images))
print("Masks:", len(masks))

print("\nMasks without image:")
for name in sorted(masks - images):
    print(name)

print("\nImages without mask:")
for name in sorted(images - masks):
    print(name)