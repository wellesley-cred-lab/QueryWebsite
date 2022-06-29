'''
Driver file that runs create_serps_and_compare.py
# files1 is all the query.html inside the corresponding category folder of the earlier date folder.
# files2 is all the query.html inside the corresponding category folder of the later date folder.
# file2 is the individual query.html file 
# query will be the query term with all the spaces and parenthesis escaped.
# filename is "escapedquery.html"
'''
import serp_scraper
import comparing_serps
import create_serps_and_compare
import os
import sys

def main(date1, date2, category):
    #date1 = '6-8-22'
    #date2 = '6-9-22'
    #f = 'Ace.html'


    files1 = os.listdir(f"../SERP_Collection/{date1}/{category}")
    files2 = os.listdir(f"../SERP_Collection/{date2}/{category}")
    files1.sort()
    for file2 in files2:
        if not file2.startswith('.') and file2 in files1: # ignores .DStore and checks that the query.html file exists in both /date/category folders
            query = file2[:file2.index('.')].replace(" ", "\ ") # extract the query from query.html then escape the space ' '.
            query = query.replace("(", "\(") # escape the parenthesis '('
            query = query.replace(")", "\)") # escape the parenthesis ')'
            filename = "\"" + query+".html" + "\""
            os.system(f'python create_serps_and_compare.py {date1} {date2} {category} {filename}') 
            # date1 is the earlier date, date2 is the later date, category is the corresponding category of the query (e.g. identities), filename is the "escapedquery.html"

'''
Driver that orders the date folders and calls the main method with all the date pairs
# folders are all the date folders; folder is the individual date folder.
# categories_date1 are all the category folders inside the specified earlier date
# categories_date2 are all the category folders inside the specified later date
'''
if __name__ == "__main__":
    folders = os.listdir('../SERP_Collection')
    folders.remove(".DS_Store")

    # orders the date folders
    datesList = []
    for folder in folders:
        dateComponents = folder.split("-")
        datesList.append({'month':int(dateComponents[0]), 'day':int(dateComponents[1]), 'year':int(dateComponents[2])})
    datesList = sorted(datesList, key=lambda x: (x['year'], x['month'], x['day']),reverse=True)
    sortedDates = []
    for d in datesList:
        sortedDates.append(str(d['month'])+'-'+str(d['day'])+'-'+str(d['year']))
    folders = sortedDates 

    # calls the main method with all date pairs (and all the categories inside the date folder that appeared in both dates)
    for i in range(0,len(folders)-1):
        categories_date1 = os.listdir(f'../SERP_Collection/{folders[i+1]}')
        categories_date2 = os.listdir(f'../SERP_Collection/{folders[i]}')
        for category in categories_date2: # Go through all the categories
            if not category.startswith('.') and category in categories_date1: # igmore .DStore and make sure the category folder is in both of the date folders.
                print(folders[i+1] + " " + folders[i], category)
                main(folders[i+1], folders[i], category) #folders[i+1] is the earlier date, folders[i] is the later date
                #main("6-8-22", "6-9-22")
