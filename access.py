studs = { 50:7, 100: 14}
sum = 0
for i in studs.keys():
    sum = sum + (studs[i]*i)
print(sum)
# a = [x for x in range (100)if x%2==0 ] 
# print(a)


"""
Exercise 1: 
  In some languages, it's common to use camel case (otherwise known as “mixed case”) for variables' names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.
Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.
 Implement a python  program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

"""

a = input("please enter a word in camel case")
a = list(a)
b=[x for x in a if x.upper()==x]
indices = []
for i in b:
    print(a.index(i))
    indices.append(a.index(i))
    a[a.index(i)] = i.lower()
print(indices)
added_index = 0
for i in indices:
    a.insert(i+added_index, '_')
    added_index+=1
print(''.join(a))
