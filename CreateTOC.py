
# print('  ABC  '.strip())
# quit()

import sys,re

file = ''
# file = r'C:\Users\JGarza\Desktop\README - Copy.md'
# file = r'C:\Users\JGarza\GitHub\VAERS\README.md'

try:
    file = sys.argv[1]
except IndexError:
# else:
    if file == '': 
        print('\n')
        print('make sure your markdown file has <!--TOC--> in it')
        print('\n')
        file = input("what is the path to the file?\n").replace('\"','')
    #"C:\Users\JGarza\Desktop\README - Copy.md"
print(file)


data = ''
with open(file,'r') as f: # Use file to refer to the file object
    data = f.readlines()

strFile = ''.join(data)
items = ''

# print(data)
i = 0 
while i < len(data):
    # print(data[i])
    
    isHeader = False

    if data[i][0] == '#':
        isHeader = True
    
    try:
        if data[i+1][:3] == '---':
            isHeader =  True
    except:
        pass

    if isHeader:
            headLine = data[i]
            tabCount =  len(headLine) - len(headLine.replace('#', '')) - 1
            # print(tabCount)
            tocText = re.sub("#","",headLine).strip()
            tocLink = '#' + tocText.lower().replace(' ', '-')
            item = '\t'*tabCount + '* ' + '[' + tocText + ']' + '(' + tocLink + ')\n'
            items = items + item

    i+=1

items = '<!--TOC-->\n' + items + '\n<!--TOC-->'
strFile = re.sub('<!--TOC-->(.|\\n|\\t)*<!--TOC-->',items,strFile)

with open(file,'w+') as f:
    f.write(strFile)



#input('**press enter to continue**\n')