from bs4 import BeautifulSoup

with open('testdata/sample.html') as f:
    soup = BeautifulSoup(f, 'lxml')

CLASS_FILLED = 'List_Button_Disable'
# buttons = soup.find_all('button', class_='List_Button')
buttons = soup.select('button.List_Button')
for b in buttons:
    filled = CLASS_FILLED in b['class']
    # print(b['class'])
    print(b.attrs.get('data-pkey'), "Available" if not filled else "Filled")
