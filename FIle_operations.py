import os

# Name of the folder where all notes will be stored
NOTES_DIR = "notes"

# Check if the folder already exists
# If NOT, create it. If YES, do nothing.
if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)              # Create a new directory
    print(f"Created folder: {NOTES_DIR}")
else:
    print(f"Using existing folder: {NOTES_DIR}")

# Show where we are currently working inside Colab
print("Working directory:", os.getcwd())



def write_new_note(filename, text):
    """
    Creates a new note file (or overwrites an existing one).
    - filename: name of the file (e.g. 'day1.txt')
    - text: the first line to write into the file
    """

    # Create the complete path to the file (folder + filename)
    path = os.path.join(NOTES_DIR, filename)

    # Open the file in WRITE mode ('w')
    # - If file doesn't exist → creates new file
    # - If file exists → deletes old content and writes new
    with open(path, "w") as f:
        f.write(text + "\n")            # Write the line to the file

    print("New note saved to", path)


# Try it
write_new_note("example.txt", "This is my first note!")
