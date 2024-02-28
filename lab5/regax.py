#exercise 1:
import re
string = input()
l = re.compile('ab*?')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')

#exercise 2:
import re
string = input()
l = re.compile('ab{2,3}')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')

#exercise 3:
import re
string = input()
l = re.compile('[a-z]+_[a-z]+')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')

#exercise 4:
import re
string = input()
l = re.compile('[A-Z]+[a-z]+$')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')

#exercise 5:
import re
string = input()
l = re.compile('a.*?b$')
k = l.search(string)
if k:
    print('it\'s a match')
else:
    print('no match found')

#exercise 6:
def replace_with_colon(content):
    result_string = content.replace(' ', ':').replace(',', ':').replace('.', ':')
    return result_string


text = 'Hello World. I am Diana.'
print(replace_with_colon(text))

#exercise 7:
import re
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)

snake = "hello_everyone"
camel_case = snake_to_camel(snake)

print(f"{camel_case}")

#exercise 8:
import re
def split_to_uppercase(text):
    pattern = r'[a-z]'
    return re.sub(pattern, lambda x: x.group().upper(), text)


print(split_to_uppercase("Python"))

#exercise 9:
import re
def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'
    return re.sub(pattern, r'\1 \2', text)


print(insert_spaces('pyThon'))

#exercise 10:
import re
def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = "DianaIsBest"
snake_case = camel_to_snake(camel)

print(f"{snake_case}")