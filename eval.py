from app.rag import rag_pipeline

tests = [
    {
        "question": "What is theft?",
        "expected": "Theft is the dishonest moving of movable property out of a person's possession without consent (Section 303). It includes things severed from the earth [cite: 2141] and excludes acts done in good faith without dishonest intent[cite: 2185, 2186]."
    },
    {
        "question": "What is punishment for murder?",
        "expected": "Punishment for murder (Section 103) is death or imprisonment for life, and a fine[cite: 1042]. For groups of five or more (mob lynching), the penalty is also death or life imprisonment[cite: 1043]."
    },
    {
        "question": "Difference between theft and robbery",
        "expected": "Robbery (Section 309) is an aggravated form of theft[cite: 2243]. Theft becomes robbery if the offender voluntarily causes or attempts to cause death, hurt, or wrongful restraint, or fear of instant death, hurt, or restraint[cite: 2244, 2245]."
    }
]

def is_correct(answer, expected):
    answer = answer.lower()
    expected = expected.lower()

    match_count = 0
    total_keywords = 0

    keywords = expected.split()

    for word in keywords:
        if len(word) > 4:  # ignore small words like "is", "the"
            total_keywords += 1
            if word in answer:
                match_count += 1

    if total_keywords == 0:
        return False

    score = match_count / total_keywords
    return score > 0.4   # threshold 

def evaluate():
    correct = 0

    for test in tests:
        result = rag_pipeline(test["question"])
        answer = result["answer"]

        print("\nQuestion:", test["question"])
        print("Answer:", answer)

        if is_correct(answer, test["expected"]):
            print("Auto: Correct")
            correct += 1
        else:
            print("Auto: Incorrect")

    accuracy = correct / len(tests)
    print(f"\nAccuracy: {accuracy * 100:.2f}%")

if __name__ == "__main__":
    evaluate()