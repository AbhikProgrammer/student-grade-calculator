marks = []

for i in range(3):
    mark = int(input("Give marks of Student "+str(i+1)+":  "))
    marks.append(mark)

avg = sum(marks)/3

print("Average: ", avg)

if avg >= 90:
    print("Grade A")

elif avg >= 60:
    print("Grade B")

elif avg >= 20:
    print("Grade C")

else:
    print("You Failed")

print("\n Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))
