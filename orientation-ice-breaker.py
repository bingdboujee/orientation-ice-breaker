from bs4 import BeautifulSoup
from urllib.request import urlopen

qList = []

url = 'https://hobbylark.com/party-games/Free-Fun-100-Question-Quiz-3'
ourUrl=urlopen(url)
soup=BeautifulSoup(ourUrl,'html.parser')
for i in soup.find_all('div',{'class':'full module moduleText'}):
    per_question=i.find('ol')
        
    qList.append(per_question)

qList = filter(None,qList)

newQuestion = []

for each in qList:

    new_each = str(each).replace('<li>','').replace('<ol>','').replace('<strong>','').replace('<em>','').replace('</li>','').replace('</ol>','').replace('</strong>','').replace('</em>','')
    newQuestion.append(new_each)
        
    

with open('question3.txt','a') as f:
    for each in newQuestion:
         f.write(each+'\n') 
    

studentList = ['Bingdi', 'Michael', 'John', 'Charles', 'Anna']
questionList = []
answerList = []
import random
print('Hello everyone! This is the last part of Gabelli Business School orientation - icebreaker. Let me explain the rule first. The system will randomly choose one student to answer a trivia question. The student needs to type in the answer and the system will show if the answer is right or wrong. Every student will have a chance to participate. The game will end once everybody participate.')
userInput = input('Actually...RP just told me after a long day you probably want to go home directly. So enter stop to end the game and go home now!\n')

try:
    if userInput == 'stop':
        raise IndexError('This game is MANDATORY!!!What are you thinking?')
    

except IndexError as errorMessage:
    print(errorMessage)
userInput = input('Type anything to enter the game. System will randomly select one student to answer the Jeopardy question.\n')

if userInput != 'stop':
    
        
    
   
        readFile = open(r'C:\Users\bingd\OneDrive\Desktop\question3.txt', 'r')
        line = readFile.readline()
        
        while len(studentList) > 0:
            for line in readFile:
             
                luckyYou = random.choice(studentList)
                print ('It is ' + luckyYou +' !')
            
            
                if line[0] == '\n':
                    pass
                if line[0] != '\n':
                    print('Your question is:>>>>')
                    x = line.index('?')
                    question = (line[:x+1])
                    questionList.append(question)
                    print(question)
                    answer = (line[x+2:]).replace('\n','').replace('.','')
                    answerList.append(answer)
                    userGuess = input('Please enter the answer:>>>>')
                    if userGuess.lower() != answer.lower():
                        print('Your answer is wrong! Pass to the next student.')
                    if userGuess.lower() == answer.lower():
                        print('Your answer is right! Congratulations. Now it is time for the next student.')
                studentList.remove(luckyYou)
                if len(studentList) == 0:
                    break
                

              
                    
            readFile.close()
            print('All the students have participated the game. Thanks for participating the game.')
            print('All the questions and answers that have answered are saved as a .csv file for documenting purpose.')
            combineFile = zip(questionList,answerList)
            import csv
            with open('questionList2.csv','w') as out:
                csv_out=csv.writer(out)
                csv_out.writerow(['question','answer'])
                for row in combineFile:
                    csv_out.writerow(row)
