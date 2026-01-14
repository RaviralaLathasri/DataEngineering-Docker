import sys
import pandas as pd

# Check if day argument is passed
if len(sys.argv) < 2:
    print("Usage: python pipeline.py <day>")
    sys.exit(1)

day = int(sys.argv[1])
print(f"Running pipeline for day {day}")

# Sample data
df = pd.DataFrame({
    "A": [1, 2],
    "B": [3, 4]
})

print(df)

# Save output as parquet
output_file = f"output_day_{day}.parquet"
df.to_parquet(output_file)

print(f"Pipeline completed. File saved as {output_file}")

