# archive.py
# Script to archive Cosmos DB records older than 3 months to Blob Storage
import datetime
import azure.cosmos.cosmos_client as cosmos_client
from azure.storage.blob import BlobServiceClient

# Initialize clients (pseudo)
cosmos = cosmos_client.CosmosClient(...)
blob_service = BlobServiceClient.from_connection_string("...")

def archive_old_records():
    now = datetime.datetime.utcnow()
    cutoff = now - datetime.timedelta(days=90)
    old_records = cosmos.query_items("SELECT * FROM c WHERE c.date < @cutoff", parameters=[{"name":"@cutoff", "value": cutoff.isoformat()}])
    for record in old_records:
        blob_client = blob_service.get_blob_client(container="archived-records", blob=record['id'] + ".json")
        blob_client.upload_blob(str(record), overwrite=True)
        record['archived'] = True
        record['blob_url'] = blob_client.url
        cosmos.upsert_item(record)

if __name__ == "__main__":
    archive_old_records()