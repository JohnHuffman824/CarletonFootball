# Jack Huffman
# Carleton College Football CSV Cross Refrencing Program

import csv

# Object Oriented cross refrencing program. 
# inData: csv file of new UP TO DATE data that we wish to check whether it is recorded in database
# refData: csv file of data kept in our database
# outData: csv file where recruits who are in inData but not in database (refData) are recorded
def crossReference(inData, refData, outData):
    # Current implementation could use a set to check for firstname lastname keys
    # Currently implementated as a dictionary to allow for future development
    ref_dict = {}

    # Open reference file ()
    with open(refData, "r", encoding = "UTF-8") as ref_file:
        reference_reader = csv.reader(ref_file)
        next(reference_reader)
        for row in reference_reader:
            # Format irregularity between files accounted for here
            row = [col.replace('"','') for col in row]
            newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
            ref_dict[newAthlete.first_last] = newAthlete

    with open(inData, "r", encoding = "UTF-8") as new_file, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        output_writer = csv.writer(output_file)
    
        # write the header row
        output_writer.writerow(["Last", "First", "High School", "State", "Grad Year", "Pos.", "GPA", "Email", "Mobile Number", "Hudl Film", "Parent/Guardian 1 Name", "Parent/Guardian 1 Email", "Parent/Guardian 1 Phone", "Twitter Handle", "Home Address", "City", "State", "Zip"])
        next(input_reader)
        # iterate through the new data
        for row in input_reader:
            check_first_last = row[0] + ' ' + row[1]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)

# Cross reference two inData files with frontrush data
def crossReference(inData, inDataTwo, refData, outData):
    # Current implementation could use a set to check for firstname lastname keys
    # Currently implementated as a dictionary to allow for future development
    ref_dict = {}

    # Open reference file ()
    with open(refData, "r", encoding = "UTF-8") as ref_file:
        reference_reader = csv.reader(ref_file)
        next(reference_reader)
        for row in reference_reader:
            # Format irregularity between files accounted for here
            row = [col.replace('"','') for col in row]
            newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
            ref_dict[newAthlete.first_last] = newAthlete

    with open(inData, "r", encoding = "UTF-8") as new_file, open(inDataTwo, "r", encoding = "UTF-8") as new_file_two, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        input_reader_two = csv.reader(new_file_two)
        output_writer = csv.writer(output_file)
    
        # write the header row
        output_writer.writerow(["Last", "First", "Pos.", "Email", "Height", "Weight", "GPA", "Grad Year", "High School", "State", "Twitter", "Phone", "Camp", "Film Link"])
        next(input_reader)
        next(input_reader_two)
        # iterate through the new data
        for row in input_reader:
            check_first_last = row[0] + ' ' + row[1]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)
        for row in input_reader_two:
            check_first_last = row[0] + ' ' + row[1]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)

# Athlete Class, currently not necessary but created to allow for further 
# building and cross refrencing of multiple fields across datasets
class Athlete:
    def __init__(self,last_name,first_name,first_last,school,email):
        self.last_name = last_name
        self.first_name = first_name
        self.first_last = first_last
        self.school = school
        self.email = email

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name
        
    def get_first_last(self):
        return self.first_last

    def get_school(self):
        return self.school

    def get_email(self):
        return self.email



def main():
    # Can be altered to take in files via command line
    refData = "./FrontrushRecruits1.csv"
    newData = "./2-15inData.csv"
    newData2 = "./2-15inData2.csv"
    outData = "./2-15outData.csv"

    crossReference(newData, newData2, refData, outData)

if __name__ == "__main__":
    main()