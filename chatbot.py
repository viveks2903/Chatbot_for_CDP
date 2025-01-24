from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import os

# Initialize Elasticsearch client
es = Elasticsearch(hosts=["http://localhost:9200"])

# Check Elasticsearch connection
if es.ping():
    print("Elasticsearch is connected")
else:
    print("Elasticsearch connection failed")

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

# Function to search documentation in Elasticsearch
def search_documentation(query, index_name):
    """
    Search the indexed documentation in Elasticsearch.

    :param query: The user's query.
    :param index_name: The name of the index to search in.
    """
    # Define a simple match query to search for relevant documents
    body = {
        "query": {
            "match": {
                "content": query  # Searching in the 'content' field
            }
        }
    }

    # Perform the search
    response = es.search(index=index_name, body=body)
    
    # Check for results and return the top 3 hits
    results = response.get("hits", {}).get("hits", [])
    if results:
        return [result["_source"]["content"] for result in results[:3]]  # Return the top 3 matching results
    else:
        return ["Sorry, I couldn't find relevant documentation."]

# Initialize Flask app
app = Flask(__name__)

# Endpoint to ask questions
@app.route('/ask', methods=['POST'])
def ask():
    # Get user query from request
    user_query = request.json.get("question")
    index_name = "cdp_documentation"  # Index name where documentation is stored

    # Search the documentation for the query
    search_results = search_documentation(user_query, index_name)

    # Return the response as a JSON
    return jsonify({"response": search_results})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
