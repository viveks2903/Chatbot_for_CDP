from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json

# Initialize Elasticsearch client
es = Elasticsearch(hosts=["http://localhost:9200"])

# Function to index documentation into Elasticsearch
def index_documentation(file_path, index_name):
    """
    Index documentation into Elasticsearch.
    
    :param file_path: Path to the documentation file (JSON format).
    :param index_name: The name of the index in Elasticsearch.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)  # Assuming the file is in JSON format
    
    # Create an index (if not already created)
    if not es.indices.exists(index=index_name):
        es.indices.create(index=index_name)
    
    # Prepare documents to be indexed
    actions = []
    for doc in data["documents"]:  # Assuming a list of documents inside the JSON
        action = {
            "_index": index_name,
            "_id": doc["id"],  # Unique identifier for each document
            "_source": {
                "title": doc["title"],
                "content": doc["content"]  # Full text content
            }
        }
        actions.append(action)

    # Bulk index the documents
    bulk(es, actions)
    print(f"Documents indexed into {index_name}")

# Call the function with the correct path to your JSON file

index_documentation("E:/2025/Chatbot/segment_documentation.json", "cdp_documentation")
