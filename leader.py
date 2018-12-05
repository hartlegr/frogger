from graphics import *
import operator


def leaderboard(win, name, score):

    

    score = str(score)
    #   Convert the passed name and score into a formatted string
    text = (name+" "+"-"+" "+score)
    #   Append the new score to a text fil
    file = open("high_scores.txt", "a")
    file.write(text + "\n")
    file.close()
    #   Open the high score text file and read the lines
    file = open("high_scores.txt", "r")
    
    lines = file.readlines()
    
    
    highScores = {}

    
   
    # For each line read, split the name and score
    for line in lines:
        
        line = line.split(" - ")
        
    # Add each name:score pair to the highScores dictionary
    # Jordan suggested this
        highScores[line[0]]=line[1]
        
    # Sort the items in the dictionary from highest to smallest based on the values
    
        sortedHighScores = sorted(highScores.items(), key=operator.itemgetter(1), reverse = True)


   
    file = open("high_scores.txt", "w")
    for scorer in sortedHighScores:
    # Now that the name/score pairs are sorted, overwrite each line of the high_scores file
    # with the correct order of scores
        
        
        ordered_text = (scorer[0]+" - "+scorer[1])
        
        
        
        
        file.write(ordered_text)
        
    # Draw the text file to the window
        
    file = open("high_scores.txt", "r")
    screen = file.read() 
    
    scoreboard = Text(Point(250, 250), screen)
    scoreboard.setFill("green")
    scoreboard.setSize(30)
    scoreboard.draw(win)
    
    
    file.close()





#   REFERENCES
# This was created with the help of stack overflow
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# Question by Gern Blanston
# https://stackoverflow.com/users/2786/gern-blanston
# Answer by Devin Jeanpierre
# https://stackoverflow.com/users/18515/devin-jeanpierre
# sorted_x = sorted(x.items(), key=operator.itemgetter(0))


