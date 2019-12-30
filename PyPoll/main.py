#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# Load the CSV --------------
import csv
import os


def main():

    csvPath = os.path.join("Resources","election_data.csv")

    with open(csvPath, mode="r") as csvFile:
        
        #Initialize Variables
        candidates = [] #Array of unique candidates
        VIDs = [] #Array of unique voter Ids
        totalVotes = 0 #Increment for each vote
        questionableVoters = [] #Array that will hold all voter IDs that have multiple votes in the sheet
        
        csvReader = csv.reader(csvFile)

        # Exclude Header --------------
        next(csvReader)

        # Loop Through Contents -------
        for row in csvReader:

            #Initialize dictionary, because I think it represtents a nice way to think about a row.
            current_row = {
                "VID" : row[0],
                "county" : row[1],
                "candidate" : row[2]
            }
            
            #If the candidate is not in the candidates array, add it.
            if( not( current_row["candidate"] in candidates) ):

                new_candidate = { 
                                "name" : current_row["candidate"],
                                "total" : 0,
                                "VIDs" : [] 
                                }

                candidates.append( new_candidate )

            #Lookup the entry to the candidate's list
            matched_candidate = lookupCandidateByName( current_row["candidate"], candidates )
        #   #Running total ------------
            
            #Add to total if they are a new unique voter
            if ( voterIsUnique(current_row["VID"], VIDs) ):
                totalVotes += 1
                matched_candidate["total"] += 1
                #Add this voter to the candidate's voter list
                matched_candidate["VIDs"].append( current_row["VID"] )
                #Add this voter to the list of all voters
                VIDs.append(current_row["VID"])
            else: #This voter has multiple votes
                questionableVoters.append(current_row["VID"])

            print(totalVotes)
                


    # Totals per candidate final readout --------------------
    print(candidates)
    # Candidate with highest total ------------

    # Write what you get

# Returns a candidate dict from the list of candidates that matches the one you pass in by name
def lookupCandidateByName(lookupCandidateName = "none", candidates ="none"):
    
    if lookupCandidateName == "none":
        print("A lookupCandidateName must be specified")
        return -1
    if candidates == "none":
        print("An array of candidate dicts must be provided")
        return -1
    
    for candidate in candidates:
        if(lookupCandidateName == candidate["name"] ):
            return candidate

#TODO, write this function and use it to filter candidates in the loop
def voterIsUnique(VID = "none", VIDs = "none"):
    if( VID in VIDs ):
        return False
    else: 
        VIDs = VIDs.append(VID)
        return True



#Execute main
main()