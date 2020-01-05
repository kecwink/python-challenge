#modules
import os
import csv

#set path for filec
csvpath = os.path.join("PyPoll", "election_data.csv")
#print(os.path.abspath('..'))

#open the CSV 
with open(csvpath, newline ='')as csvfile:
    election_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(election_data)

    #print the rows
    #for row in election_data:
        #print(row)

    #print results header
    print("Election Results")

    #count the number of voters
    num_of_voters = 0
    for rows in election_data:
        num_of_voters += 1
    print(f'Number of Voters: {num_of_voters}')

    #convert data into index-able object
with open(csvpath, newline ='')as csvfile:
    election_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(election_data)

    #count the number of votes for each candidate
    index_election_data = []
    Khan = 0
    Correy = 0
    Li = 0
    O_Tooley = 0
    for rows in election_data:
        for item in rows:
            #print(item)
            #for letters in item:
            if item == 'Khan':
                Khan +=1
            elif item == 'Correy':
                Correy +=1 
            elif item == 'Li':
                Li += 1
            elif item == 'O\'Tooley':
                O_Tooley += 1 
            else:
                continue

    #calculate the percentage of votes each candidate recieved
    Khan_percentage= float('{0:.2f}'.format((Khan/num_of_voters)*100))
    Correy_percentage= float('{0:.2f}'.format((Correy/num_of_voters)*100))
    Li_percentage= float('{0:.2f}'.format((Li/num_of_voters)*100))
    O_Tooley_percentage= float('{0:.2f}'.format((O_Tooley/num_of_voters)*100))

#print the percentage of votes each candidate recieved, followed by number of votes
print('Votes by Percentage')
print(f' Khan: {Khan_percentage}% ({Khan})')
print(f' Correy: {Correy_percentage}% ({Correy})')
print(f' Li: {Li_percentage}% ({Li})')
print(f' O_Tooley: {O_Tooley_percentage}% ({O_Tooley})')

#calculate the winner
#create a dictionary with total votes for each candidate
votes_by_candidate = {'Khan':661583, 'Correy':209046, 'Li':146360, 'O_Tooley':31586}

#find the canidate with the most popular votes
import operator
popular_winner = max(votes_by_candidate, key=lambda key: votes_by_candidate[key])
#print(popular_winner)
print(f'Winner:{popular_winner}')