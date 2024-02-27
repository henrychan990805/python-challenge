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
#CSV_Reader
SourcePath = os.path.relpath("Resources/budget_data.csv")
with open(SourcePath, 'r') as Source:
    SourceReader = csv.reader(Source, delimiter = " ")
    next(SourceReader)
    for row in SourceReader:
       TotalMonths = TotalMonths + 1
       Data = row[0].split(',')
       Profit = float(Data[1])
       Total = Total + Profit
       ProfitChange2 = Profit
       ProfitChangeRes = ProfitChange2 - ProfitChange1
       if GreatestInc < ProfitChangeRes:
           MonthOfGreatestInc = Data[0]
           GreatestInc = ProfitChangeRes
       elif GreatestDec > ProfitChangeRes:
           MonthOfGreatestDec = Data[0]
           GreatestDec = ProfitChangeRes
       ProfitChange1 = Profit
       TotalProfitChange = TotalProfitChange + ProfitChangeRes
Source.close()
AveChange = (TotalProfitChange - 1088983)/(TotalMonths - 1)
if os.path.exists("analysis") is False:
    os.mkdir("analysis")
AnalysisPath = os.path.relpath("analysis/analysis.csv")
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
