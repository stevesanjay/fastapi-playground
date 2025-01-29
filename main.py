from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/reverse", response_class=HTMLResponse)
async def reverse_name(request: Request, name: str = Form(...)):
    reversed_name = name[::-1]
    return templates.TemplateResponse("index.html", {"request": request, "reversed_name": reversed_name})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)