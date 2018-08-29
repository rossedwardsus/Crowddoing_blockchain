import requests

COIN_LIST_PATH = "coins.csv"  # Path for file containing the list of coins
COIN_LIST_URL = "https://min-api.cryptocompare.com/data/all/coinlist"  # URL of CryptoCompare API for coin list
COIN_HISTO_URL = "https://min-api.cryptocompare.com/data/histohour"  # URL of CryptoCompare API for historical data


def get_crypto_list():
   
	try:
		page = requests.get(COIN_LIST_URL)
		data = page.json()
		coins = list()

		#print(str(data["Data"]))

		i = 0

		#print(list(data.keys())[4])

		for key, value in data["Data"].items() :
			print(key, value)
			print("\n\n")

		#while i < len(data):
		#	print(str(data["Data"]))
		#	print("\n\n")
		#	i += 1


        # If response is successful
        #if data['Response'] == "Success":
        #    print("Parsing coin list from CryptoCompare. Please wait...")
            
        #    full_data = data['Data']
        #    df = pd.DataFrame(data['Data'])
        #    df.to_csv(COIN_LIST_PATH)
        #    display(df.head())
            
		print("Successfully extracted list of cryptocurrencies in ")
	except Exception as ex:
		print("Problem communicating with CryptoCompare API. Reason {}".format(str(ex)))
		#exit()



#def main():
#	print("hello")
#	get_crypto_list()


if __name__== "__main__":
  	get_crypto_list()
