from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# API stays clean
@app.get("/quote")
def quote():
    return {"status": "OK"}

# Static at /static
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Root path serves the SPA entry point (or remove this if you’re happy with /static)
#@app.get("/")
#def root():
 #   return FileResponse("static/home.html")

#@app.get("/about")
#def root():
#    return FileResponse("static/about.html")

#@app.get("/projects")
#def root():
 #   return FileResponse("static/projects.html")


