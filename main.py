import re
from bs4 import BeautifulSoup
from soupselect import select

css = None
with open('tests/file1.css') as out:
	css = out.read()

html = None
with open('tests/file1.html') as out:
	html = out.read()

def parse(css):
	return re.finditer(
		"([^\r\,{}]+)(,(?=[^}]*{)|\s*{)([\w\t:;\-# ]*)",
		css.replace('\n', '').replace('\t', '')
	)

soup = BeautifulSoup(html)
parsed = parse(css)

for m in parsed:
	print m.group(3)
	elems = select(soup, m.group(1))
	for elem in elems:
		elem['style'] = '{}{}'.format(
			elem.get('style', ''),
			m.group(3)
		)

with open("out.html", "wb") as out:
    out.write(soup.prettify("utf-8"))
