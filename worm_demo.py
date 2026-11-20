
# ==========================================
# Cyber Security Assignment - Task 4
# Worm Simulation (Local & Limited)
# ==========================================

import random
from pathlib import Path


# ==========================================
# Step 1: Create a test folder
# ==========================================

def create_folder():
    project_folder = Path(__file__).resolve().parent

    if project_folder.name == "test_copies":
        project_folder = project_folder.parent

    folder = project_folder / "test_copies"
    folder.mkdir(exist_ok=True)
    return folder


# ==========================================
# Step 2: Count existing copies
# ==========================================

def count_copies(folder):
    files = list(folder.glob("copy_*.py"))
    count = len(files)
    return count


# ==========================================
# Step 3: Generate a random filename
# ==========================================

def generate_filename(folder):
    random_number = random.randint(1000, 9999)
    filename = f"copy_{random_number}.py"

    while (folder / filename).exists():
        random_number = random.randint(1000, 9999)
        filename = f"copy_{random_number}.py"

    return folder / filename


# ==========================================
# Step 4: Copy file contents
# ==========================================

def copy_file(source, destination):
    with open(source, "rb") as f:
        contents = f.read()

    with open(destination, "xb") as f:
        f.write(contents)


def verify_copy(source, destination):
    with open(source, "rb") as f:
        original_contents = f.read()

    with open(destination, "rb") as f:
        copied_contents = f.read()

    return original_contents == copied_contents


# ==========================================
# Step 5: Run the simulation
# ==========================================

def main():
    simulation_folder = create_folder()
    print(simulation_folder)

    copy_count = count_copies(simulation_folder)

    if copy_count >= 5:
        print("Maximum number of copies reached. Stopping simulation.")
        return

    # Current Python file
    source_file = Path(__file__).resolve()

    destination_file = generate_filename(simulation_folder)

    copy_file(source_file, destination_file)

    verified = verify_copy(source_file, destination_file)

    if verified:
        print("Copy verified successfully.")
    else:
        print("Copy verification failed.")
        return

    print(f"Created new copy: {destination_file.name}")


if __name__ == "__main__":
    main()
