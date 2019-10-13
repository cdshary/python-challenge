import os 
import csv
#open the file 
with open('script1.txt') as csv_file:

    #initialize csv reader
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    print(csv_reader)
    header=next(csv_reader)
    for row in csv_reader:
        month=str(Date+)
        profit=int(Profit/Losses+)
        print(row)
        total+=int(row+1)
        
    
    
    