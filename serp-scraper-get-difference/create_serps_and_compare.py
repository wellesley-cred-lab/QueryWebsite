'''
This file runs the serp_scraper.py for the query and the two specified dates, then runs compare_serps.py. 
The file is run automatically for all the queries and all possible date pairs.
'''
import serp_scraper
import comparing_serps
import os
import sys

def main(date1, date2, category, filename):
    #date1 = '6-8-22'
    #date2 = '6-9-22'
    #category = 'Queer'
    #f = 'Ace.html'

    query = filename.split('.')[0] # query is the query term without the .html extension

    os.system(f'python serp_scraper.py {date1} {category} {filename}')
    os.system(f'python serp_scraper.py {date2} {category} {filename}')

    path_to_serps = 'for_comparing_serps'
    f1 = f'{path_to_serps}/{date1}_{filename.split(".")[0]}.json'
    f2 = f'{path_to_serps}/{date2}_{filename.split(".")[0]}.json'

    os.system(f'python comparing_serps.py {f1} {f2} {query} {date1} {date2}')

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
