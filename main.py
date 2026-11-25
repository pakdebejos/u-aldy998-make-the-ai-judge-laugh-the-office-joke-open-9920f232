"""The Printer Got Promoted: an entry for the make.fun bounty "Make the AI Judge Laugh: the Office Joke Open".

The program writes the entry text - one line, 153 characters -
to entry.txt (153 characters, inside the 1-200 gate) in the output directory (MAKEFUN_OUTPUT_DIR locally, /output
in the grader). The text is a fixed constant with no trailing newline, so
both of the grader's runs write byte-identical output.
"""
import os

LINE = "Our office printer finally got a promotion, because it was the only one here who could actually produce a paper trail without asking for a meeting first."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
