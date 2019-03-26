import csv
total=0
No_of_month=0
Profitlossvalues=[]
change=[]
changesum=0
greatest_increase=0
Greatest_Decrease=0
with open("budget_data.csv", 'r') as csvfile:
    csvcontent=csv.reader(csvfile, delimiter=",")
    next(csvcontent,None)
    for row in csvcontent:
        No_of_month=No_of_month+1
        total=total + float(row[1])
        Profitlossvalues.append(row [1])
    for i in range(1,len(Profitlossvalues)):
        change.append(((float(Profitlossvalues[i]))-(float(Profitlossvalues[i-1]))))
    for J in range(0, len(change)):
        changesum=changesum+float(change[J])
    greatest_increase=max(change)
    Greatest_Decrease=min(change)
    
    print(f"Total months: {No_of_month}")
    print(f"Total: {total}")
    print(f" Average  Change: $ {changesum/len(change)}")
    print(f"Greatest_increase in Profits: {greatest_increase}")
    print(f"Greatest Decrease in Profits: {Greatest_Decrease}")