print("Hi Greg's Students in Internship Ready")

message = "Welcome to FIU"
print(len(message))
print(message[0])
print(type(message))
print(type(3))
print(type("3"))
print(3*3)
print(3*"3")
print(len("greg")==4)

a = 10
b = 3
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division
print(10/2)
print(a//b) # floor division
print(a**b) # a to the power of b
print(a%b) # modulo

professors = ["greg", "kianoosh", "richard", "patricia", "debra"]
print(professors[0])
print(professors[-1])
professors.append("leo")
print(professors)
professors.extend(["heather", "kevin", "jason"])
print(professors)
professors.insert(2,"trevor")
print(professors)
professors[3] = "mark"
print(professors)
print(professors[3:5]) # accessing professors in positions 3 and 4
print(professors[5:])
print(professors[:3])
print(professors[:])
professors.remove("kianoosh")
print(professors)
print(professors.index("mark"))
x = professors.pop(6)
print(professors)
print(x)
print(len(professors))
print(type(professors))
professors.sort()
print(professors)
professors.sort(reverse=True)
print(professors)

for i in professors:
    print(i.title())
print("FIU")

water_data = {
    "temperature":[78,89,92],
    "pH":[6.5,6.7,6.3],
    "oxygen":[7.2,5.6,3.5]
}

print(water_data["oxygen"])

print(water_data.keys())
print(water_data.values())

import pandas as pd

df = pd.DataFrame(water_data)
print(df)

