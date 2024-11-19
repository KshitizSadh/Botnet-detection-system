import joblib

def save_model(model, file_path):
    joblib.dump(model, file_path)
    print(f"Model saved to {file_path}.")

def load_model(file_path):
    model = joblib.load(file_path)
    print(f"Model loaded from {file_path}.")
    return model
