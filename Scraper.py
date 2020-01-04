import declarations as d

d.driver.get(d.websites[0])
content =  d.driver.page_source
soup = d.b4(content)

print(soup.prettify())

# for a in soup.findAll('a', href=True, attrs={'class':'tab-content'}):
#     for b in a.findAll('a', href=True, attrs={'class':'tab-pane active'}):
#         for c in b.findAll('a',href=True, attrs={'class':'table table-striped'}):
#             name = c.find('div', attrs={'class':'_3wU53n'})

x = input()