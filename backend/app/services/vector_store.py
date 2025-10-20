
import chromadb
from chromadb.utils import embedding_functions
from app.config import settings

# Path to store the persistent ChromaDB data
CHROMA_DATA_PATH = "chroma_data"
# Name of the collection to store document embeddings
COLLECTION_NAME = "research_documents"

class VectorStoreService:
    def __init__(self):
        # Initialize a persistent ChromaDB client
        self.client = chromadb.PersistentClient(path=CHROMA_DATA_PATH)

        # Use OpenAI's embedding function, configured with the central settings
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=settings.OPENAI_API_KEY,
            model_name="text-embedding-ada-002"
        )

        # Get or create the collection
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function
        )

    def add_document_chunks(self, chunks: list[str], metadatas: list[dict], ids: list[str]):
        """
        Adds document chunks and their metadata to the collection.

        Args:
            chunks (list[str]): The text chunks of the document.
            metadatas (list[dict]): A list of metadata dictionaries, one for each chunk.
            ids (list[str]): A list of unique IDs, one for each chunk.
        """
        if not chunks:
            return

        self.collection.add(
            documents=chunks,
            metadatas=metadatas,
            ids=ids
        )

    def query_collection(self, query_text: str, n_results: int = 5):
        """
        Queries the collection to find the most relevant document chunks.

        Args:
            query_text (str): The user's query.
            n_results (int): The number of results to return.

        Returns:
            A dictionary containing the query results.
        """
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )

# Example of how this service would be used (for demonstration)
if __name__ == '__main__':
    # This block would not be in the final application code
    # It requires OPENAI_API_KEY to be set in the environment

    # Initialize the service
    vector_store = VectorStoreService()

    # Example documents
    docs = [
        "The mitochondria is the powerhouse of the cell.",
        "The capital of Iran is Tehran.",
        "Photosynthesis is the process by which plants convert light into energy."
    ]
    meta = [{'source': 'biology_101'}, {'source': 'geography_faq'}, {'source': 'botany_intro'}]
    doc_ids = ['doc1', 'doc2', 'doc3']

    # Add documents
    vector_store.add_document_chunks(docs, meta, doc_ids)

    # Query for relevant information
    query_results = vector_store.query_collection("what is the main source of energy for a plant?")

    print("Query Results:")
    print(query_results)
