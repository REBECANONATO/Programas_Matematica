'''
Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". Keep track of the number of tags using the variable count.
'''

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here



for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count = count + 1

print(count)


'''
Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list. For example, if the list is items = ['first string', 'second string'], printing html_str should output:
'''

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here

for item in items:
    html_str = html_str + "<li>{}</li>\n".format(item)

html_str = html_str + "</ul>"

print(html_str)