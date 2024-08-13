grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_ = ['Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron']
Aaron_grades = sum(grades[0])/5
Aaron_ = students_.pop(4)
Bilbo_grades = sum(grades[1])/4
Bilbo_ = students_.pop(1)
Johnny_grades = sum(grades[2])/4
Johnny_ = students_.pop(0)
Khendrik_grades = sum(grades[3])/3
Khendrik_ = students_.pop(1)
Steve_grades = sum(grades[4])/5
Steve_ = students_.pop(0)
grades_ = {Aaron_: Aaron_grades, Bilbo_: Bilbo_grades, Johnny_: Johnny_grades, Khendrik_: Khendrik_grades, Steve_: Steve_grades}
print(grades_)
