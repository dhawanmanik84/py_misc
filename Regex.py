import re

text = "This is a new document, a line, a file, to learn regex"
pattern = r"learn"

search = re.search(pattern, text)
if search:
    print ("Pattern found:", search.group())
else:
    print ("Pattern not found")

