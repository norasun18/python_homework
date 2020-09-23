alcoholic = input("Enter the amount of the alcoholic drink (l).\n")
content = input("Enter the alcohol content of the alcoholic drink (%).\n")
nonalcoholic = input("How much non-alcoholic drink do you want to add (l)?\n")
a = float(alcoholic)
b = float(content)
c = float(nonalcoholic)
abv = a*b/(a+c)
print("Alcohol content of the drink is", abv, "%.")

