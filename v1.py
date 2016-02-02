#Take in content from a file - CSV, JSON, etc
#Using this have all information about 2 car companies in this
#Display this car information in JSON format or whatever format you have picked
#Convert it accordingly into a Class/Objects
#Ask the user which object the functions need to be called for & call that object's function
#have functions which enable you to call the optimzer for an object
#Accordingly optimize prices of all lines within the car company, and suggest the tech decisions
#Based on the results on the optimizer, give results for all the carlines
#export the same in a file

import pyexcel as pe
#import pyexcel_xls # import it to handle xls file\
import pyexcel_xlsx as pxlsx # import it to handle xlsx file
book = pxlsx.get_book(file_name="FEC game input.xlsx")
sheets = book.to_dict();
for name in sheets.keys():
	print(name)