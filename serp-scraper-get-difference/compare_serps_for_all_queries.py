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
        if not file2.startswith('.') and file2 in files1:
            query = file2[:file2.index('.')].replace(" ", "\ ")
            query = query.replace("(", "\(")
            query = query.replace(")", "\)")
            filename = "\"" + query+".html" + "\""
            os.system(f'python create_serps_and_compare.py {date1} {date2} {category} {filename}')
    #     if not file.startswith('.'):
    #         #file.replace(' ', )
    #         query = file[:file.index('.')].replace(" ", "\ ")
    #         query = query.replace("(", "\(")
    #         query = query.replace(")", "\)")
    #         filename = "\"" + query+".html" + "\""
    #         #print(" ", date1, date2, filename)
    #         #print(filename)
    


if __name__ == "__main__":
    folders = os.listdir('../SERP_Collection')
    folders.remove(".DS_Store")

    datesList = []
    for folder in folders:
        dateComponents = folder.split("-")
        datesList.append({'month':int(dateComponents[0]), 'day':int(dateComponents[1]), 'year':int(dateComponents[2])})
    datesList = sorted(datesList, key=lambda x: (x['year'], x['month'], x['day']),reverse=True)
    sortedDates = []
    for d in datesList:
        sortedDates.append(str(d['month'])+'-'+str(d['day'])+'-'+str(d['year']))
    folders = sortedDates 

    for i in range(0,len(folders)-1):
        categories_date1 = os.listdir(f'../SERP_Collection/{folders[i+1]}')
        categories_date2 = os.listdir(f'../SERP_Collection/{folders[i]}')
        for category in categories_date2:
            if not category.startswith('.') and category in categories_date1:
                print(folders[i+1] + " " + folders[i], category)
                main(folders[i+1], folders[i], category)
                #main("6-8-22", "6-9-22")
