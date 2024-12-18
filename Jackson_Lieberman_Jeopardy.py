categories = ['Hobbies 100', 'Hobbies 200','Hobbies 300','Family 100','Family 200', 'Family 300', 'Sports 100', 'Sports 200', 'Sports 300']  #make string of catagoreys 
values = [100, 200, 300, 100, 200, 300, 100, 200, 300]       #create list of values 
questions = ["What is Jackson's favorite hobby? ", "What is Jackson's least favorite hobby? ", "What was Jackson's favorite hobby when he was young? ", "How many siblings does Jackson have? ", "Whats Jackson's brothers name? ", "Where is Jackson's mom from? ", "What is Jackson's main sport? ", "What sport does Jackson play during the fall ", "What sport did Jackson play for one season in 8th grade? "] #create string of questions
answers = ["Coding", "Reading", "Legos", "1", "Griffin", "South Africa", "Squash", "Soccer", "Football"]    #create a string of answers
score = 0                                                    # create a score variables

question = '''Which category do you want?

        Hobbies 100    Family 100    Sports 100
        Hobbies 200    Family 200    Sports 200
        Hobbies 300    Family 300    Sports 300   

        '''                                                  #create a variable that be edited later and will be printed
name = input('''What is your name?
             ''')                                            # ask what the users name is 
print("Hello " + name, "welcome to Jackson's Jeopardy!")     # print a welcome 

while len(categories) >= 1:                                  # while the length of the string called catagories is greater than or equal to 1                             
    while True:                                              #so that the code stays in an infinite loop until the previous line is not true
        category = str.capitalize(input(question))                  #asks what cataorgy you want and prints the function q which was defined earlier
      
        if category not in categories:                       #if the catagorey isnt in the list called catagories 
            print ('Invalid answer, pick again! ')           #tell the user to print again
        else:                                                #if the previous line isnt the case then stop the current loop
            break
        
    index = categories.index(category)                       #defines the variable index 
    answer = input(questions[index])                         #makes a function called answer that is defined by what the user inputs

    if answer == answers[index]:                             #if the answer is correct
        score += values[index]                               #add the value from the string of values to the varible we created
        print (f'''Correct!
               Your score is {score}

               ''')                                          #tell the user they got it right and tell them their score
        
        categories.pop(index)                                #remove the value from catagoreys so you cant answer the same question twice
        values.pop(index)                                    #remove the value from questions so you cant answer the same question twice
        questions.pop(index)                                 #remove the value from questions so you cant answer the same question twice
        answers.pop(index)                                   #remove the value from answers so you cant answer the same question twice
        question=question.replace(category, "           ")   #replace the catagory from the question variable we created earlier
    else:                                                    #if not correct
        print(f'''Incorrect!
    The correct answer was {answers[index]}''')              #tell the user it was incorrect and show them the correct answer
        categories.pop(index)                                #remove the value from catagoreys so you cant answer the same question twice
        values.pop(index)                                    #remove the value from questions so you cant answer the same question twice
        questions.pop(index)                                 #remove the value from questions so you cant answer the same question twice
        answers.pop(index)                                   #remove the value from answers so you cant answer the same question twice
        question=question.replace(category, "           ")
