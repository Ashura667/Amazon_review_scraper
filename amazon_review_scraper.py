import requests

import bs4
commentaire = []
def function(url, numberofpage):
    agent = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'fr-FR,fr;q=0.9',
        'referer': url,
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/109.0.0.0 Safari/537.36',
    }
    for i in range(1,numberofpage+1):
        req = requests.get(url.replace("#reviews-filter-bar", "&pageNumber="+str(i)), headers=agent)
        soup = bs4.BeautifulSoup(req.text, "html.parser")
        all_element = soup.find_all("span", class_="a-size-base review-text review-text-content")
        for element in all_element:
            commentaire.append(element.find("span").text)

function('https://www.amazon.fr/product-reviews/B00YUIM2J0/ref=acr_dp_hist_5?ie=UTF8&filterByStar=five_star&reviewerType=all_reviews#reviews-filter-bar',5)
for element in commentaire:
    print(element)

fichier = open("avis.csv", "a+", encoding="utf8")
fichier.write("\n".join(commentaire))
