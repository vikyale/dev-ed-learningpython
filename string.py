language="Python"

##Longitud del string 

#print(len(language))

##Access each individual letter
letter = language[0]
letter4 = language[4]

letter = language[0:3]
print(letter)
print(letter4)

letter1=language[1:]

print(letter1)

letter2=language[-1]
print(letter2)

upper_languaje=language.upper()
print(upper_languaje)

street= 'Calle los Milagros 234 LA VICTORIA'
lower_text= street.lower()

print(lower_text)

find_text = street.find('234')

print(find_text)

replace_text = street.replace('234','994')
print(replace_text)