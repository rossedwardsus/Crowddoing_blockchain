from __future__ import print_function
import os
import requests
#from bs4 import BeautifulSoup
import csv
import time
import json

RESULTS = "results.csv"
URL = "https://api.blockcypher.com/v1/eth/main/addrs/738d145faabb1e00cf5a017588a9c0f998318012"

def main():
    resp = requests.get(URL)
    #sess = requests.Session()

    print(str(resp.json()["txrefs"]))

    for tx in resp.json()["txrefs"]:
    	print(str(tx))

    #parsed = json.loads(str(resp.json()))
    #print(json.dumps(parsed, indent=4, sort_keys=True))

    #with open(RESULTS, 'wb') as f:
    #    wr = csv.writer(f, quoting=csv.QUOTE_ALL)
    #    wr.writerow(map(str, "Rank Address Quantity Percentage".split()))
    #    page = 0
    #    while True:
    #        page += 1
    #        data = getPage(sess, page)

            # Even pages that don't contain the data we're
            # after still contain a table.
    #        if len(data) < 4:
    #            break
    #        else:
    #            for row in data:
    #                wr.writerow(row)
    #            time.sleep(1)

if __name__ == "__main__":
    main()