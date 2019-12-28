# Reads in a csv of budget data and outputs a brief analysis to the screen and 
# to the financial_analysis.txt file
import os
import csv

csvpath =  os.path.join('Resources','budget_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Initialize data with values from the first row
    first_row = next(csvreader)
    nMonths = 1
    totalProfits = float(first_row[1])
    bestMonth = {"date": first_row[0], "profit": totalProfits}
    worstMonth = {"date": first_row[0], "profit": totalProfits}

    #Loop through each row in the csv
    for row in csvreader :
        nMonths+=1
        profit = float(row[1])
        totalProfits+=profit

        if( profit > bestMonth["profit"]):
            bestMonth = {"date" : row[0], "profit": profit}
            
        if ( profit < worstMonth["profit"]):
            worstMonth = {"date" : row[0], "profit": profit}

    averageProfit = totalProfits / nMonths
    averageProfit = round(averageProfit,2)

    output = ""
    #Build the output string
    output+="Financial Analysis \n"
    output+="---------------------------- \n"
    output+=f"Total Months: {nMonths} \n"
    output+=f"Average Change: {averageProfit} \n"

    #Adjust output language for the user.
    if(bestMonth["profit"] > 0 ):
        output+= f'Greatest increase in profits: {bestMonth["date"]} (${int(bestMonth["profit"])}) \n'
    else:
        output+="Profits did not increase in any month. \n"
        output+=f'Least decrease in profits: {bestMonth["date"]} (${int(bestMonth["profit"])}) \n'


    if(worstMonth["profit"] < 0 ):
        output+=f'Greatest decrease in profits: {worstMonth["date"]} (${int(worstMonth["profit"])}) \n'
    else:
        output+=f"No losses were incurred in any month \n"
        output+=f'Least increase in profits: {worstMonth["date"]} (${int(worstMonth["profit"])}) \n'

    #Print the output to the console
    print(output)

    #Write the output to a text file
    with open('financial_analysis.txt', 'w') as outputFile:
        outputFile.write(output)