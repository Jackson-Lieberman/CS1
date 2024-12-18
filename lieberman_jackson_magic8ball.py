import random                                                                           #imports the random library                                              
while True:                                                                             #makes the code forever
    answers= ['yes', 'no', 'maybe', 'ask again']                                        #makes a list of answers
    question = input ('''What is your question?
                    ''')                                                                #asks what their question is
    first_word = question.split()[0]                                                    #finds the first work of the quesion
    if '?' in question or first_word in ['am', 'are', 'will', 'is', 'what', 'which', 'when', 'where', 'who', 'whom', 'whose', 'why', 'how']:                        
        print("The answer to " + question, "is " + (random.choice(answers)))            #if the word is in the previous list it will give a random answer
    else:
        print('That is not a question')                                                 #if its not in the list then it will say its not a question                      
