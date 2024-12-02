import os
from datetime import date, time, datetime
import datetime

total_day = 201 #total days back
commit_frequency = 2 #commit time per day
repo_link = "git@github.com:Audran-wol/Koholo.git"

tl = total_day #time day
ctr = 1

now = datetime.datetime.now()

# Get the current year
current_year = now.year

# Manually set the start and end dates
start_date = datetime.datetime(2024, 11, 29)  # September 1st, 2024
end_date = datetime.datetime(2024, 12, 2)  # November 19th, 2024

# Calculate the total number of days in the desired range
total_days_in_range = (end_date - start_date).days + 1

# Initialize the pointer to start from the end_date
pointer = 0

f = open("commit.txt", "w")
os.system("git config user.name")
os.system("git config user.email")
os.system("git init")

while tl > 0:
    ct = commit_frequency
    while ct > 0:
        f = open("commit.txt", "a+")
        l_date = end_date - datetime.timedelta(days=pointer)
        
        # Check if the date is within the desired range
        if start_date <= l_date <= end_date:
            formatdate = l_date.strftime("%Y-%m-%d")
            f.write(f"commit ke {ctr}: {formatdate}\n")
            os.system("git add .")
            os.system(f"git commit --date=\"{formatdate} 12:15:10\" -m \"commit ke {ctr}\"")
            print(f"commit ke {ctr}: {formatdate}")
            ctr += 1
            ct -= 1
        
        f.close()
        pointer += 1
        
        # Reset pointer if it exceeds the total days in range
        if pointer >= total_days_in_range:
            pointer = 0
            break
    tl -= 1

os.system(f"git remote add origin {repo_link}")
os.system("git branch -M main")
os.system("git push -u origin main -f")