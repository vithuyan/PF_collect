# Exercise 10
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}
for cohort, num_students in students.items():
    print("{}: {} students.".format(cohort, num_students))
students['cohort4'] = 43
print (students.keys())

def increase_cohort(list, percent):
    for cohort, num_students in students.items():
        students[cohort] = int(num_students * (1 + percent/100))

increase_cohort(students, 5)
print(students)
students.pop('cohort2')
print(students)
