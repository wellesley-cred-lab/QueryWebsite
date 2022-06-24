from bs4 import BeautifulSoup as BS
import json
import os
import sys

def appendIcons(soup, changes, up_icon_src, down_icon_src, disappear_icon_src, appear_icon_src):
    allBlocks = soup.find('div', class_='v7W49e')
    organics = []
    for block in allBlocks.children:
        if block.name == 'div':
            if block.has_attr('class') and block['class'][0] == 'ULSxyf': ## non-organic block
                continue
            else: # organic
                div = block.find('div', class_='yuRUbf')
                cite_domain = block.find('cite')
                domain = cite_domain.text.split()[0]

                if domain in changes['organic']:
                    domain_results = changes['organic'][domain]
                    if domain_results['change_type'] == 'move' and domain_results['change']>0:
                        img_tag = soup.new_tag("img", src = up_icon_src)
                        str_tag = soup.new_tag("a", href = 'https://www.google.com/')
                        str_tag.string = changes['organic'][domain]['change_type']
                        block.append(img_tag)
                        block.append(str_tag)
                    elif domain_results['change_type'] == 'move' and domain_results['change']<0:
                        img_tag = soup.new_tag("img", src = down_icon_src)
                        str_tag = soup.new_tag("a", href = 'https://www.google.com/')
                        str_tag.string = changes['organic'][domain]['change_type']
                        block.append(img_tag)
                        block.append(str_tag)
                    elif domain_results['change_type'] == 'disappear':
                        img_tag = soup.new_tag("img", src = disappear_icon_src)
                        str_tag = soup.new_tag("a", href = 'https://www.google.com/')
                        str_tag.string = changes['organic'][domain]['change_type']
                        block.append(img_tag)
                        block.append(str_tag)
                    elif domain_results['change_type'] == 'appear':
                        img_tag = soup.new_tag("img", src = appear_icon_src)
                        str_tag = soup.new_tag("a", href = 'https://www.google.com/')
                        str_tag.string = changes['organic'][domain]['change_type']
                        block.append(img_tag)
                        block.append(str_tag)
                    else:
                        str_tag = soup.new_tag("a", href = 'https://www.google.com/')
                        str_tag.string = changes['organic'][domain]['change_type']
                        block.append(str_tag)
    return soup

