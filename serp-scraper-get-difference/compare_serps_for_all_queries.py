import serp_scraper
import comparing_serps
import create_serps_and_compare
import os
import sys

def main(date1, date2):
    #date1 = '6-8-22'
    #date2 = '6-9-22'
    #f = 'Ace.html'

    # query = filename.split('.')[0]

    # os.system(f'python serp_scraper.py {date1} {filename}')
    # os.system(f'python serp_scraper.py {date2} {filename}')

    # path_to_serps = 'for_comparing_serps'
    # f1 = f'{path_to_serps}/{date1}_{filename.split(".")[0]}.json'
    # f2 = f'{path_to_serps}/{date2}_{filename.split(".")[0]}.json'
    # date1, date2, filename
    #date1 = "6-8-22"
    #date2 = "6-9-22"
    files = os.listdir("../SERP_Collection/6-8-22")
    files.sort()
    for file in files:
        if not file.startswith('.'):
            #file.replace(' ', )
            query = file[:file.index('.')].replace(" ", "\ ")
            query = query.replace("(", "\(")
            query = query.replace(")", "\)")
            filename = "\"" + query+".html" + "\""
            #print(" ", date1, date2, filename)
            #print(filename)
            os.system(f'python create_serps_and_compare.py {date1} {date2} {filename}')


if __name__ == "__main__":
    folders = os.listdir('../SERP_Collection')
    folders.remove(".DS_Store")
    #print(folders)
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
        print(folders[i+1] + " " + folders[i])
        main(folders[i+1], folders[i])
        print()
    #main("6-8-22", "6-9-22")
