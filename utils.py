import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        quote = quote.lower()
        base = base.lower()
        if quote == base:
            raise APIException(f'Невозможно привести одинаковые валюты {base}')

        try:
            quote_tinker = keys[quote]
        except:
            raise APIException(f'Неудалось обработать валюту {quote}')
        
        try:
            base_tinker = keys[base]
        except:
            raise APIException(f'Неудалось обработать валюту {base}')
        
        try:
            amount = float(amount)
        except:
            raise APIException(f'Неудалось обработать кол-во {amount}')
        
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_tinker}&tsyms={base_tinker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base*amount