from aiohttp import web
import json
import asyncio
import asyncpg


async def add_project_handler(request):
	
	#async def run():
    #conn = await asyncpg.connect(user='user', password='password', database='database', host='127.0.0.1')
    #values = await conn.fetch('''SELECT * FROM mytable''')
    #await conn.close()

    data = await request.json()

    print(data["token"])
	
	#name
	#token
	#twitter
	#linkedin
	#active in portfolio
    response_obj = { 'status' : 'added' }
    return web.Response(text=json.dumps(response_obj))



async def get_project_handler(request):
	#name
	#token
	#twitter
	#linkedin
	#active in portfolio
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))

