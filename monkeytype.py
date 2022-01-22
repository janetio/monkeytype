from htmlformonkey import htmldoc
from bs4 import BeautifulSoup
import pyautogui
res = (BeautifulSoup(htmldoc,'html.parser')).find_all(class_='word')
totalwords=[]
for word in res:
    totalwords.append(word.getText())
pyautogui.write(' '.join(totalwords))