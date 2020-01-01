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
    output += '\n\n'
    output += buildCountyBreakdown(candidates)
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

#Creates an output string that fits minimum requirements
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

        #Careful to do floating point maths
        percentage = float(candidate["total"]) / float(totalVotes)
        percentage *= 100
        percentage = round(percentage,2)
        # Totals per candidate final readout --------------------
        # Format to read out two decimal places
        output += f"{candidate['name']}: %{'%.2f' % percentage} ({candidate['total']}) \n"
        
    # Candidate with highest total ------------
    output += "----------------------------\n"
    output += f"Winner: {winner['name']}\n"

    return output

def buildCountyBreakdown(candidates):
    output = '---------------------------- \n'
    output += 'Candidate Votes Per County \n'
    output += '---------------------------- \n'

    countyBreakdown = {}

    # Build the output string and collate data by county for later
    for candidate in candidates:
        output += f'{candidate["name"]} : Total Votes: {candidate["total"]} \n'
        for county in candidate["counties"]:

            countyTotal = candidate['counties'][county]

            # Build Dict that breaks down data by county
            if ( not(county in countyBreakdown) ):
                countyBreakdown[county] = {"total" : 0}

            countyBreakdown[county][candidate["name"]] = countyTotal 
            countyBreakdown[county]["total"] += countyTotal

            candidatePercent = float(countyTotal) / candidate["total"]
            candidatePercent *= 100
            candidatePercent = round(candidatePercent,2)
            # Totals per candidate final readout --------------------
            # Format to read out two decimal places
            output += f"    {county}: %{'%.2f' % candidatePercent} ({countyTotal}) \n"

    output += '---------------------------- \n'
    output += 'Breakdown by County \n'
    output += '---------------------------- \n'

    for county in countyBreakdown:
        countyTotal = countyBreakdown[county]["total"]
        output += f'{county} : Total Votes: {countyTotal} \n'

        for candidate in countyBreakdown[county]:
            #Don't print out the total
            if candidate == "total" : continue
            
            percentage = float(countyBreakdown[county][candidate]) / countyTotal
            percentage *= 100
            percentage = round(percentage, 2)
            output += f"    {candidate}: %{'%.2f' % percentage} ({countyBreakdown[county][candidate]}) \n"            

    return output
    


#Execute main
main()