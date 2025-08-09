import os

# Define the base structure
structure = {
    "data": ["raw/.gitkeep", "processed/.gitkeep"],
    "sql": ["create_tables.sql", "load_data.sql"],
    "sql/queries": ["churn_rate_by_segment.sql", "nps_by_age_group.sql"],
    "notebooks": ["01-data-exploration.ipynb", "02-sentiment-analysis.ipynb", "03-nps-analysis.ipynb"],
    "src": ["db_connection.py", "preprocess.py", "sentiment_model.py", "nps_calculator.py"],
    "reports/figures": [".gitkeep"],
    "output/tables": [".gitkeep"],
    "output/logs": [".gitkeep"],
}

# Create folders and empty files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        with open(os.path.join(folder, file), "w") as f:
            pass  # Create an empty file

# Top-level files
with open("requirements.txt", "w") as f:
    f.write("# Add your project dependencies here\n")

with open(".env", "w") as f:
    f.write("# Store sensitive credentials here\n")

with open("README.md", "w") as f:
    f.write("# credit-risk-sentiment-nps\n\n")

with open("LICENSE", "w") as f:
    f.write("MIT License\n")

print("✅ Project structure created successfully.")
