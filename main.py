# main.py
from fastapi import FastAPI

# 1. Cria a instância principal do FastAPI
app = FastAPI()

# 2. Define uma rota (endpoint) para a raiz ("/")
#    @app.get diz ao FastAPI que esta função responde a requisições GET
@app.get("/")
def ler_raiz():
    return {"message": "Olá, mundo! Esta é minha API para o app Android."}

# 3. Define outra rota
@app.get("/items/{item_id}")
def ler_item(item_id: int):
    return {"item_id": item_id, "descricao": "Este é um item de exemplo."}