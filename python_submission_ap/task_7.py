# Python Submission - Task 7
# Andrew Piggot
# 1/12/2024

# Function to read the and store the data from names.txt, mark1.txt and mark2.txt
# Summary of the open and read functions:
# "with open" simply opens the file in read mode ("r") and makes sure the file is closed after the block is executed.
# "X.readlines()" reads all lines within a file and stores them as a list of strings.
def read_data():
    with open( "names.txt", "r" ) as names_file:
        names = names_file.readlines() # Read all lines from names file.
 
    with open( "mark1.txt", "r" ) as marks_1: # Read all coursework marks from file.
        marks1 = marks_1.readlines()
 
    with open( "mark2.txt", "r" ) as marks_2: # read all prelim marks from file.
        marks2 = marks_2.readlines()
 
    # Clean up any extra spaces or newline characters.
    names = [name.strip() for name in names]
    marks1 = [int( mark.strip() ) for mark in marks1]
    marks2 = [int( mark.strip() ) for mark in marks2]
 
    return names, marks1, marks2 # Return the cleaned up data.
 
# Function to calculate the percentage.
def calc_percent( course_mark, prelim_mark ):
    total_mark = course_mark + prelim_mark # Add course and prelim marks together for total mark.
    percent = ( total_mark * 100 ) / 150 # Calculate percentage by multiplying total mark by 100 and dividing by highest possible mark.
    return percent # Return the percentage.
 
# Function to get the grade based on percentage.
def get_grade( percent ):
    if percent >= 70:
        return"A" # Grade A if greater than or equal to 70.
    elif 60 <= percent < 70:
        return "B" # Grade B if between 60 and 70.
    elif 50 <= percent < 60:
        return "C" # Grade C if between 50 and 60.
    elif 45 <= percent < 50:
        return "D" # Grade D if between 45 and 50.
    else:
        return "No Grade" # No grade if less than 45
 
# Function to count all "A" grades.
def count_a_grades( grades ):
    count = 0
    for grade in grades: # Loop through the grades list
        if grade == "A": # Check if the grade found in the grades list is equal to "A"
            count = count + 1 # Add 1 for each "A" grade found.
    return count # Return the total count of "A" grades stored.
 
# Function to find the student with the highest percentage.
# The "Find Max" algorithm iterates through the percents list and keeps track of the maximum value and the corresponding index.
# At the end, the student with the highest percentage is identified.
def get_top_student( names, percents ):
    max = percents[0] # Start at the first position. Assume this is the highest.
    max_index = 0 # Start index at 0.
    for i in range( 1, len( percents ) ): # Start from 2nd element because we already store the 1st using the "max" variable.
        if percents[i] > max: # Check if a higher percentage is found.
            max = percents[i] # If found, update the maximum percentage.
            max_index = i # Update the index.
    return names[max_index], max # Return the name and index of the top student.
 
# Main function to process and display results for all students.
def process_data():
    names, marks1, marks2 = read_data() # Get all names and marks from function.
 
    grades = [] # Empty list, will use this to store all "A" grades.
    percents = [] # Empty list, will use this to store all percentages for finding the top student.
 
    # Loop through all student names by index.
    for i in range( len( names ) ):
        name = names[i]
        course_mark = marks1[i]
        prelim_mark = marks2[i]
 
        # Calculate percentage.
        percent = calc_percent( course_mark, prelim_mark )
 
        # Get the grade.
        grade = get_grade( percent )
 
        # Store grade and percent for later.
        grades.append( grade )
        percents.append( percent )
 
        # Display results in a nice format of rows.
        print( "-" * 40 )
        print( f"{names[i]:<15} {course_mark:<18} {prelim_mark:<12} {percent:<10.2f} {grade:<10}" )
    
    # Count "A" grades for print.
    count_a = count_a_grades( grades )
    print( "-" * 40 )
    print( f"Number of 'A' Grades: {count_a}" )
 
    # Find top student and their percentage for print.
    top_student, top_percent = get_top_student( names, percents )
    print( "-" * 40 )
    print( f"Top Student: {top_student} with {top_percent:.2f}%" )
    print( "-" * 40 )
 
process_data() # Call the main function.
