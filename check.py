import gzip
import pickle

# Load the compressed file to test
try:
    with gzip.open('updated_similarity.pkl.gz', 'rb') as f:
        similarity_data = pickle.load(f)
    print("Compressed file loaded successfully!")
except Exception as e:
    print(f"Error loading compressed file: {e}")
