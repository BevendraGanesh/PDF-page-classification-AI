import os
import pandas as pd

base_dir = "dataset"

rows = []

for split in ["train", "test", "validation"]:
    split_path = os.path.join(base_dir, split)

    for label in os.listdir(split_path):
        label_path = os.path.join(split_path, label)

        if os.path.isdir(label_path):
            for file in os.listdir(label_path):
                if file.endswith(".txt"):
                    with open(os.path.join(label_path, file), "r", encoding="utf-8") as f:
                        text = f.read()

                    rows.append({
                        "text": text,
                        "label": label
                    })

df = pd.DataFrame(rows)

df.to_csv("dataset/dataset.csv", index=False)

print("dataset.csv created successfully!")
print(df.head())