
## Deployment(Full Downloader API)
1.Heroku
```bash
--- Create Procfile
--- Write this code this file: "web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app"
```
2.Render
```bash
--- Create Web Service on Render
--- Start Command: uvicorn app:app --host 0.0.0.0 --port 10000
```
3.Vercel
```bash
--- Create versel.json file
--- Write this:
            {
    "builds": [{
        "src": "app.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "app.py"
        }
    ]
}
```
4.VPS Server
```bash
--- Use this article: 
https://dylancastillo.co/fastapi-nginx-gunicorn/0
```
5.Railway
```bash
--- Create Procfile
--- Write this code this file: "web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT:-5000}"
```


