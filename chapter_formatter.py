""" This script processes the contents of a file which lists the chapters in a youtube video
The file contains text in the format: 
    <(timestamp)> <chapter title>. 

Our target format is:
    <chapter##>=<timestamp>
    <chapter##><NAME>=<chapter title>
in all caps.

Code steps are:
1. Read line and remove ()
2. Assign timestamp to variable
3. Assign chapter title to variable
4. 1st line: use a counter with the number formatted in ## 
5. 2nd line: use the chapter title
6. Increment counter
"""


def create_chapter(text: str, index: int) -> tuple:
    text = text.translate(str.maketrans({"(": "", ")": ""}))
    timestamp, sep, chapter_title = text.partition(" ")
    chapter_number = format(index, "02d")

    # timestamp = format(timestamp, "0^9s")
    timestamp = str.format("{:0>8s}.000", timestamp)

    line1 = f"CHAPTER{chapter_number}={timestamp}\n"
    line2 = f"CHAPTER{chapter_number}NAME={chapter_title}"

    # print(timestamp, chapter_title)
    # print(line1)
    # print(line2)

    return line1, line2


file_path = "C:\\Users\\iagbarakwe\\Downloads\\chapters.txt"
new_chapters_file_path = "C:\\Users\\iagbarakwe\\Downloads\\processed_chapters.txt"

with open(file=file_path) as fopen, open(file=new_chapters_file_path, mode="w") as fwrite:
    lines = fopen.readlines()

    new_lines = []
    for idx, line in enumerate(lines):
        new_lines.extend(create_chapter(line, idx+1))
    new_lines.append("\n")

    fwrite.writelines(new_lines)
    print("Finished processing chapters")

# else:
#     print("Error processing chapters")
