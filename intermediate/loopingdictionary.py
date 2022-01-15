books = {
    "harryPotter": 900,
    "percyJackson": 600,
    "hero": 400
}

for key,val in books.items():
    print(" Name of book " + key)
    print("Pages" + str(val))
    print("_________")
    
books["theSelection"] = 300

print(books)