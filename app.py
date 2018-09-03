from aiohttp import web
from api.api_project import get_project_handler, add_project_handler
import logging

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def home_handler(request):
    return web.FileResponse('./home.html')

app = web.Application()
app.router.add_static('/static/', path='./static/', name='static')
app.add_routes([web.get('/home', home_handler), web.post('/api/project/add', add_project_handler), web.get('/api/project', get_project_handler), web.get('/', handle),
                web.get('/{tail:.*}', home_handler)])


logging.basicConfig(level=logging.DEBUG)

web.run_app(app)