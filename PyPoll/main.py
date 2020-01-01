#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

# Load the CSV --------------
import csv
import os


def main():

    #Path to the file.  Uncomment second line to test on a smaller set
    csvPath = os.path.join("Resources","election_data.csv")
    # csvPath = os.path.join("Resources","election_data_test.csv")

    with open(csvPath, mode="r") as csvFile:
        
        #Initialize Variables
        candidates = [] #Array of unique candidates
        totalVotes = 0 #Increment for each vote
        
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
            
            matched_candidate = lookupCandidateByName( current_row["candidate"], candidates )

            #If the candidate is not in the candidates array, add it.
            if( not( matched_candidate) ):

                new_candidate = { 
                                "name" : current_row["candidate"],
                                "total" : 0,
                                "counties" : {}
                                }

                candidates.append( new_candidate )
                matched_candidate = lookupCandidateByName( current_row["candidate"], candidates )

            
            totalVotes += 1
            matched_candidate["total"] += 1

            #If this row's county isn't already represented on the matched candidate, add it
            if( not( current_row["county"] in matched_candidate["counties"] ) ):
                matched_candidate["counties"][current_row["county"]] = 0

            #Increment the candidate's total per county
            matched_candidate["counties"][current_row["county"]] += 1
                
    output = buildOutputString(candidates, totalVotes)

    print(output)

    # Write to text file
    with open("election_results.txt", mode="w") as resultFile:
        resultFile.write(output)

#---------------------------------------------------------------------------------------------
# Helper function definitions
# --------------------------------------------------------------------------------------------        

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

    #If not found return false
    return False

def buildOutputString(candidates, totalVotes):
    output = "Election Results \n"
    output += '---------------------------- \n'
    output += f"Total Votes: {totalVotes} \n"
    output += '---------------------------- \n'

    winner = {"name" : "none", "total" : -1}

    #Loop through each candidate: 
    for candidate in candidates:
        if( winner["total"] < candidate["total"]):
            winner = candidate

        percentage = float(candidate["total"]) / totalVotes
        percentage *= 100
        percentage = round(percentage,2)
        # Totals per candidate final readout --------------------
        output += f"{candidate['name']}: %{percentage} ({candidate['total']}) \n"
        
    # Candidate with highest total ------------
    output += "----------------------------\n"
    output += f"Winner: {winner['name']}\n"

    return output


#Execute main
main()