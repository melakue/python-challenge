import csv
total=0
No_of_month=0
Profitlossvalues=[]
months=[]
change=[]
changesum=0
maxvalue=0
greatest_increase=0
Greatest_Decrease=0
with open("budget_data.csv", 'r') as csvfile:
    csvcontent=csv.reader(csvfile, delimiter=",")
    next(csvcontent,None)
    #maxvalue=csvcontent[1]
    maxpos=0
    for row in csvcontent:
        #if (row[0][1]==867884):
        No_of_month=No_of_month+1
        total=total + float(row[1])
        months.append(row [0])
        Profitlossvalues.append(row [1])
        #minProfitlossvalue=Profitlossvalues[0]
    for i in range(1,len(Profitlossvalues)):
        change.append(((float(Profitlossvalues[i]))-(float(Profitlossvalues[i-1]))))
    for J in range(0, len(change)):
        changesum=changesum+float(change[J])
     #maxProfitlossvaluechange=Profitlossvalues[0]   
    greatest_increase=max(change)
    Greatest_Decrease=min(change)
    maxpos = change.index(max(change))
    minpos=change.index(min(change))
    #print(f"maximum position :{months[maxpos+1]}")
    print(f"Total months: {No_of_month}")
    print(f"Total: {(int(total))}")
    print(f" Average  Change: $ {round((changesum/len(change)),2)}")
    print(f"Greatest_increase in Profits :{months[maxpos+1]} ({int(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {months[minpos+1]} ({int(Greatest_Decrease)})")

    myfile=open("outputfile.txt", 'w+')
    myfile.write(f"Total months: {No_of_month}\n")
    myfile.write(f"Total: {(int(total))}\n")
    myfile.write(f"Average  Change: $ {round((changesum/len(change)),2)}\n")
    myfile.write(f"Greatest_increase in Profits :{months[maxpos+1]} ({int(greatest_increase)}\n")
    myfile.write(f"Greatest Decrease in Profits: {months[minpos+1]} ({int(Greatest_Decrease)})\n")
    myfile.close()