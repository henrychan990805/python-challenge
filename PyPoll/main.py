import os
import csv
#Key_Variables
TotalVotes = 0
CharlesStockham_Count = 0
DiannaDeGette_Count = 0
RaymondDoane_Count = 0
CharlesStockham_Count_Percent = 0
DiannaDeGette_Count_Percent = 0
RaymondDoane_Count_Percent = 0
Winner_list = []
ResoursePath = os.path.relpath("Resources/election_data.csv")
with open(ResoursePath,"r") as Resourse:
    VoteDataReader = csv.reader(Resourse, delimiter = ",")
    next(VoteDataReader)
    for row in VoteDataReader:
        if row[2] == "Charles Casper Stockham":
            CharlesStockham_Count += 1
        elif row[2] == "Diana DeGette":
            DiannaDeGette_Count += 1
        elif row[2] == "Raymon Anthony Doane":
            RaymondDoane_Count += 1
    Resourse.close()
TotalVotes = CharlesStockham_Count + DiannaDeGette_Count + RaymondDoane_Count
Candidates = [CharlesStockham_Count,DiannaDeGette_Count,RaymondDoane_Count]
CharlesStockham_Count_Percent = '{:.3f}'.format((CharlesStockham_Count/TotalVotes)*100)
DiannaDeGette_Count_Percent = '{:.3f}'.format((DiannaDeGette_Count/TotalVotes)*100)
RaymondDoane_Count_Percent = '{:.3f}'.format((RaymondDoane_Count/TotalVotes)*100)
if max(Candidates) == CharlesStockham_Count:
    Winner_list.append("Charles Casper Stockham")
if max(Candidates) == DiannaDeGette_Count:
    Winner_list.append("Diana DeGette")
if max(Candidates) == RaymondDoane_Count:
    Winner_list.append("Raymon Anthony Doane")
if os.path.exists("analysis") is False:
    os.mkdir("analysis")
election_result = os.path.relpath("analysis/analysis.csv")
with open(election_result,'w',newline='') as election_data:
    election_data_writer = csv.writer(election_data)
    election_data_writer.writerow(["Election Results"])
    election_data_writer.writerow(["-"*27])
    election_data_writer.writerow([f"Total Votes: {TotalVotes}"])
    election_data_writer.writerow(["-"*27])
    election_data_writer.writerow([f"Charles Casper Stockham: {CharlesStockham_Count_Percent}% ({CharlesStockham_Count})"])
    election_data_writer.writerow([f"Diana DeGette: {DiannaDeGette_Count_Percent}% ({DiannaDeGette_Count})"])
    election_data_writer.writerow([f"Raymon Anthony Doane: {RaymondDoane_Count_Percent}% ({RaymondDoane_Count})"])
    election_data_writer.writerow(["-"*27])
    election_data_writer.writerow([f"Winner : {Winner_list[0]}"])
    election_data_writer.writerow(["-"*27])