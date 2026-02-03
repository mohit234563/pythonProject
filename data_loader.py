import os
import json
from database_manager import DatabaseManager

def upload_dataset():
    db_manager = DatabaseManager()
    
    # --- ADD THESE TWO LINES ---
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, 'dataset.json')
    # ---------------------------
    
    # Now this will work because json_path is defined!
    with open(json_path, 'r') as file:
        data = json.load(file)
    
    # Clear existing data to avoid duplicates
    db_manager.collection.delete_many({})
    
    # Insert the new dataset
    db_manager.collection.insert_many(data)
    print(f"Successfully uploaded {len(data)} subjects to LabQuizDB!")

if __name__ == "__main__":
    upload_dataset()