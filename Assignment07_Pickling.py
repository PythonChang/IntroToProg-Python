#-------------------------------------------------#
# Title: Pickling
# Dev:   Samantha Chang
# Date:  May 18, 2019
# ChangeLog: (Who, When, What)
#-------------------------------------------------#

import pickle
todo_dict = {'Clean House': 'Low', 'Yard Work': 'High', 'Pay Bills': 'Med'}
filename = 'ToDo'
outfile = open(filename, 'wb')
pickle.dump(todo_dict,outfile)
outfile.close()