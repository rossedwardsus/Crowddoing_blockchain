COIN_LIST_PATH = "coins.csv"  # Path for file containing the list of coins
COIN_LIST_URL = "https://min-api.cryptocompare.com/data/all/coinlist"  # URL of CryptoCompare API for coin list
COIN_HISTO_URL = "https://min-api.cryptocompare.com/data/histohour"  # URL of CryptoCompare API for historical data


def get_crypto_list():
    """
    Uses the CryptoCompare API to retrieve a list of cryptocurrencies.
    Docs: https://www.cryptocompare.com/api/#-api-data-coinlist-
    """
    try:
        page = requests.get(COIN_LIST_URL)
        data = page.json()
        coins = list()

        # If response is successful
        if data['Response'] == "Success":
            print("Parsing coin list from CryptoCompare. Please wait...")
            
            full_data = data['Data']
            df = pd.DataFrame(data['Data'])
            df.to_csv(COIN_LIST_PATH)
            display(df.head())
            
            print("Successfully extracted list of cryptocurrencies in {}".format(COIN_LIST_PATH))
    except Exception as ex:
        print("Problem communicating with CryptoCompare API. Reason {}".format(str(ex)))
        exit()



def main():
	get_crypto_list()