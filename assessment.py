def assess_student(reasoning_score, psychometry_score, total_reasoning, total_psychometry):
    def grade(score, total):
        percent = (score / total) * 100
        if percent >= 75:
            return "High"
        elif percent >= 50:
            return "Medium"
        else:
            return "Low"
    return {
        "reasoning": grade(reasoning_score, total_reasoning),
        "psychometry": grade(psychometry_score, total_psychometry)
    }
