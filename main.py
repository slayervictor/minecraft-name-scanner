import time
from scraper import IsUsernameTaken

data_path = "data/words.txt"
output_path = "data/output.txt"
savedata_path = "data/savedata.txt"

# start from the saved line
try:
    with open(savedata_path, "r", encoding="utf-8") as f:
        start_line = int(f.read().strip())
except (FileNotFoundError, ValueError):
    start_line = 0 

# main func
with open(data_path, "r", encoding="utf-8") as infile, \
     open(output_path, "a", encoding="utf-8") as outfile:

    for _ in range(start_line):
        next(infile, None)

    current_line = start_line

    for word in infile:
        if current_line > 21000:
            print("Reached line limit — stopping.")
            break
        word = word.strip()
        if not word:
            current_line += 1
            continue

        taken = IsUsernameTaken(word)

        if not taken:
            outfile.write(word + "\n")
            outfile.flush()

            print(f"{word}: {taken}")

        with open(savedata_path, "w", encoding="utf-8") as s:
            s.write(str(current_line))

        current_line += 1
