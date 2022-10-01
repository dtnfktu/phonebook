import database as db
import dbfiles as fl
import menu
import os
from sys import platform

print(platform)
input()
if os.path.exists('phonebook.csv') :
    guide = fl.loadcsv('phonebook.csv')
else :
    guide = []
while True :
    key = db.printtable(guide)
    if key == 0 :
        break
    elif key == 1 :
        guide.append(menu.inputrec())
    elif key == 2 :
        guide.pop(menu.delrec() - 1)
    elif key == 3 :
        db.printtable(menu.searchrec(guide),False)
    elif key == 4 :
        menu.editrec(guide)
    elif key == 5 :
        menu.exportdata(guide)
    elif key == 6 :
        guide = menu.importdata()

fl.exportcsv('phonebook.csv', guide)
print('Работа завершена')