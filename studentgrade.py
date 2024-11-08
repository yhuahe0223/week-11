score  = int(input('Enter a list of student scores, One by One:(Negative number to quit): '))
#Prompts the user to begin entering the scores 
totalExc = 0
totalGood = 0
totalPass = 0 
totalFail = 0
#sets the total values for the grades 

while not score < 0 :
    score = int(input(" Student score: ")) # again it asks for the student's score 
    if score >= 90 or score >= 100: # if the score is greater than 90 or greater than 100, print excellent and add one to the total excellent grade 
        print("Excellent")
        totalExc = totalExc + 1
    elif score >=70 and score < 90:# if the score is greater than or equal to 70 or less than 90, print Good and add one to the total good grade 
        print("Good")
        totalGood = totalGood + 1
    elif score >= 50 and score < 70:# if the score is greater than or equal to 50 and less than 70, print pass and add a score to total pass grade 
        print('Pass')
        totalPass = totalPass + 1
    else:# anything that is less than 50 will be consider a fail and add to the total number of fails 
        print('Fail')
        totalFail =totalFail + 1 
#each time a score is inputed, it adds a count to the variable untill a negative number is entered 
print(f'Total Excellent:{totalExc}')
print(f'Total Good:{totalGood}')
print(f'Total Pass:{totalPass}')
print(f'Total Fail:{totalFail}')
#this collects and prints the total number of the grades 