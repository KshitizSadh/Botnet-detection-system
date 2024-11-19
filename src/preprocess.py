import pandas as pd

def load_and_preprocess_data(attack_file, normal_file):
    """
    Load and preprocess two datasets: one for attack traffic and one for normal traffic.

    Steps:
    - Load both datasets as pandas DataFrames.
    - Add a 'Label' column to distinguish attack vs normal traffic.
    - Concatenate the two datasets into one.
    - Drop unnecessary or irrelevant columns.
    - Handle missing values by filling or removing them.
    - Ensure proper formatting for machine learning.

    :param attack_file: Path to the attack traffic CSV file.
    :param normal_file: Path to the normal traffic CSV file.
    :return: Preprocessed pandas DataFrame.
    """
    print(f"Loading datasets:\n - Attack: {attack_file}\n - Normal: {normal_file}")
    try:
        # Load the attack and normal datasets
        attack_data = pd.read_csv(attack_file)
        normal_data = pd.read_csv(normal_file)

        # Add a 'Label' column (1 for attack, 0 for normal)
        attack_data['Label'] = 1
        normal_data['Label'] = 0

        # Concatenate the two datasets
        full_data = pd.concat([attack_data, normal_data], ignore_index=True)
        print("Datasets merged. Combined shape:", full_data.shape)

        # Drop unnecessary columns (update based on your dataset structure)
        columns_to_drop = ['Unnamed: 0', 'Source IP', 'Destination IP', 'Timestamp']
        full_data = full_data.drop(columns=columns_to_drop, errors='ignore')
        print(f"Dropped columns: {columns_to_drop}")

        # Handle missing values (fill with 0 for now)
        full_data = full_data.fillna(0)
        print("Missing values handled by filling with 0.")

        # Convert categorical columns to numeric if needed
        categorical_columns = full_data.select_dtypes(include=['object']).columns
        if not categorical_columns.empty:
            print(f"Converting categorical columns to numeric: {categorical_columns.tolist()}")
            full_data = pd.get_dummies(full_data, columns=categorical_columns, drop_first=True)

        # Display final dataset info
        print("Final Dataset Shape:", full_data.shape)
        print("Preprocessing complete.")
        return full_data
    except Exception as e:
        print(f"Error during preprocessing: {e}")
        raise

# Example test code (can be removed in production)
if __name__ == "__main__":
    # Provide the paths to the attack and normal traffic CSV files
    attack_file = "data/CTU13_Attack_Traffic.csv"
    normal_file = "data/CTU13_Normal_Traffic.csv"

    # Preprocess and save the combined dataset
    processed_data = load_and_preprocess_data(attack_file, normal_file)
    output_path = "Results/Processed_Traffic.csv"
    processed_data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to: {output_path}")
