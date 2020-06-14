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

# 1. Initalize a total vote counter.
total_votes = 0

# Candidate Options and votes
candidate_options = []
county_options = []
# Delcalre the empty dictionary.
candidate_votes = {}
county_votes = {}
# Winning Candidate, percentage, and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# County with largest vote count, percentage, Name
largest_county_turnout = ""
winning_county_c = 0
winning_county_p = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    
    # To do :read and analyze the data here.
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes +=1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Print the county name from each row
        county_name = row[1]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of Candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #If the county does not match any existing candidate
        if county_name not in county_options:
            # Add it to the list of counties.
            county_options.append(county_name)

            # Begin tracking that county vote tally.
            county_votes[county_name] = 0

        #Add a vote to that county's count.
        county_votes[county_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

#Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the file vote count to the text file.
    txt_file.write(election_results)

#Determine the percentage of votes for each candiate by looping through the counts.
#Interate through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
    
        # To do: print out each candidate's Name, vote count, and percentage of votes to the terminal
        candidate_results = f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # Save the canadidate results to our text file.
        txt_file.write(candidate_results)
            
            # Determine winning vote count and candidate
        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning_percent = 
            #vote_percentage.
            # Set the winning_candidate equal to the candidate's name.
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

    for county in county_votes:
        # Retrieve vote count of a county
        votes = county_votes[county]
        # Calculate the percentage of votes.
        votes_percentage= float(votes) / float(total_votes) * 100
        # To do: print out the County Name, vote count, and percentage of votes to the terminal
        county_results = f"{county}: {votes_percentage:.1f}%({votes:,})\n"
        # Print the county, their voter count, and percentage to the terminal
        print (county_results)
        # Save the county results to our text file.
        txt_file.write(county_results)

        # Determine which county had the greatest vote.
        if (votes > winning_county_c) and (votes_percentage > winning_county_p):
            #If true then set winning_count_c = votes and winning_county_p = 
            #county.
            # Set the Largest County Turnout equal to the county name.
            winning_county_c = votes
            winning_county_p = votes_percentage
            largest_county_turnout = county           
            

    # Print the winning candidates' results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    # Print the County results to the terminal
    county_summary = (
        f"-------------------------\n"
        f"Winning Votes: {winning_county_c:,}\n"
        f"Winning Percentage: {winning_county_p:.1f}%\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n")
    print(county_summary)
    # Save the County results to the text file.
    txt_file.write(county_summary)


#Done up to lesson 3.5.6
#print(f"{candidate}: received {vote_percentage}% of the vote.")
# Print the candidate vote dictionary
#print(candidate_votes)
# Print the candidate name and percentage of votes.

#print(candidate_options)


# 3. Print the total votes.
#print(total_votes)

# Close the file

#print(headers)

# Using the open() function with the "w" mode mode we will write data to the file
#with open(file_to_save, "w") as txt_file:

# Write some data to the file.
#    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


# Close the file
