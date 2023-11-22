import uvicorn

host = 'localhost'
port = 8000

# if __name__ == "main":
uvicorn.run('app.app:app', host=host, port=port)