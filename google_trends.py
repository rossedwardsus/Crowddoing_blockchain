#schema
#projectid date number


from pytrends.request import TrendReq

pytrend = TrendReq(hl='en-us')

kw_list = ["blockchain"]


pytrend.build_payload(kw_list)

interest_over_time = pytrend.interest_over_time()

print(interest_over_time)