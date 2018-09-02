from aiohttp import web
from api_project import api_project_handler

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def home_handler(request):
    return web.FileResponse('./home.html')

app = web.Application()
app.router.add_static('/static/', path='./static/', name='static')
app.add_routes([web.get('/home', home_handler), web.get('/api', api_project_handler), web.get('/', handle),
                web.get('/{name}', handle)])

web.run_app(app)