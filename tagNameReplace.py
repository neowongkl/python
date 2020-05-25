# python3 
# work on linux machine
# change html tag name by id
from bs4 import BeautifulSoup
from pathlib import Path
import html

tcount = 0
fcount = 0
tagPath = []
# loop through all html file inside directory
for path in Path('/mnt/c/test').rglob('*.html'):
	htmlr = open(path, 'r').read()
	soup = BeautifulSoup(htmlr, "html.parser")
	# target tag
	tag = soup.find(id='user_tmpl')
	if tag:
		tcount += 1
		tagPath.append(path)
		# change tag name
		tag.name = 'div'
		htmlw = open(path, 'w')
		htmlw.write(html.unescape(str(soup)))
		htmlw.close()
	else:	
		fcount += 1

f=open('chnage_list.txt','w')
for ele in tagPath:
    f.write(str(ele))
    f.write("\n")

f.close()

print("")
print("tcount: ", tcount)
print("fcount: ",  fcount)


