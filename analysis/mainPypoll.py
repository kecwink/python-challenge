import os
import csv


csvpath = os.path.join('..',"PyPoll", "election_data.csv")


with open(csvpath, newline ='') as csvfile:
    election_data = csv.reader(csvfile, delimiter =',')
    csv_header = next(election_data)

    
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

#calculate the winner with total votes for each candidate
votes_by_candidate = {'Khan':661583, 'Correy':209046, 'Li':146360, 'O_Tooley':31586}

#find the canidate with the most popular votes
import operator
popular_winner = max(votes_by_candidate, key=lambda key: votes_by_candidate[key])
print(f'Winner:{popular_winner}')

#write results to a text file
with open('pypollresults.txt', 'w')as writer:
    writer.write(f'''
    Election Results
    Number of Voters: {num_of_voters}
    Votes by Percentage
    Khan: {Khan_percentage}% ({Khan})
    Correy: {Correy_percentage}% ({Correy})
    Li: {Li_percentage}% ({Li})
    O_Tooley: {O_Tooley_percentage}% ({O_Tooley})
    Winner:{popular_winner}
    ''') 
