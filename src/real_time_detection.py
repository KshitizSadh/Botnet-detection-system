import sys
import numpy as np
import joblib
import scapy.all as scapy
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Add the src folder to the system path
sys.path.append("c:/Users/sadhs/Desktop/botnet detection system/src")

# Load the pre-trained RandomForest model and scaler
model = joblib.load('Results/random_forest_model.pkl')
scaler = joblib.load('Results/scaler.pkl')  # Assuming scaler was saved during training

def extract_features_from_packet(packet):
    """
    Extracts the features from a packet.
    You need to implement the same feature extraction logic that was used during training.
    """
    # Example features (adjust based on your actual feature extraction process)
    packet_length = packet.length
    packet_time = packet.time
    ip_src = packet[scapy.IP].src
    ip_dst = packet[scapy.IP].dst

    # Additional feature extraction logic should be added here as per your dataset
    # Example: Protocol type, packet size, etc.
    features = [packet_length, packet_time, ip_src, ip_dst]  # Add more features as required
    return features

def detect_botnet(packet):
    """
    Detects potential botnet activity from a packet using the trained RandomForest model.
    """
    # Extract features from the packet
    features = extract_features_from_packet(packet)

    # Ensure that the feature vector has the same shape as expected by the model
    if len(features) != 57:  # Replace with the number of features used during training
        print(f"Invalid feature vector length: {len(features)}. Expected 57 features.")
        return

    # Preprocess the features (apply the same scaling as used during training)
    scaled_features = scaler.transform([features])

    # Make a prediction using the pre-trained model
    prediction = model.predict(scaled_features)

    # Check the prediction (assuming '1' indicates botnet activity)
    if prediction == 1:
        print(f"Potential Botnet detected: {packet.summary()}")
    else:
        print(f"Normal traffic detected: {packet.summary()}")

# Start sniffing packets for real-time detection
print("Starting real-time detection...")

# Use Scapy's sniff function to capture packets and apply the detection function
scapy.sniff(filter="ip", prn=detect_botnet, count=10)
