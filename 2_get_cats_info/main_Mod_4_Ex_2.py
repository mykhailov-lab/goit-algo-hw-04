from data_Mod_4_Ex_2 import get_cats_info
from colorama import Fore, Style
path = "cats_file.txt"
cats_info = get_cats_info(path)
for cat in cats_info:
    print (f' {Fore.GREEN}id: {cat['id']} name: {cat['name']} cat: {cat['age']}')
#print(cats_info)