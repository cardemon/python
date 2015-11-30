def HM1_2(text):
     max_count = 0
     the_char = ''
     unique = list(set(text.lower()))
     unique = sorted(unique)
     for char in unique:
         if char.isalpha():
             if text.lower().count(char)>max_count:
                 max_count = text.lower().count(char)
                 the_char = char
     return the_char

print(HM1_2("Hello World!"))
print(HM1_2("LALALALA!"))
print(HM1_2("abe!"))
print(HM1_2("AAaooo!!!!"))
print(HM1_2("LOOL!"))

