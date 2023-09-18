# Jack Huffman
# Carleton College Football CSV Cross Refrencing Program

import csv

# Object Oriented cross refrencing program. 
# inData: csv file of new UP TO DATE data that we wish to check whether it is recorded in database
# refData: csv file of data kept in our database
# outData: csv file where recruits who are in inData but not in database (refData) are recorded
# def crossReference(inData, refData, outData):
#     # Current implementation could use a set to check for firstname lastname keys
#     # Currently implementated as a dictionary to allow for future development
#     ref_dict = {}

#     # Open reference file ()
#     with open(refData, "r", encoding = "UTF-8") as ref_file:
#         reference_reader = csv.reader(ref_file)
#         next(reference_reader)
#         for row in reference_reader:
#             # Format irregularity between files accounted for here
#             row = [col.replace('"','') for col in row]
#             newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
#             ref_dict[newAthlete.first_last] = newAthlete

#     with open(inData, "r", encoding = "UTF-8") as new_file, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
#         input_reader = csv.reader(new_file)
#         output_writer = csv.writer(output_file)
    
#         # write the header row
#         # output_writer.writerow(["Last", "First", "High School", "State", "Grad Year", "Pos.", "GPA", "Email", "Mobile Number", "Hudl Film", "Parent/Guardian 1 Name", "Parent/Guardian 1 Email", "Parent/Guardian 1 Phone", "Twitter Handle", "Home Address", "City", "State", "Zip"])
#         output_writer.writerow(["First", "Last", "Date Of Birth", "Pos.", "Height", "Weight", "Mobile Number", "Email", "Twitter Handle", "Home Address", "City", "State", "Zip", "GPA", "High School", "Grad Year", "Hudl Film", "HC First", "HC Last", "HC Phone", "HC Email", "Jersey#"])
#         next(input_reader)
#         # iterate through the new data
#         for row in input_reader:
#             check_first_last = row[0] + ' ' + row[1]

#             if check_first_last not in ref_dict:
#                 output_writer.writerow(row)


# THIS IS THE CODE I USED FOR NICK TOOLE
# def crossReferenceToole(inData, refData, outData):
#     # Current implementation could use a set to check for firstname lastname keys
#     # Currently implementated as a dictionary to allow for future development
#     ref_dict = {}

#     # Open reference file ()
#     with open(refData, "r", encoding = "UTF-8") as ref_file:
#         reference_reader = csv.reader(ref_file)
#         next(reference_reader)
#         for row in reference_reader:
#             # Format irregularity between files accounted for here
#             row = [col.replace('"','') for col in row]
#             newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[9], row[11], row[0], row[0])
#             ref_dict[newAthlete.first_last] = newAthlete

#     with open(inData, "r", encoding = "UTF-8") as new_file, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
#         input_reader = csv.reader(new_file)
#         output_writer = csv.writer(output_file)
    
#         # write the header row
#         # output_writer.writerow(["Last", "First", "High School", "State", "Grad Year", "Pos.", "GPA", "Email", "Mobile Number", "Hudl Film", "Parent/Guardian 1 Name", "Parent/Guardian 1 Email", "Parent/Guardian 1 Phone", "Twitter Handle", "Home Address", "City", "State", "Zip"])
#         # output_writer.writerow(["First", "Last", "Date Of Birth", "Pos.", "Height", "Weight", "Mobile Number", "Email", "Twitter Handle", "Home Address", "City", "State", "Zip", "GPA", "High School", "Grad Year", "Hudl Film", "HC First", "HC Last", "HC Phone", "HC Email", "Jersey#"])
#         output_writer.writerow(["First Name","Last Name","Event Name","Participation Date/Session","Cell Phone","Participant E-mail","DOB","Age","Grade as of Fall 2023","School","HS Grad Yr","Primary Position","Secondary Position","Twitter Handle", "In ARMS","Coach Priority Level"])
#         next(input_reader)
#         next(input_reader)
#         # iterate through the new data
#         for row in input_reader:
#             check_first_last = row[0] + ' ' + row[1]
            
#             if check_first_last in ref_dict:
#                 curAthlete = ref_dict[check_first_last]
#                 curAthletePriority = curAthlete.get_state()
#                 output_writer.writerow(row + ["Yes", curAthletePriority])
#             if check_first_last not in ref_dict:
#                 output_writer.writerow(row + ["No", "None"])


# # Cross reference two inData files with frontrush data
# def crossReference(inData, inDataTwo, refData, outData):
#     # Current implementation could use a set to check for firstname lastname keys
#     # Currently implementated as a dictionary to allow for future development
#     ref_dict = {}

