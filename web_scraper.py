import requests
article_url="https://www.france24.com/en/middle-east/20250608-israel-orders-military-block-aid-flotilla-carrying-greta-thunberg-gaza-freedom-flotilla-coalition-madleen"
try:
    response=requests.get(article_url)
    response.raise_for_status()
    html_content=response.text
    print("html content sucefully retrieved")
except requests.exceptions.RequestException as e:
    print(f"error retrieving page:{e}")
    html_content=None
     
    