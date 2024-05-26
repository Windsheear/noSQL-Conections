from astrapy import DataAPIClient
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Initialize the client
client = DataAPIClient("AstraCS:WrimbGzbdUlEkUfxvQsUBkLU:9da493f01ec1c0294db81e887293866268bf9c0c0bd7d4f170554861d98c8a07")
db = client.get_database_by_api_endpoint(
  "https://0cc6f5df-ff20-4f30-ba42-47f7065105dd-us-east1.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")
collection_name = "mycollection2"
db.create_collection(collection_name)

print(f"Created collection: {collection_name}")