def modifyHTML(date1, date2, query):
    up_icon_src = 'data:image/png;base64,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'
    down_icon_src = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAAXNSR0IArs4c6QAAB5FJREFUWEfFmHtsleUdxz/Pey69UBTMMiCTDHpKS7hs4hQnBYq0FNnFxYjJEnXELCZzifSGkIEOJy4GKZweICb4x5ZliTrdYFHXyaC0YmEhw2FUboXTckmUrVyWctqenvd9n2d53tOet6c9txYSnz/f93l+z/f5Xb+/n1BKKW5hxVD4lY2NB4XEgwRMbJkPHvBi3IJ0EOMB2IdCxG7y4GvH6ekeQGkkqZaSFBRB24uLmVRQiH8cYMcEUKkoi17ez5XrhcBYFW/gET2c2bESrzEhZ63mBNBSkns2NhPpK0Bg5yw83UZLFnB515Kc5GQGqEwu3bRZ9uvDjPJU4QEZQykPP11SwJPfD1A8fSoCycUrPfz5WAe/a+lGGX4wfCCtBCCFgSEsNj81jzULpoLhTQs2LUATxdN72jlyqj/psJTaVFHOBH+I3yNy0oKJzb0b9hPpF6AfNmz5jSingqvw4EspKyVAieKBTXu5GpmYdEhgcmZ7FX5vXk7ARm6yZJSy+hYUviSLGEQ5H/oRIkUQjQaobCp+e5BL3cO0oyw2Pj6dZ5bMHxewkYfCNyJUvXQ06bOhegnvfHSU/FEAD567xjO7P0naeKqxnAJf7pGX7RU6/m27n1n1H7tblcndd+fz8frKZKsNz4MDUlJacwjD0MkWDKE43fgQfo8XRPaEawLaPfI0ApHdP01pU1b3oWNyvYQQfP7KQiYU3ZkAmdCgLigldR8i1ZATK/ZuXMiCKZOzKcT5b1omZevbUbbJ3zYvYs5dRTmdk1aEQINrbtPK4+LupXgGH5gAeG0gyn3rDyeEFhYanHy1KqdL9KbShhZMy82RXaHqnM+ue+cEfzl6DVTccr94LMCGpYG4VodMXFx3ACUHq4OSnA1V4Rfp89PI2wN1rUipjQzaGhd2rswZoN44s+ZAojrp0tkZWo6BiAO0ZIyyBn1B3G9W3DuBN9aUj+mCWwU40oJtWx/i2/m+OMCFW96n++pQblN0hlaS3cWT8d8qQFPBbCcG4sEohEVncBVC2X1qZt1HOmYHf0g6mx4ek/b05lsFqGVUvPI+l7rdIhAOVSNsZalATUsC0GtPlvD4/cVfC8D/SYsFdYcSd3eGqhCm3a9m1bnR29m0HDGG4BiSdjs0qOt/qRMs8XXk5SWIiBVT8+pbEx/PB1fgMcbqgbfHxKaKUVrblsDyWMVExPEbplq92VVrV7AKjOxV43anGS1PKkVxbSuCODXL8/UiWi9eU09vP56472sFiKK4xgVo2NcRF6OWqljvBsnZpnL8IjMx+OeNCM/ubOf4puV4vX7ncel8UBeHxa9+wOoV3+W5+7+FN0NNV3aM4oaPdKZ3ZE6ZBsIye1VJQ3tCg+eC1XgzWPh6LMb3ntc+Kxw+cLKxggJvXlqAwyvEs6umsf7h9JTNllFKhgXs67+cjVAypmbWukGiLyz0pSekR7u+4ommzxyAjt+QR1dwEaXrDmPb8VqsFXAhVMmM2jaHEanBGntfscW7NT9Im8JMO0JpvUscOnZUIqSMquJanWbiav3mJC/HfrM8Yx4sqd2HzYSkxi7P28OAdUf8nO4xNErlkgeFlwvBZRkD8M3jYTb9MZy4O9xUrTWoVKC+GSkHiYGArqbsTGRWzXtY5Gd8yNBP0/bTuWsp/kz+pwNkbTMItzfpDK2I1+KOqxFWbnFV+9n2SiZ60zTjg7faKMrq/o499LAMUMOhKt3HZXxMv5TMqTuY2DN3yhXe2/hUHKAtFYHaAwkSbAhJOId6bGIxd90hzDjLSrk6gsvw6dYzy/rOphZuRlyXON+4GI+v0OWD5S/u5cueIRas+Pe2Sib7c+CDShF47l2k964E4dRYhFCEg1WIEW1mKpx9Zj/znm9zemzHhUWU802POGGYIKwxJGU1+3EmPk4keugMLsXwpO5XR15Usvav2EaRAzImJ3F518KcJjGm6md2fRtSxu+1TZvw69X4BnEkdXVvHTnJr/70pfN6RwuGwblgVbrR0ChlbNnbzolLX/H22kfxZ5gWDB3Ut8zfeIDeXnfOk+/r4XTj6oTsUW3nrNp9WMqtJBps547KjOOJbP6V8r9UPBI6yucXet3futXYuRL/MLo8CqBUNoFat/QNaTIcrNS1Y1xYRh7SpOCeF5q5GXHdR7eeZ4JLyB+h+ZSjD0sNUFLbPmKSJTi29UG+kVfEONiYg1EHuyUVc+pczucoAMWnWyu4I390Xk07PHLqYk0rGMn50OOxONlYhc/QmS2HKHfKoYVSNvM3/Iv+gb4khWqCcGLbYiYXTEppnYzjt6i0mdtwAD3RGrUU/Owns3hh2Qw8HokxIpT0hMFUgndO3+ClPUeQjM6FwhB0bCvH69UD0dQr6wBT98pbP/iEPS3XMwjRxhPE1J34jR4n1Sgj3+mzhYg340lLCGZM+g//2PwEviwjkqwAHcFKEVM2D2x4ixsDUxFCZ/yxsm4dYBJh36Sj6cd4cxzh5QYw2WvY9+llGv5wFsv0YBh2Im+mVLGyMHx5rJoPu9csz2moNFzOOAC6x7XxVMzki6v/5ffNX9B8osupQItmT+Pn1WWUB6aDT9eEzMQjU+76P5NnpMF5/YQpAAAAAElFTkSuQmCC'
    disappear_icon_src = 'data:image/png;base64,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'
    appear_icon_src = 'data:image/png;base64,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'

    changes_path = 'serp-scraper-get-difference/changes'
    pathToSerps = 'SERP_Collection'
    changesJsonPath = f'{query}_changebetween_{date1}_and_{date2}.json'
    with open(f'{changes_path}/{changesJsonPath}', 'r') as file_change:
        changesData = json.load(file_change)
        
    previousHtml = open(f'{pathToSerps}/{date1}/{query}.html', 'r')
    htmltext1 = previousHtml.read()
    soup = BS(htmltext1, 'html.parser')
    modified_soup = appendIcons(soup, changesData, up_icon_src, down_icon_src, disappear_icon_src, appear_icon_src)
    
    if not os.path.isdir('SERP_Collection_modified'):
        os.mkdir('SERP_Collection_modified')

    if not os.path.isdir(f'SERP_Collection_modified/{date1}'):
        os.mkdir(f'SERP_Collection_modified/{date1}')
    with open(f'SERP_Collection_modified/{date1}/{query}.html', "w", encoding='utf-8') as file:
        file.write(str(modified_soup))
    
    nextHtml = open(f'{pathToSerps}/{date2}/{query}.html', 'r')
    htmltext2 = nextHtml.read()
    soup = BS(htmltext2, 'html.parser')
    modified_soup = appendIcons(soup, changesData, up_icon_src, down_icon_src, disappear_icon_src, appear_icon_src)
    
    if not os.path.isdir(f'SERP_Collection_modified/{date2}'):
        os.mkdir(f'SERP_Collection_modified/{date2}')
    with open(f'SERP_Collection_modified/{date2}/{query}.html', "w", encoding='utf-8') as file:
        file.write(str(modified_soup))

if __name__ == "__main__":
    modifyHTML(sys.argv[1], sys.argv[2], sys.argv[3])


