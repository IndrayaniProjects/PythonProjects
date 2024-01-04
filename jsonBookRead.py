import json
f=open('c://GitRepos//PythonProjects//jsonBook.txt','r')
s=f.read()
print(s)

book = json.loads(s)
print(type(book))

for person in book:
    print(book[person])

