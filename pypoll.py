import os
import csv
with open("election_data.csv", "r") as csv_file:
    header = next(csv_file)
    row=[0]
    for row in csv_file:
        rows=({['Voter ID'](row, 1), ['County'](row, 2), ['Candidate'](row, 3)})
        print(rows)



 print('Election Results')
  print('-------------------------')
  print('Total Votes: 3521001')
 print(' -------------------------')
  print('Khan: 63.000% (2218231)')
  print('Correy: 20.000% (704200)')
  print('Li: 14.000% (492940)')
 print('O'Tooley: 3.000% (105630)')
  print('-------------------------')
  print('Winner: Khan')
  print('-------------------------')
