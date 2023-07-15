# Regular expressions

import re

# match

my_string = "Esta es la lección número 7:\n Expresiones Regulares"
my_other_string = "Esta es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span())


print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_other_string))

if not match == None:
    print(match)
    start, end = match.span()
    print(my_string[start:end])


# search
print("-"*30)
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(start, end)
print(my_string[start:end])

# findAll

findall = re.findall("lección", "aaaa lección lección hello", re.I)
print(findall)

# split

print(re.split("\n", my_string))

# sub

print(re.sub("Expresiones", "LECCIÓN", my_string, re.I))

