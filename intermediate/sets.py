#sets are basically high order arrays in python
#without caring for the order or how it is arranged

# you can define a set by the set keyword and wrapping around by a () symbol or just by wrapping everything by curly braces {}

programmingLanguagesSet = {"Python", "Python", "Java", "Javascript", "Typescript", "GoLang"}

print(programmingLanguagesSet)

programmingLanguagesSet.add("PHP")

print(programmingLanguagesSet)

#for sets do not have an order of objects inside of a set
#IT DOESN'T MATTER!

if "Python" in programmingLanguagesSet:
    print("Python is in the set!")