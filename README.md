
# CDP Documentation Chatbot

This project involves building a chatbot that can answer "how-to" questions related to four Customer Data Platforms (CDPs): Segment, mParticle, Lytics, and Zeotap. The chatbot retrieves relevant information from official documentation for each CDP and provides answers to user queries. The project uses **Elasticsearch** for indexing and searching documentation.

## Project Overview

- **Index Documentation**: This part of the project is responsible for indexing documentation for different CDPs into Elasticsearch.
- **Chatbot**: A chatbot will retrieve the indexed documentation and answer how-to questions related to the CDPs.

## Requirements

Before running the project, make sure you have the following installed:

1. **Python 3.x**: Install the latest version of Python from the official website: [Python Downloads](https://www.python.org/downloads/)
2. **Elasticsearch**: Ensure that Elasticsearch is installed and running. You can download it from the official website: [Elasticsearch Downloads](https://www.elastic.co/downloads/elasticsearch)
3. **Python Libraries**: Install the required Python libraries by running the following command:

    ```bash
    pip install elasticsearch
    ```

4. **Elasticsearch Service**: If you're using Elasticsearch as a service on Windows, ensure that the service is running.

## Getting Started

### 1. **Run Elasticsearch**

Ensure that Elasticsearch is up and running on your local machine. If you're using Docker or a local installation, Elasticsearch should be available at `http://localhost:9200`.

To start Elasticsearch:
- **If running as a service on Windows**: Open **Command Prompt** as an administrator and start the service.
- **If running manually**: Navigate to the `bin` directory of your Elasticsearch installation and run `elasticsearch.bat`.

### 2. **Index Documentation into Elasticsearch**

Before using the chatbot, the documentation needs to be indexed into Elasticsearch. The code will read a JSON file containing the documentation and index it into an Elasticsearch index.

#### Prepare Documentation JSON File

Ensure you have the JSON file containing the documentation, such as `segment_documentation.json`. The JSON file should have a structure like:

```json
{
    "documents": [
        {
            "id": "1",
            "title": "How to Set Up a New Source in Segment",
            "content": "Step 1: Go to the Segment dashboard..."
        },
        ...
    ]
}
```

#### Index the Documentation

Run the Python script to index the documentation into Elasticsearch:

```bash
python app.py
```

This will read the documentation JSON file (e.g., `segment_documentation.json`) and index it into Elasticsearch under the `cdp_documentation` index.

### 3. **Using the Chatbot**

Once the documentation is indexed, you can use the chatbot to answer "how-to" questions. The chatbot queries Elasticsearch to find relevant information from the indexed documentation.

The chatbot can answer questions such as:

- "How do I set up a new source in Segment?"
- "How can I create a user profile in mParticle?"
- "How do I build an audience segment in Lytics?"

### 4. **Customizing the Code**

You can modify the code to handle different CDPs by:

- Changing the documentation JSON files for other CDPs (e.g., `mparticle_documentation.json`, `lytics_documentation.json`).
- Adjusting the indexing and search logic as needed for other platforms.

### 5. **Error Handling**

If you encounter a connection error, ensure that Elasticsearch is running on the specified port (`9200`) and is accessible from your script. If you're using a different host or port for Elasticsearch, update the connection details in the Python code.

## Troubleshooting

- **Elasticsearch is not running**: Make sure the Elasticsearch service is up and running.
- **Connection issues**: Check if Elasticsearch is running on the correct port (`9200`) and is accessible.
- **Indexing issues**: If the index already exists, Elasticsearch may not allow overwriting. You can delete the existing index or create a new one.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Sections in the `README.md`:

1. **Project Overview**: Provides a general description of the project and its core functionality.
2. **Requirements**: Lists all the software and dependencies required to run the project.
3. **Getting Started**: Detailed instructions on how to set up Elasticsearch, index the documentation, and use the chatbot.
4. **Customizing the Code**: Instructions for modifying the code to support other CDPs.
5. **Troubleshooting**: Helps users debug common issues related to Elasticsearch or the Python script.
6. **License**: Information on the project's license (you can adjust based on your preference).

