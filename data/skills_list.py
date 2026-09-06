"""
Predefined skills keyword list used to detect skills mentioned in a resume.
Grouped by category for easier maintenance. Matching is case-insensitive
and looks for whole-word / phrase matches in the resume text.
"""

SKILLS_LIST = [
    # Programming Languages
    "Python", "Java", "JavaScript", "TypeScript", "C++", "C", "C#", "Go",
    "Rust", "PHP", "Ruby", "Swift", "Kotlin", "R", "SQL",

    # Web Development
    "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Express.js",
    "Django", "Flask", "FastAPI", "Next.js", "Bootstrap", "Tailwind CSS",
    "REST API", "GraphQL",

    # Data & AI/ML
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision",
    "TensorFlow", "PyTorch", "Keras", "Scikit-learn", "Pandas", "NumPy",
    "OpenCV", "Data Analysis", "Data Visualization", "Matplotlib",
    "Power BI", "Tableau",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Redis", "Firebase",
    "Oracle",

    # Cloud & DevOps
    "AWS", "Azure", "Google Cloud", "Docker", "Kubernetes", "CI/CD",
    "Jenkins", "Git", "GitHub", "Linux",

    # Cybersecurity
    "Ethical Hacking", "Penetration Testing", "Kali Linux", "VAPT",
    "Network Security", "Cryptography",

    # Soft/General
    "Project Management", "Agile", "Scrum", "Problem Solving",
    "Communication", "Team Leadership",
]
