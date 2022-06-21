import json
import os
import sys

def getClasses(path, date):
    result_classes = {}
    files = os.listdir(path)
    for f in files:
        if not f.startswith('.') and f.startswith(date):
            with open(f'{path}/{f}', 'r') as inFile:
                data = json.load(inFile)
            query = f.split('_')[1].split('.')[0]
            classes = set()
            for d in data:
                if d['type'] not in ['organic', 'unknown']:
                    classes.add(d['type'].replace(' ', ''))
            result_classes[query] = list(classes)
    return result_classes

def main(path, date):
    result_classes = getClasses(path, date)
    if not os.path.isdir("SERP-Components"):
        os.mkdir('SERP-Components')
    
    path1 = f"SERP-Components/components_{date}.json"
    with open(path1, "w") as outfile:
        json.dump(result_classes, outfile)



if __name__ == "__main__":
    path = 'serp-scraper-get-difference/for_comparing_serps'
    #sys.argv[1] - is a path to json files of components for each query, 
    #in this case for_comparing_serps
    #sys.argv[2] - is a date of data collection, ex 6-8-22
    main(path, sys.argv[1])