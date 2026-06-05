marks = []

for i in range(3):
    mark = int(input("Give marks of Student "+str(i+1)+":  "))
    marks.append(mark)

avg = sum(marks)/3

print("Average: ", avg)
