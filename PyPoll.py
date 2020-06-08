# The data we need to reteieve.
# 1. The total number of number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
 
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # To do :read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    # Print the hear row.
    headers = next(file_reader)
    print(headers)
    
    #for row in file_reader:
        #print(row)

# Close the file



# Using the open() function with the "w" mode mode we will write data to the file
#with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


# Close the file
