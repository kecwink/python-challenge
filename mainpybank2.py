#modules
import os
import csv

#set path for filec
csvpath = os.path.join("..", "PyBank", "budget_data.csv")
#print(os.path.abspath('..'))

#open the CSV 
with open(csvpath, newline ='')as csvfile:
    bank_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(bank_data)

    
#count the total number of months 
    months = ['J', 'F', 'M', 'A', 'S', 'O', 'N', 'D']
    num_of_months = 0
    profits =[]
    for row in bank_data:
        for data in row:
            for month in months:
                if month in data:
                    num_of_months += 1
                else:
                    continue
    print("Financial Analysis")
    print(f"Total months: "+ str(num_of_months))

#open the CSV 
with open(csvpath, newline ='')as csvfile:
    bank_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(bank_data)

#create a list with only the profits/losses    
    amounts = []

    for row in bank_data:
        for item in row:
            if len(item) != 8 or item == '-':
                amounts.append(item)
    #print (amounts)

    number_amounts = []
    for amount in amounts:
        profit1 = int(amount)
        number_amounts.append(profit1)
    #print(number_amounts)
    
#calculate the total profit
    total_profits =sum(number_amounts)
    print(f"Total profits: ${total_profits}")

#open the CSV 
with open(csvpath, newline ='') as csvfile:
    bank_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(bank_data)

#calculate the average change of the period
average_change = float('{0:.2f}'.format(total_profits/num_of_months))
print(f"The average change is: ${average_change}")


#highlight the greatest increase in profits    
#create lists of dates and profits
with open(csvpath, newline ='')as csvfile:
    bank_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(bank_data)
#create a list with only the profits/losses    
    amounts = []
    for row in bank_data:
        for item in row:
            if len(item) != 8 or item == '-':
                amounts.append(item)
    # #print(amounts)
with open(csvpath, newline ='')as csvfile:
    bank_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(bank_data)
#create a list with the dates
    dates =[]
    months = ['J', 'F', 'M', 'A', 'S', 'O', 'N', 'D']
    for row in bank_data:
        for data in row:
            for month in months:
                if month in data:
                    dates.append(data)
    #print(dates)
#create a dictionary of dates and profits
date_and_profit = dict(zip(dates, amounts))
#print(date_and_profit)

#find the key associated with tne highest profit increase
import operator
max_profit = max(date_and_profit, key=lambda key: date_and_profit[key])
#print(max_profit)
print(f'Greatest Increase in Profits:  {max_profit} : (${date_and_profit[max_profit]})')  

#find the greatest decrease in profit    
dec_profit = min(date_and_profit, key=lambda key: date_and_profit[key])
#print(dec_profit)
print(f'Greatest Decrease in Profits:  {dec_profit} : (${date_and_profit[dec_profit]})')