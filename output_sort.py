# sort_strings_by_length.py

def sort_file(input_path: str, output_path: str = "data/output_sorted.txt"):
    # Read all lines (strip newline characters)
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    # Sort by length (shortest first), keeping stable order for equal lengths
    sorted_lines = sorted(lines, key=len)

    # Write result
    with open(output_path, "w", encoding="utf-8") as f:
        for line in sorted_lines:
            f.write(line + "\n")


sort_file("data/output.txt")
