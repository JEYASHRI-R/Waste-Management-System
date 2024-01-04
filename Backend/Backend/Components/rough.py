import sys
sys.path.append('..')
from Resource.imports import *
from Resource.config import *

df = pd.read_csv(COLLECTION_STATUS)
json_data = df.to_json(orient='records')  # Convert DataFrame to JSON
print(json_data)