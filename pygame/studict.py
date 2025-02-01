stu = {}

stunum=int(input("Enter the number of students"))

for i in range(1,stunum+1):
    name=input(f"enter name of the student {i}:")
    roll=int(input(f"enter the roll no of student {i}"))
    dayab=int(input(f"enter the no of days student {i} was absent:"))
    stu[f'st{i}']={'name':name,'roll':roll,'dayab':dayab}
    
r1 = {k: (v['roll'], v['dayab']) for k, v in stu.items() if v['dayab'] > 4}

print(r1)
