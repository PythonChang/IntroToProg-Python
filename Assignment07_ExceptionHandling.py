#-------------------------------------------------#
# Title: Exception Handling
# Dev:   Samantha Chang
# Date:  May 18, 2019
# ChangeLog: (Who, When, What)
#-------------------------------------------------#

try:
    OpenFile = open('To_Do.txt')
    if OpenFile.name == "To_Do.txt":
        raise Exception
except Exception as e:
    print("Error")
except FileNotFoundError as e:
    print(e)
else:
    print(OpenFile.read())
    OpenFile.close()
finally:
    print("Executing finally")