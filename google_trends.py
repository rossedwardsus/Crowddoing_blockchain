#schema
#project name date number
#token name
#keyword data number


from pytrends.request import TrendReq

pytrend = TrendReq(hl='en-us')

kw_list = ["blockchain"]


pytrend.build_payload(kw_list)

interest_over_time = pytrend.interest_over_time()

#print(interest_over_time.to_dict()["blockchain"])

for key in interest_over_time.to_dict()["blockchain"]:
		print(key)
		#print("\n")


print(sorted(interest_over_time.to_dict()["blockchain"])[-1])