import pandas as pd

url = "https://data.cityofnewyork.us/api/views/3h2n-5cm9/rows.csv?accessType=DOWNLOAD"

print("Loading data... hang tight...")
data_violations = pd.read_csv(url, nrows=1000)

# Show the first 5 rows
print(data_violations.head())