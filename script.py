import nltk
from nltk.corpus import wordnet

# Ensure NLTK resources are available
nltk.download("wordnet")

# Load job-related keywords from a file
with open("keywords.txt", "r") as f:
    job_keywords = {line.strip().lower() for line in f}

# Function to suggest synonyms for missing keywords
def suggest_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name().replace("_", " "))
    return synonyms

# Get resume input
resume = input("Paste your resume text:\n").lower()

# Check for missing keywords
missing_keywords = [word for word in job_keywords if word not in resume]

# Calculate match percentage
total_keywords = len(job_keywords)
matched_keywords = total_keywords - len(missing_keywords)
match_percentage = (matched_keywords / total_keywords) * 100

# Display results
if missing_keywords:
    print("\n⚠ Missing Keywords (Add these for better ranking):")
    print(", ".join(missing_keywords))
    
    # Suggest alternatives
    for word in missing_keywords:
        alternatives = suggest_synonyms(word)
        if alternatives:
            print(f"🔹 Suggested alternatives for '{word}': {', '.join(alternatives)}")

print(f"\n🔹 Resume Match Score: {match_percentage:.2f}%")