# # Unit 3 | Assignment - Py Me Up, Charlie
# ## PyPoll
import os
import csv
import statistics

output_path = os.path.join("..", "PyPoll", "election_output.csv")
csvpath = os.path.join('..', 'PyPoll', 'election_data.csv')

totalVotes = []
candidatesWithVotes = []
uniqueCandidatesWithVotes = []
percentOfWinsPerCandidate = []
totalVotesPerCandidate = []
winnerOfEleccion = []

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
    #     total += int(row[1])
          totalVotes.append(row[0])
          candidatesWithVotes.append(row[2])
          if row[2] not in uniqueCandidatesWithVotes:
              uniqueCandidatesWithVotes.append(row[2])
    khanVotes = candidatesWithVotes.count(uniqueCandidatesWithVotes[0])
    correyVotes = candidatesWithVotes.count(uniqueCandidatesWithVotes[1])
    liVotes = candidatesWithVotes.count(uniqueCandidatesWithVotes[2])
    oTooleyVotes = candidatesWithVotes.count(uniqueCandidatesWithVotes[3])
    totalVotes = int(len(totalVotes))
    candidatesAndVoteCount = {"Khan":khanVotes, "correyVotes":correyVotes, "liVotes":liVotes, "oTooleyVotes":oTooleyVotes}
    maximum = max(candidatesAndVoteCount, key=candidatesAndVoteCount.get)
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")
    print(f"{uniqueCandidatesWithVotes[0]}: {round(((khanVotes/totalVotes)*100))}% ({khanVotes}) ")
    print(f"{uniqueCandidatesWithVotes[1]}: {round(((correyVotes/totalVotes)*100))}% ({correyVotes}) ")
    print(f"{uniqueCandidatesWithVotes[2]}: {round(((liVotes/totalVotes)*100),)}% ({liVotes})")
    print(f"{uniqueCandidatesWithVotes[3]}: {round(((oTooleyVotes/totalVotes)*100))}% ({oTooleyVotes})")
    print("-------------------------")
    print(f"The winner is: {maximum} with {candidatesAndVoteCount[maximum]} votes")
    file = open("bankTextFile", "w")   
    file.write(f"Total Votes: {totalVotes}\n{uniqueCandidatesWithVotes[0]}: {round(((khanVotes/totalVotes)*100))}% ({khanVotes})\n{uniqueCandidatesWithVotes[1]}: {round(((correyVotes/totalVotes)*100))}% ({correyVotes})\n{uniqueCandidatesWithVotes[2]}: {round(((liVotes/totalVotes)*100),)}% ({liVotes})\n{uniqueCandidatesWithVotes[3]}: {round(((oTooleyVotes/totalVotes)*100))}% ({oTooleyVotes})\n"The winner is: {maximum} with {candidatesAndVoteCount[maximum]} votes ")
    file.close()


