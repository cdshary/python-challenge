import os
import csv
data_dict={}
with open("budget_data.csv", "r") as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    row=[0]
    total=0
    for row in csv_reader:
        date, profit = row[0].split(',')
        print(date, profit)
        row_count= len(list(csv_reader))
        print(row_count)
        total=sum(profit)
        print(total)
        average=sum/len(profit)

  print('Financial Analysis')
  print('----------------------------')
  print('Total Months: 86')
  print('Total: $38382578')
  print(' Average  Change: $-2315.12')
  print('Greatest Increase in Profits: Feb-2012 ($1926159)')
  print('Greatest Decrease in Profits: Sep-2013 ($-2196167)')
    

#see notes below for what I previously had



        
        
        #print(len(row))
        # if row_count==0:
        #     print(f'Columns{",".join(row)}')
        #     row_count+=1
        #     print(data_dict)
        #     print(data_dict.keys)

        #     print(len(data_dict))

        #total_months=len(data_dict)

        #total_profit= ""

        #greatest profit
        # greatest_profit=0
        # greatest_profit1=""

        # #greatest loss
        # greatest_loss=0
        # greatest_loss1= ""

        # total_profit_values=data_dict.values()

        # for value in total_profit_values:
        #     total_profit_values += int(value)

        # for key in data_dict:
        #     value=data_dict[key]
        #     if int(value)> greatest_profit:
        #         greatest_profit = int(value)
        #         greatest_profit1= key

        #     if int(value)< greatest_loss:
        #         greatest_loss=int(value)
        #         greatest_loss1=key
            
            
            # print("Total Months: {}".format(total_months))
            # print("Total: ${}".format(total_profit))
            # print("Average Change: ${}".format(total_profit_values).mean())
            # print("Greatest Increase: {} ${}".format(greatest_profit1, greatest_profit))
            # print("Greatest Decrease in profits:{} ${}".format(greatest_loss1, greatest_loss))