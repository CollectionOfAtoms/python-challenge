#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# Load the CSV --------------
import csv
import os

csvPath = os.path.join("Resources","election_data.csv")

#Initialize Variables
totalVotes = 0 #Increment for each vote
candidates = [] #Array of unique candidates

with open(csvPath, mode="r") as csvFile:
    csvReader = csv.reader(csvFile)

    # Exclude Header --------------
    csvHeader = csvReader.next("")

    # Loop Through Contents -------
    for row in csvReader:
        
        totalvotes += 1

        #Initialize dictionary, because I think it represtents a nice way to think about a row.
        current_row = {
            "VID" : row[0]
            "county" : row[1]
            "candidate" : row[2]
        }
        
        #If the candidate is not in the candidates array, add it.
        if( not( current_row["candidate"] in candidates) ):

            new_candidate = { 
                            "name" : current_row["candidate"},
                            "total" : 0,
                            "VIDs" : [] 
                            }


            candidates = candidates.append( new_candidate )
        #We know about the candidate at this point. 
        #Lookup the entry to the candidate's list
        matched_candidate = lookupCandidateByName( current_row["candidate"], candidates )
    #   #Running total ------------
        
        #Add to total if they are a new unique voter
        if ( voterIsUnique(VID, UniqueVoters) )

        matched_candidate["total"] += 1
    #   #Build array of unique candidates -----------
        Matched_candidate["VIDs"].append( current_row["VID"] )
    #   #Running Totals per candidate ------------

# Totals per candidate final readout --------------------
# Candidate with highest total ------------

# Write what you get

# Returns a candidate dict from the list of candidates that matches the one you pass in by name
def lookupCandidateByName(lookupCandidateName = "none", candidates ="none"):
    
    if lookupCandidateName == "none" {
        throw new error("A lookupCandidateName must be specified")
    }
    else if candidates == "none"
        throw new error("An array of candidate dicts must be provided")
    
    for candidate in candidates:
        if(lookupCandidateName == candidate["candidate"] ):
            return candidate

#TODO, write this function and use it to filter candidates in the loop
def voterIsUnique(VID = "none", VIDs = "none")