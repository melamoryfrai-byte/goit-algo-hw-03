import sys
from pathlib import Path
import shutil

def copy_dir_data(source: Path, dest: Path):
    for f in source.iterdir():
        try:
            if f.is_dir():
                copy_dir_data(f, dest)
            else:
                file_ext = f.suffix[1:] if f.suffix else 'no_extension'
                target_dir = dest / file_ext
                target_dir.mkdir(parents=True, exist_ok=True)
                target_file = target_dir / f.name # Avoid overwriting files
                counter = 1
                while target_file.exists():
                    stem = f.stem
                    suffix = f.suffix
                    target_file = target_dir / f"{stem}_{counter}{suffix}"
                    counter += 1

                shutil.copy2(f, target_file)
                print(f"File {f} copied to {target_file}")
        except (PermissionError, OSError) as e:
            print(f"Error copying {f}: {e}")
            continue



# 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, 
# помилки доступу до файлів або директорій.
def main():
    if len(sys.argv) < 2:
        print("Usage: python '1_task.py' <source_directory> [destination_directory]")
        sys.exit(1)

    source_path = Path(sys.argv[1])
    destination_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source_path.exists():
        print(f"Source directory '{source_path}' does not exist.")
        sys.exit(1)
    if not source_path.is_dir():
        print(f"Source path '{source_path}' is not a directory.")
        sys.exit(1)

    try:
        destination_path.mkdir(parents=True, exist_ok=True)
    except (PermissionError, OSError) as e:
        print(f"Error creating destination directory '{destination_path}': {e}")
        sys.exit(1)

    for item in source_path.iterdir():
        item_path = item.resolve()
        try:
            if item.is_dir():
                copy_dir_data(item_path, destination_path)
            else:
                shutil.copy2(item_path, destination_path)
                print(f"File {item_path} copied to {destination_path}")
        except (PermissionError, OSError) as e:
            print(f"Error processing '{item_path}': {e}")
            continue
if __name__ == "__main__":
    main()
                