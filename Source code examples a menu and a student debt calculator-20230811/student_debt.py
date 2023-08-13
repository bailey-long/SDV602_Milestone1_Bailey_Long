a_list_of_tuples = [('John','Doe',230,50000), \
		('Jane','Doe',260,70000),  \
		('Tane','Kahurangi', 220, 60000),\
		('Hinemoa','Awatea',240,40000)]
print("The original list\n",a_list_of_tuples)

# Calculate the total student debt
student_debt = 0
for a_student in a_list_of_tuples:
      student_debt += a_student[3]
print(f'\n\nTotal Student Debt = {student_debt}\n')


# Calculate if the student uses up all the weekly income, how many weeks it will take to pay off for each student. 
# Make a new list that contains new tuples 
# that include weeks to pay off.
new_list = []
for a_student in a_list_of_tuples:
      new_student = a_student + ((a_student[3] / a_student[2]),)
      new_list += [new_student]
print("\nNEW LIST \n", new_list)

# Do the same calculation, but update the existing list with the new tuples
for index in range(len(a_list_of_tuples)):
      a_student = a_list_of_tuples[index]
      new_student = a_student + ((a_student[3] / a_student[2]),)
      a_list_of_tuples[index] = new_student
print("\nExisting list updated\n",a_list_of_tuples)