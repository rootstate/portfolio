# Dockerised Portfolio Stack
A small in progress stie that demonstrates the following:
* **FastAPI** backend -> JSON API, Redis powered visit counter
* **Nginx** static frontend -> just plain HTML + a touch of jQuery
* **Docker Compose** orchestrataion -> seperate Dockerfiles for front/backend

---
## Quick start guide
> **What you need:** Docker desktop with Compose v2 + Compose Watch

```bash
# clone and enter the dir
git clone https://github.com/rootstate/portfolio.git

# First run/build
docker compose up --build
```
**Note:**
* Frontend is exposed to port 3000
* Backend is exposed to 8000 (JSON return)

## API functionality so far
* GET - /status - liveness probing
* GET - /api/counter - Auto inrementing Redis key (returns {"visits": N}

## Licens
MIT - do whatever you want, i dont care :)

## Note from author
Make sure to check in regularly, will keep iterating and adding functionality until hosting (probably AWS). Hope to see you again :)
