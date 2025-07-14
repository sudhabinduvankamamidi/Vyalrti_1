from questions import arithmetic_questions, logical_questions
from assessment import assess_student

def run_quiz():
    print("Welcome to the Student Ability Checker!")
    name = input("Enter student name: ")
    print("\nArithmetic Ability Test:")
    arithmetic_score = 0
    for q in arithmetic_questions:
        print(q['question'])
        ans = input("Your answer: ")
        if ans.strip() == str(q['answer']):
            arithmetic_score += 1
    print("\nLogical Reasoning Test:")
    logical_score = 0
    for q in logical_questions:
        print(q['question'])
        ans = input("Your answer: ")
        if ans.strip().lower() == str(q['answer']).lower():
            logical_score += 1
    result = assess_student(arithmetic_score, logical_score, len(arithmetic_questions), len(logical_questions))
    print(f"\n{name}'s Progress Report:")
    print(f"Arithmetic: {result['arithmetic']}")
    print(f"Logical Reasoning: {result['logical']}")

if __name__ == "__main__":
    run_quiz()
