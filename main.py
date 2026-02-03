from database_manager import DatabaseManager
from quiz_engine import QuizEngine

def main():
    db = DatabaseManager()
    
    while True:
        print("\n===  MCQ MANAGEMENT SYSTEM ===")
        subjects = db.get_all_subjects()
        
        if not subjects:
            print("No subjects found in Atlas. Please run data_loader.py first.")
            break

        for i, sub in enumerate(subjects):
            print(f"{i+1}. {sub}")
        print(f"{len(subjects)+1}. Exit")

        try:
            choice = int(input("\nSelect Subject: "))
            if choice == len(subjects) + 1:
                break
            
            selected_sub = subjects[choice - 1]
            data = db.get_subject_data(selected_sub)
            
            # Start the quiz
            engine = QuizEngine(data['questions'])
            engine.start_quiz()
            
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid number.")

if __name__ == "__main__":
    main()