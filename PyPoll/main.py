import csv
total=0
No_of_votes=0
uniquevalues=[]
candidateslist=[]
candidatesvote = []
maxpos=0
with open("election_data.csv", 'r') as csvfile:
    csvcontent=csv.reader(csvfile, delimiter=",")
    next(csvcontent,None)
    maxpos=0
    print(f"Election Results")
    print("--------------------")
    for row in csvcontent:
        No_of_votes=No_of_votes+1
        candidateslist.append(row[2])
    print(f"Total Votes:  {No_of_votes}")
    print("-----------------------")
    myfile=open("outputfile.txt", 'w+')
    myfile.write(f"Election Results\n")
    myfile.write(f"---------------------\n")
    myfile.write(f"Total Votes: ")
    myfile.write(f"{No_of_votes}\n")
    myfile.write(f"-----------------------\n")
    for i in range(len(candidateslist)):
        if candidateslist[i] not in uniquevalues:
            uniquevalues.append(candidateslist[i])
    for j in range(len(uniquevalues)):
        candidatesvote.append(candidateslist.count(uniquevalues[j]))
        print(f"{uniquevalues[j]}: {format(float(((candidateslist.count(uniquevalues[j])/No_of_votes)*100)),'.3f')}% ({candidatesvote[j]})")
        myfile.write(f"{uniquevalues[j]}: {format(float(((candidateslist.count(uniquevalues[j])/No_of_votes)*100)),'.3f')}% ({candidatesvote[j]})\n")
    maxpos = candidatesvote.index(max(candidatesvote))
    print("--------------------------")
    print(f"Winner: {uniquevalues[maxpos]}\n")
    print("-----------------------\n")
    myfile.write(f"---------------------\n")
    myfile.write(f"Winner: {uniquevalues[maxpos]}\n")
    myfile.write(f"---------------------------\n")
    myfile.close()