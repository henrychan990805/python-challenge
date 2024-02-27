import csv
import os
#Key_Variables
TotalMonths = 0
Total = 0
AveChange = 0
ProfitChange1 = 0
ProfitChange2 = 0
ProfitChangeRes = 0
TotalProfitChange = 0
GreatestInc = 0
GreatestDec = 0
Profit = 0
MonthOfGreatestInc = ''
MonthOfGreatestDec = ''
#Using a variable to define where is the resource file
SourcePath = os.path.relpath("Resources/budget_data.csv")
#Opening the resource file as read
with open(SourcePath, 'r') as Source:
    SourceReader = csv.reader(Source, delimiter = " ")
#Using next() function to skip the firstline, header
    next(SourceReader)
#Main function: analyze data from each row
    for row in SourceReader:
#Main function: Calculate the total number of months
       TotalMonths = TotalMonths + 1
       Data = row[0].split(',')
#Getting the profit of each month and store them with a variable
       Profit = float(Data[1])
#Calculating total profit
       Total = Total + Profit
#Using a variable to calculate
       ProfitChange2 = Profit
#Calculating profit change
       ProfitChangeRes = ProfitChange2 - ProfitChange1
#Calculating Maximum Increase of Profit and Maximum Decrease of Profit
       if GreatestInc < ProfitChangeRes:
           MonthOfGreatestInc = Data[0]
           GreatestInc = ProfitChangeRes
       elif GreatestDec > ProfitChangeRes:
           MonthOfGreatestDec = Data[0]
           GreatestDec = ProfitChangeRes
       ProfitChange1 = Profit
       TotalProfitChange = TotalProfitChange + ProfitChangeRes
Source.close()
#Calculating Average Change
AveChange = (TotalProfitChange - 1088983)/(TotalMonths - 1)
#Creating a folder to store output files
if os.path.exists("analysis") is False:
    os.mkdir("analysis")
AnalysisPath = os.path.relpath("analysis/analysis.csv")
#Creating and store results in a csv file
with open (AnalysisPath, 'w', newline = '') as AnalysisRes:
    AnalysisResWriter = csv.writer(AnalysisRes)
    AnalysisResWriter.writerow(["Financial Analysis"])
    AnalysisResWriter.writerow(["-"*27])
    AnalysisResWriter.writerow([f"Total Months: {int(TotalMonths)}"])
    AnalysisResWriter.writerow([f"Total: {Total}"])
    AnalysisResWriter.writerow([f"Average Change: ${'{:.2f}'.format(AveChange)}"])
    AnalysisResWriter.writerow([f"Greatest Increase in Profits: {MonthOfGreatestInc} (${int(GreatestInc)})"])
    AnalysisResWriter.writerow([f"Greatest Decrease in Profits: {MonthOfGreatestDec} (${int(GreatestDec)})"])
    AnalysisRes.close()
