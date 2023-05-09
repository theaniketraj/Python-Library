# Write a python program to fill in a letter template with name and date

name = input("Enter your name: ")
date = input("Enter the date: ")
template = '''
Dear <|Name|>
You are selected
<|Date|>
'''
print(template.replace('<|Name|>',name).replace('<|Date|>',date))