#     # Open reference file ()
#     with open(refData, "r", encoding = "UTF-8") as ref_file:
#         reference_reader = csv.reader(ref_file)
#         next(reference_reader)
#         for row in reference_reader:
#             # Format irregularity between files accounted for here
#             row = [col.replace('"','') for col in row]
#             newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
#             ref_dict[newAthlete.first_last] = newAthlete

#     with open(inData, "r", encoding = "UTF-8") as new_file, open(inDataTwo, "r", encoding = "UTF-8") as new_file_two, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
#         input_reader = csv.reader(new_file)
#         input_reader_two = csv.reader(new_file_two)
#         output_writer = csv.writer(output_file)
    
#         # write the header row
#         output_writer.writerow(["Last", "First", "Pos.", "Email", "Height", "Weight", "GPA", "Grad Year", "High School", "State", "Twitter", "Phone", "Camp", "Film Link"])
#         next(input_reader)
#         next(input_reader_two)
#         # iterate through the new data
#         for row in input_reader:
#             check_first_last = row[0] + ' ' + row[1]
#             if check_first_last not in ref_dict:
#                 output_writer.writerow(row)
#         for row in input_reader_two:
#             check_first_last = row[0] + ' ' + row[1]
#             if check_first_last not in ref_dict:
#                 output_writer.writerow(row)

# Object Oriented cross refrencing program. 
# inData: csv file of new UP TO DATE data that we wish to check whether it is recorded in database
# refData: csv file of data kept in our database
# outData: csv file where recruits who are in inData but not in database (refData) are recorded
#THIS ONE IS USED WHEN THE INDATA HAS FIRST AND LAST NAME COMBINED INTO ONE FIELD
def crossReference2(inData, refData, outData):
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
            # Last, First, Last First, School, Email
            newAthlete = Athlete(row[1], row[0], row[0] + ' ' + row[1], row[0], row[0])
            ref_dict[newAthlete.first_last] = newAthlete

    with open(inData, "r", encoding = "UTF-8") as new_file, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        output_writer = csv.writer(output_file)
    
        # write the header row
        # output_writer.writerow(["Last", "First", "High School", "State", "Grad Year", "Pos.", "GPA", "Email", "Mobile Number", "Hudl Film", "Parent/Guardian 1 Name", "Parent/Guardian 1 Email", "Parent/Guardian 1 Phone", "Twitter Handle", "Home Address", "City", "State", "Zip"])
        output_writer.writerow(["Last","First","Twitter Handle","Twitter DM Status","Coach Priority Level for Admissions","GPA","Date Of Birth","Pos.","Height","Weight","Mobile Number","Email","Home Address","City","State","Zip","High School","Grad Year","Hudl Film","HC First","HC Last","HC Phone","HC Email","Jersey#","Source"])
        next(input_reader)
        # iterate through the new data
        for row in input_reader:
            check_first_last = row[1] + ' ' + row[0]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)

def delete_duplicates(inData, inDataTwo, outData):
    ref_dict = {}

    with open(inData, "r", encoding = "UTF-8") as new_file, open(inDataTwo, "r", encoding = "UTF-8") as new_file_two, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        input_reader_two = csv.reader(new_file_two)
        output_writer = csv.writer(output_file)
    
        # write the header row
        output_writer.writerow(["Last", "First", "Pos.", "Email", "Height", "Weight", "GPA", "Grad Year", "High School", "State", "Twitter", "Phone", "Camp", "Film Link"])
        next(input_reader)
        next(input_reader_two)

        for row in input_reader:
            check_first_last = row[0] + ' ' + row[1]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)
                newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
                ref_dict[newAthlete.first_last] = newAthlete
        for row in input_reader_two:
            check_first_last = row[0] + ' ' + row[1]
            if check_first_last not in ref_dict:
                output_writer.writerow(row)
                newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[2], row[11])
                ref_dict[newAthlete.first_last] = newAthlete

