import csv
import requests
from bs4 import BeautifulSoup
import re

def get_highschool_from_url(profile_url):
    # Access the player's Hudl profile page
    response = requests.get(profile_url)

    if response.status_code == 200:
        # Parse the profile page to extract high school information
        soup = BeautifulSoup(response.text, 'html.parser')
        meta_tag = soup.find('meta', {'name': 'description'})

        if meta_tag and 'content' in meta_tag.attrs:
            # Use regular expression to extract high school information
            description_content = meta_tag['content']
            highschool_match = re.search(r"More info: (.*?) -", description_content)

            state_abbreviation = description_content[-2:].strip()


            if highschool_match:
                highschool_name = highschool_match.group(1).strip()
                return highschool_name, state_abbreviation
            else:
                return None, None
        else: 
            return None, None
    else:
        return None, None

def process_csv(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as input_file, open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Write header to output CSV
        writer.writerow(['First Name', 'Last Name', 'High School', 'State'])

        next(reader)  # Skip header row in input CSV

        for row in reader:
            recruit_id, first_name, last_name, hudl_link = row

            # Check if there is a valid Hudl link
            if hudl_link:
                # Extract high school information from the provided Hudl URL
                highschool, state = get_highschool_from_url(hudl_link)

                # Write to output CSV
                writer.writerow([first_name, last_name, highschool, state] if highschool else [first_name, last_name, 'No High School Info', state])
            else:
                print(f"Skipping recruit {first_name} {last_name} with no Hudl link.")

if __name__ == "__main__":
    input_csv = 'FirstLastHudlExport1-10-24.csv'
    output_csv = 'export.csv'

    process_csv(input_csv, output_csv)

