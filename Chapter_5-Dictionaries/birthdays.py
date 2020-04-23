birthdays = {"Anna": "18. September", "Martha": "22. Oktober"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("There are no birthday informations for " + name)
        print("What is your birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday Database updated!")
