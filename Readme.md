
# **Botnet Detection Using Machine Learning**

A Python-based project that detects botnet activity in network traffic using machine learning models. This system preprocesses network data, trains a classification model, and evaluates its performance to differentiate between normal and malicious traffic.

---

## **Table of Contents**

- [Features](#features)  
- [Technologies Used](#technologies-used)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Project Structure](#project-structure)  
- [Results](#results)  
- [Contributing](#contributing)  
- [License](#license)  

---

## **Features**

- **Packet Capture**: Capture live network packets using Scapy or Pyshark.  
- **Data Preprocessing**: Clean and prepare raw network traffic data.  
- **Machine Learning**: Train a classification model to detect botnet traffic.  
- **Feature Importance Analysis**: Understand the key features influencing detection.  
- **Real-Time Detection**: Classify live network traffic for botnet activity.  

---

## **Technologies Used**

- **Programming Language**: Python  
- **Libraries**:  
  - Data Processing: `pandas`, `numpy`, `scikit-learn`  
  - Visualization: `matplotlib`, `seaborn`  
  - Packet Analysis: `scapy`, `pyshark`  
  - Machine Learning: `RandomForestClassifier`  

---

## **Dataset**

We used the **CTU-13 dataset**, a well-known dataset for botnet detection research.  
- **Source**: [CTU-13 Dataset](https://mcfp.felk.cvut.cz/publicDatasets/)  
- Alternatively, capture live network packets with Scapy for real-time analysis.  

---

## **Installation**

1. Clone this repository:  
   ```bash
   git clone https://github.com/your-username/botnet-detection.git
   cd botnet-detection
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. If using Scapy or Pyshark, ensure you have the required permissions to sniff packets.  

---

## **Usage**

### **1. Train and Test the Model**  
1. Place your dataset in the project directory.  
2. Run the preprocessing and training script:  
   ```bash
   python train_model.py
   ```

### **2. Real-Time Packet Analysis**  
1. Use Scapy to sniff packets and classify them:  
   ```bash
   python real_time_detection.py
   ```

---

## **Project Structure**

```plaintext
botnet-detection/
│
├── data/
│   └── ctu-13-dataset.csv        # Dataset file
│
├── src/
│   ├── preprocess.py             # Data preprocessing
│   ├── train_model.py            # Model training and testing
│   ├── real_time_detection.py    # Live traffic classification
│   └── utils.py                  # Utility functions
│
├── README.md                     # Project documentation
├── requirements.txt              # Dependencies
└── results/                      # Results and visualizations
```

---

## **Results**

The model achieved an **accuracy of XX%** on the test dataset with the following performance metrics:  

![image](https://github.com/user-attachments/assets/e3cbb35b-2bd9-4cb1-b688-e4a9ae0920f2)

![Figure_1](https://github.com/user-attachments/assets/e0a41b96-5fad-4d32-8e96-29c3c687e407)

![2](https://github.com/user-attachments/assets/441c96c6-7d06-41bb-a501-0a6659b3ed95)




## **Contributing**

Contributions are welcome! To contribute:  
1. Fork this repository.  
2. Create a feature branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m 'Add feature'`).  
4. Push to the branch (`git push origin feature-name`).  
5. Open a Pull Request.  

---

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---
```

You can copy this into a file named `README.md` in your project directory. Let me know if you need any changes or additions!
