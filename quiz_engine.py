import random
import os

class QuizEngine:
    def __init__(self, questions):
        self.questions = questions
        random.shuffle(self.questions)
        self.score = 0

    def start_quiz(self):
        total_q = len(self.questions)
        current_idx = 0

        while current_idx < total_q:
            # Get the next 10 questions
            batch = self.questions[current_idx : current_idx + 10]
            
            for i, q in enumerate(batch):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Subject: {q.get('subject', 'General')}")
                print(f"Score: {self.score}/{current_idx + i}")
                print("-" * 30)
                print(f"Q{current_idx + i + 1}: {q['question']}")
                
                for opt in q['options']:
                    print(opt)
                
                user_ans = input("\nYour Answer (A/B/C/D): ").strip().upper()

                if user_ans == q['answer']:
                    print("✅ CORRECT!")
                    self.score += 1
                else:
                    print(f"❌ INCORRECT! The correct answer was: {q['answer']}")
                
                input("\nPress Enter for next question...")

            current_idx += 10
            
            # Batch menu
            if current_idx < total_q:
                print(f"\n--- Batch Complete! Current Score: {self.score}/{current_idx} ---")
                print("1. Next 10 Questions")
                print("2. Switch Subject / Back to Menu")
                print("3. Exit Program")
                
                choice = input("Choice: ")
                if choice == '2': break
                if choice == '3': exit()