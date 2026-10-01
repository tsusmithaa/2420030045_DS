import pandas as pd

import pandas as pd

data = {
    "name": ["Riya", "Kiran", "Sneha", "Arjun", "Meghana",
             "Rahul", "Ananya", "Vikram", "Nisha", "Pranav"],
    "Roll No": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "Section": ["A", "B", "A", "C", "B", "A", "C", "B", "A", "C"],
    "Age": [18, 19, 20, 19, 18, 20, 19, 18, 20, 19],
    "DS": [92, 75, 88, 81, 90, 78, 85, 94, 80, 87],
    "QC": [89, 82, 91, 76, 88, 84, 79, 90, 85, 83],
    "TOC": [95, 80, 87, 84, 92, 81, 86, 93, 82, 89]
}
df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print(df)

read_df = pd.read_csv("students.csv")
print(read_df.head(5))
print(read_df.tail(5))
print(read_df.describe())
print(read_df.shape)