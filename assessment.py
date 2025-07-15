def assess_student(arithmetic_score, logical_score, total_arithmetic, total_logical):
    def grade(score, total):
        percent = (score / total) * 100
        if percent >= 75:
            return "High"
        elif percent >= 50:
            return "Medium"
        else:
            return "Low"
    return {
        "arithmetic": grade(arithmetic_score, total_arithmetic),
        "logical": grade(logical_score, total_logical)
    }
