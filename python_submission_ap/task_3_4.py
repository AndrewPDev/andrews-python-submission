# Python Submission - Tasks 3 & 4.
# Andrew Piggot
# 1/12/2024

# Create function.
def calc_grade():
    course_mark = -1 # Set var to invalid value to keep the below loop running until valid input.
    while course_mark < 0 or course_mark > 60:
        course_mark = int( input( "Please enter the course mark (0-60): " ) ) # Ask user for the course mark and convert to int where possible.
        if course_mark < 0 or course_mark > 60:
            print( "Invalid mark, must be between 0 and 60." ) # Error if input is not between 0 and 60.
 
    prelim_mark = -1 # Set var to invalid value to keep the loop running until valid input.
    while prelim_mark < 0 or prelim_mark > 90:
        prelim_mark = int( input( "Please enter the prelim mark (0-90): " ) ) # Ask user for the prelim mark and conver to int where possible.
        if prelim_mark < 0 or prelim_mark > 90:
            print( "Invalid mark, must be between 0 and 90" ) # Error if input is not between 0 and 90.
 
    total_mark = course_mark + prelim_mark # Add course and prelim marks together for total mark.
    percent = ( total_mark * 100 ) / 150 # Calculate the percentage by multiplying total mark by 100 and dividing by highest possible mark.
 
    if percent >= 70:
        grade = "A" # Grade A if greater than or equal to 70.
    elif 60 <= percent < 70:
        grade = "B" # Grade B if between 60 and 70.
    elif 50 <= percent < 60:
        grade = "C" # Grade C if between 50 and 60.
    elif 45 <= percent < 50:
        grade = "D" # Grade D if between 45 and 50.
    else:
        grade = "No Grade" # No grade if less than 45
 
    # Print the percentage and the grade.
    print( f"Percentage: {percent:.0f}%" ) # :.0f to round to no trailing decimal.
    print( f"Grade: {grade}" )
calc_grade() # Run function.
