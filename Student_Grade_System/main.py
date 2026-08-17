
""" 
this are basic project to prefect for 

1  list

2 Conditional statement

3 Looping 


"""

# this are the marks list 
marks = [23 , 45 , 67 , 23 , 45 , 89 , 90 , 21 ]
# print(int_list)
total = 0


# use by loop iterative one by one marks 
for mark in marks :
    total += mark

per = total / len(marks) # this are logic of program 


print("Total:", total)
print("Percentage:", per)

# use conditional statement create by garde system 
if per > 90:

    print("A Grade")
elif per >= 75:

    print("grade B")

elif per >= 60:

    print("C grade ")

elif per >= 45:

    print("D grade")

else :

    print("fail")



