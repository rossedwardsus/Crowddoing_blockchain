#follower count and screen names
#retweets over time

from aiohttp import web
import json
import asyncio
import asyncpg


async def get_project_twitter_follower_count_over_time_handler(request):
	
	#async def run():
    #conn = await asyncpg.connect(user='user', password='password', database='database', host='127.0.0.1')
    #values = await conn.fetch('''SELECT * FROM mytable''')
    #await conn.close()

	
	#name
	#token
	#twitter
	#linkedin
	#active in portfolio
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))



async def get_project_twitter_retweet_count_over_time_handler(request):
	#name
	#token
	#twitter
	#linkedin
	#active in portfolio
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

