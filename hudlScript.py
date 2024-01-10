import csv
import requests
from bs4 import BeautifulSoup
import re

# Jack Huffman
# This code take a CSV of ARMS recruits with no listed highschool information and finds their highschool through their hudl link


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

            if highschool_match:
                highschool_name = highschool_match.group(1).strip()
                return highschool_name
            else:
                return None
        else:
            return None
    else:
        return None

def process_csv(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as input_file, open(output_csv, 'w', newline='', encoding='utf-8') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # Write header to output CSV
        writer.writerow(['First Name', 'Last Name', 'High School'])

        next(reader)  # Skip header row in input CSV

        for row in reader:
            recruit_id, first_name, last_name, hudl_link = row

            # Check if there is a valid Hudl link
            if hudl_link:
                # Extract high school information from the provided Hudl URL
                highschool = get_highschool_from_url(hudl_link)

                # Write to output CSV
                writer.writerow([first_name, last_name, highschool] if highschool else [first_name, last_name, 'No High School Info'])
            else:
                print(f"Skipping recruit {first_name} {last_name} with no Hudl link.")

if __name__ == "__main__":
    input_csv = 'FirstLastHudlExport1-10-24.csv'
    output_csv = 'export.csv'

    process_csv(input_csv, output_csv)



# Recruits with no hudl link or high school
# Zephaniah Sitaietasi 
# Isaac Staley 
# Nyheem Robertson
# Mensah Junior Owusu Philip
# Nysear Smith
# Victor Velasquez
# Josiah Rucks
# Daniel Beckstead
# Tom Breeze
# Jason Arredondo
# Macon Lincoln
# Jayden Davison
# Mansur McClain
# Jack Patock
# Markus Williams
# Joshua Gauthier
# Jerome Curry 
# Michael Anthony
# Jamar MacFadden
# Joshua Gauthier
# Tacori Allen
# Mansur McClain
# Nyheem Robertson
