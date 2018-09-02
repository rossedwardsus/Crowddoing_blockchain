from aiohttp import web
import json

async def api_project_handler(request):
    response_obj = { 'status' : 'success' }
    return web.Response(text=json.dumps(response_obj))
