import os

PART_A = "We lease trained seagulls to landlords losing the war on pigeons, "
PART_B = "because one territorial gull clears a roof faster and cheaper than netting or poison."
SENTENCE = PART_A + PART_B
assert SENTENCE == "We lease trained seagulls to landlords losing the war on pigeons, because one territorial gull clears a roof faster and cheaper than netting or poison."
assert 1 <= len(SENTENCE) <= 200

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
