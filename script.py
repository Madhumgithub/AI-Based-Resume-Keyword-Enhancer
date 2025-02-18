
### **🐍 script.py**
```python
job_keywords = {"Python", "Machine Learning", "Data Structures", "SQL", "Flask", "TensorFlow", "NLP"}

resume = input("Paste your resume text:\n").lower()
missing_keywords = [word for word in job_keywords if word.lower() not in resume]

if missing_keywords:
    print("\n⚠️ Missing Keywords (Add these for better ranking):")
    print(", ".join(missing_keywords))
else:
    print("\n✅ Your resume is optimized for ATS!")
