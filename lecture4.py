# dictionary in python
info={"key":"value",
      "name":"kushagra",
      "learning":"python",}

print(info)
print(info["name"])
info["name"]="kushagra jaiswal"
print(info)
# nested dictinary
student={"name":"kushagra",
         "score":{"chem":98,
                  "phy":97,
                  "maths":99}}
print(student["score"]["phy"])

# dictionary methods
student={"name":"kushagra",
         "score":{"chem":98,
                  "phy":97,
                  "maths":99}}

print(student.keys())
print(student.values())
print(student.items())
print(student.get("score"))
student.update({"city":"Kanpur"})
print(student)

# sets in python
collection={"kushagra", 1,2,3,3,1,2,"jaiswal"}
print(collection)
print(type(collection))
print(len(collection))
# null set
null_set=set()
print(type(null_set))

# set methods
set=set()
set.add(2)
print(set)
set.add(3)
set.add(4)
set.add(1)
print(set)
set.remove(3)
print(set)
set.clear()
print(set)

set_2={"kushagra","jaiswal","arpit","satvik",67}
# print(set_2.pop())
set_1={23,34,45,67,56}
print(set_1.union(set_2))
print(set_1.intersection(set_2))

# practice question
dictionary={"cat":"a small animal",
            "table":("a piece of furniture","list of facts and figures")}
print(dictionary)
# question2 
subjects={"python","java","c++","javascript","c","python","java","c++"}
print(len(subjects))

# question 3
marks={}

x= int(input("enter your phy marks:"))
marks.update({"phy":x})
x= int(input("enter your chem marks:"))
marks.update({"chem":x})
x= int(input("enter your maths marks:"))
marks.update({"maths":x})

print(marks)

# ques4
values={("int",9),("float",9.0)}
print(values)
print(type(values))