#display the purpose of the program
print ("This is ECONOMICS 1st term examination question")

#display the instructions
print ("Select the letter with the correct option")

score = 0

question1 = input("\n1. A collection of data which has not been processed is referred to as? \na. disjointed data \nb. raw data \nc. class intervals \nd. Frequency. \n")
if (question1.lower()== "b"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question2 = input("\n2. An arrangement of data in rows and column is referred to as a? \na. graph \nb. bar chart \nc. pie chart \nd. Table. \n")
if (question2.lower()== "d"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question3 = input("\n3. The difference between the highest and lowest in a set of data is the? \na. Range \nb. medium \nc. variance \nd. mode. \n")
if (question3.lower()== "a"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question4 = input("\n4. The graph of the function X = a + bY is? \na. linear \nb. quadratic \nc. cubical \nd. exponential. \n")
if (question4.lower()== "b"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question5 = input("\n5. The most frequently occurring value in a given data is the? \na. mode \nb. median \nc. mean \nd. range. \n")
if (question5.lower()== "a"):

    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1
    
question6 = input("\n6. The sum of items divided by the number of items the? \na. Frequency \nb. Mean \nc. Median \nd. Mode. \n")
if (question6.lower()== "b"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1
    
question7 = input("\n7. Which of the following is a measure of central tendency? \na. Percentage \nb. Graph \nc. Variance \nd. Median. \n")
if (question7.lower()== "d"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question8 = input("\n8. Which of the following is not a set of measures of central tendency? \na. Mode and medium \nb. mean and medium \nc. Mean and mode \nd. median and percentage. \n")
if (question8.lower()== "d"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question9 = input("\n9. Which of the following tools of economic analysis is used when data contains more than one category? \na. Bar charts \nb. Component bar charts \nc. Graphs \nd. Symbolic statements. \n")
if (question9.lower()== "b"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

question10 = input("\n10. Find the mode of the following set of scores 1,1,2,2,2,3,3,4,5,?  \na. 2 \nb. 3 \nc. 4 \nd. 5. \n")
if (question10.lower()== "a"):
    print ("correct        ✔")
    score = score +1
else:
    print ("wrong          ❌")
    score = score -1

print ("Your score for this quiz is ",str(score), " over 10")