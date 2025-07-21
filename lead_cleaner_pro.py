import pandas as pd
import re

# Load file
df = pd.read_csv("test_leads.csv")

# Drop blanks
clean_df = df.dropna(subset=["Email", "Phone"])

# Remove duplicates
clean_df = clean_df.drop_duplicates()

# Trim spaces
clean_df["Name"] = clean_df["Name"].astype(str).str.strip()
clean_df["Email"] = clean_df["Email"].astype(str).str.strip()
clean_df["Phone"] = clean_df["Phone"].astype(str).str.strip()

# Capitalize names
clean_df["Name"] = clean_df["Name"].str.title()

# ✅ Fix: email validation returns True/False
def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

clean_df = clean_df[clean_df["Email"].apply(is_valid_email)]

# Clean phone numbers
clean_df["Phone"] = clean_df["Phone"].str.replace(r"[^\d]", "", regex=True)

# Save
clean_df.to_csv("cleaned_leads_pro.csv", index=False)

print(f"✅ Done! Cleaned {len(df)} rows → {len(clean_df)} rows saved in cleaned_leads_pro.csv")
