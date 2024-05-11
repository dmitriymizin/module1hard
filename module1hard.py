grades= [[5, 3, 3, 5, 4,], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(sorted(students))
grades_Aaron=grades[0]
average_Aaron=sum(grades[0]) / len(grades[0])
print('Aaron:', average_Aaron)
grades_Bilbo=grades[1]
average_Bilbo=sum(grades[1])/len(grades[1])
print('Bilbo:', average_Bilbo)
grades_Johnny=grades[2]
average_Johnny=sum(grades[2])/len(grades[2])
print('Johnny:', average_Johnny)
grades_Khendrik=grades[3]
average_Khendrik=sum(grades[3])/len(grades[3])
print('Khendrik:', average_Khendrik)
grades_Steve=grades[4]
average_Steve=sum(grades[4])/len(grades[4])
print('Steve:', average_Steve)
print({('Aaron:', average_Aaron), ('Bilbo:', average_Bilbo), ('Johnny:', average_Johnny), ('Khendrik:', average_Khendrik), ('Steve:', average_Steve)})

