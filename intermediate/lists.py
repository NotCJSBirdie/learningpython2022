# welcome to lists
# other languages called this array! familiar?

programmingLanguages = ["Python", "Java", "Javascript", "Typescript", "GoLang"]

print(programmingLanguages[0])
print(programmingLanguages[1])
print(programmingLanguages)

programmingLanguages.append("C++")
print(programmingLanguages)

# looping through an array

for i in range(len(programmingLanguages)):
    print(programmingLanguages[i])
    
    
for language in programmingLanguages:
    print(language)