def modify_content(text):
    # Example: Convert to uppercase and add line numbers
    lines = text.splitlines()
    modified_lines = [f"{idx + 1}: {line.upper()}" for idx, line in enumerate(lines)]
    return "\n".join(modified_lines)

def main():
    filename = input("Enter the filename to read (e.g., input.txt): ")

    try:
        with open(filename, "r") as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as outfile:
            outfile.write(modified)

        print(f"\n✅ Success! Modified content written to: {new_filename}")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"\n❌ Error: Could not read the file '{filename}'.")

if __name__ == "__main__":
    main()
    