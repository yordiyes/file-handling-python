# File Read & Write Challenge with Error Handling

try:
    # Ask user for input file
    filename = input("Enter the filename to read: ")

    # Open and read the file
    with open(filename, 'r') as file:
        content = file.read()

    # Modify content (example: make uppercase)
    modified_content = content.upper()

    # Write to a new file
    new_filename = "modified_" + filename
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to {new_filename}")

except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")
except IOError:
    print("Error: The file cannot be read or written.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
