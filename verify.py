import pickle

# Check if the original file is valid
try:
    with open('similarity.pkl', 'rb') as f:
        similarity_data = pickle.load(f)
    print("Original file loaded successfully!")
except Exception as e:
    print(f"Error while loading similarity.pkl: {e}")