# Takes input from Full_Recruit_Export on ARMS
def check_duplicates(inData, outData):
    ref_dict = {}

    with open(inData, "r", encoding = "UTF-8") as new_file, open(outData, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        output_writer = csv.writer(output_file)
    
        # write the header row
        output_writer.writerow(["First", "Last", "Recruiting Coach", "State"])
        next(input_reader)

        for row in input_reader:
            check_first_last = row[1] + ' ' + row[3]
            first = row[1]
            last = row[3]
            coach = row[58]
            state = row[30]
            newAthlete = Athlete(first, last, check_first_last, state, coach, None, None)
            if check_first_last not in ref_dict:
                ref_dict[check_first_last] = newAthlete
            else:
                refAthlete = ref_dict[check_first_last]
                if state == '' or coach == '':
                    output_writer.writerow([first, last, coach, state])
                if state == refAthlete.get_state() and coach == refAthlete.get_coach():
                    output_writer.writerow([first, last, coach, state])



# Athlete Class, currently not necessary but created to allow for further 
# building and cross refrencing of multiple fields across datasets
class Athlete:
    def __init__(self,last_name,first_name,first_last,state,coach,school,email):
        self.last_name = last_name
        self.first_name = first_name
        self.first_last = first_last
        self.state = state
        self.coach = coach
        self.school = school
        self.email = email

    def get_last_name(self):
        return self.last_name

    def get_first_name(self):
        return self.first_name
        
    def get_first_last(self):
        return self.first_last

    def get_state(self):
        return self.state
    
    def get_coach(self):
        return self.coach
    
    def get_school(self):
        return self.school

    def get_email(self):
        return self.email
    

# THIS IS THE CODE I USED FOR NICK TOOLE 2nd time 6-8-2023
def crossReferenceToole(arms_data, verified_data, camp_data, out_data):
    # Current implementation could use a set to check for firstname lastname keys
    # Currently implementated as a dictionary to allow for future development
    ARMS_dict = {}
    verified_dict = {}

    # Open reference file ()
    with open(arms_data, "r", encoding = "UTF-8") as ref_file:
        reference_reader = csv.reader(ref_file)
        next(reference_reader)
        for row in reference_reader:
            # Format irregularity between files accounted for here
            row = [col.replace('"','') for col in row]
            newAthlete = Athlete(row[0], row[1], row[0] + ' ' + row[1], row[4], row[5], row[6], row[6])
            ARMS_dict[newAthlete.first_last] = newAthlete


    #13 is gpa

    with open(verified_data, "r", encoding = "UTF-8") as ref2_file:
        reference_reader2 = csv.reader(ref2_file)
        next(reference_reader2)
        for row in reference_reader2:
            # Format irregularity between files accounted for here
            row = [col.replace('"','') for col in row]
            newAthlete = Athlete(row[5], row[3], row[1], row[13], row[3], row[3], row[3])
            verified_dict[newAthlete.first_last] = newAthlete

    with open(camp_data, "r", encoding = "UTF-8") as new_file, open(out_data, "w", encoding = "UTF-8", newline="") as output_file:
        input_reader = csv.reader(new_file)
        output_writer = csv.writer(output_file)
    
        # write the header row
        output_writer.writerow(["Year", "Position", "Name", "High School", "State", "Height", "Weight","GPA","Mobile Phone","Twitter"])
        next(input_reader)
        # iterate through the new data
        for row in input_reader:
            last_first = row[2]  # Combined name in the third column
            last_name, first_name = last_first.split(", ")  # Split and rearrange the name
            
            check_first_last = first_name + " " + last_name
            
            if check_first_last in ARMS_dict:
                curAthlete = ARMS_dict[check_first_last]
                form = curAthlete.state
                vv2 = curAthlete.coach
                attendVV = curAthlete.school
                if check_first_last in verified_dict:
                    verAthlete = verified_dict[check_first_last]
                    gpa = verAthlete.state
                    output_writer.writerow(row + ["Yes",form,vv2,attendVV,"Yes",gpa])
                if check_first_last not in verified_dict:
                    output_writer.writerow(row + ["Yes",form,vv2,attendVV,"No",""])
            if check_first_last not in ARMS_dict:
                if check_first_last in verified_dict:
                    verAthlete = verified_dict[check_first_last]
                    gpa = verAthlete.state
                    output_writer.writerow(row + ["No","","","","Yes",gpa])
                if check_first_last not in verified_dict:
                    output_writer.writerow(row + ["No","","","","No",""])
    

def main():
    # arms_data = "./VV-Info-6-27-2023-Correct.csv"
    # verified_data = "./Verified-Toole.csv"
    # camp_data = "ColumbiaCampCombined-Toole-7-6-2023.csv"
    # camp_data2 = "Toole-Chicago-AM.csv"
    # camp_data3 = "Toole-Chicago-PM.csv"
    # out_data = "ColumbiaCampCombined-Updated-Toole-7-6-2023.csv"
    # out_data2 = "Toole-Chicago-AM-UPDATED.csv"
    # out_data3 = "Toole-Chicago-PM-UPDATED.csv"
    # crossReferenceToole(arms_data, verified_data, camp_data, out_data)
    
    # crossReferenceToole(arms_data, verified_data, camp_data2, out_data2)
    
    # crossReferenceToole(arms_data, verified_data, camp_data3, out_data3)
    armsData = "./allData/FullRecruitExport9-18-2023.csv"
    duplicates = "duplicates9-18-2023.csv"
    check_duplicates(armsData, duplicates)



if __name__ == "__main__":
    main()