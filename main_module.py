import list2D as l #calling list2d.py from same folder and named it as "l"

import display_menu as dm #calling display_menu.py from same folder and named it as "dm"

import display_functions as df #calling display_function.py from same folder and named it as "df"

path="books.txt" #calling text file from same folder

upr_list = l.read_file(path) 
main_db = l.content_2dlist(upr_list) 
dm.displayMenu() 
df.display_items(main_db)
