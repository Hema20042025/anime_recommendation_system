import gzip
import pickle

# Test decompress and load the .gz file
try:
    with gzip.open('similarity.pkl.gz', 'rb') as f:
        similarity_data = pickle.load(f)
    print("File loaded successfully!")
except Exception as e:
    print(f"Error loading the compressed file: {e}")

