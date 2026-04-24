import os

base_dir = "/storage/emulated/0/Lesson/nigeria-dashboard"
templates_dir = os.path.join(base_dir, "templates")

# Create templates folder if it doesn't exist
os.makedirs(templates_dir, exist_ok=True)

print("Templates folder created at:", templates_dir)
print("Exists now:", os.path.exists(templates_dir))