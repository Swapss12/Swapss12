import itertools

# Define components
subjects_1st = ["I"]
subjects_3rd = ["He", "She"]
subjects = subjects_1st + subjects_3rd

verbs = [
    "love", "am loving", "was loving", "have loved", "had loved", "will love",
    "might love", "could love", "should love", "would love", "must love",
    "have been loving", "had been loving", "will be loving", "will have loved",
    "might have loved", "could have loved", "should have loved", "would have loved",
    "must have loved", "will have been loving", "might have been loving",
    "could have been loving", "should have been loving", "would have been loving",
    "must have been loving"
]

modals = ["", "will", "can", "might", "could", "should", "would", "must"]
negative_forms = ["", "not"]
question_forms = ["", "?"]

# Helper function to combine parts into a sentence
def combine_parts(subject, modal, verb, negative, question):
    if modal:
        if negative:
            sentence = f"{subject} {modal} not {verb} flowers"
        else:
            sentence = f"{subject} {modal} {verb} flowers"
    else:
        if negative:
            sentence = f"{subject} do not {verb} flowers" if subject == "I" else f"{subject} does not {verb} flowers"
        else:
            sentence = f"{subject} {verb} flowers"
    
    if question:
        sentence += "?"
    else:
        sentence += "."
    
    return sentence

# Generate sentences
sentences = set()

for subject, verb, modal, negative, question in itertools.product(subjects, verbs, modals, negative_forms, question_forms):
    sentence = combine_parts(subject, modal, verb, negative, question)
    sentences.add(sentence)

# Save to a text file
file_path = "generated_sentences.txt"
with open(file_path, "w") as file:
    for sentence in sentences:
        file.write(sentence + "\n")

print(f"Generated {len(sentences)} unique sentences and saved to {file_path}")


<!---
Swapss12/Swapss12 is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
