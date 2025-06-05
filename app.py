from flask import Flask, redirect
import requests
import re

app = Flask(__name__)

@app.route('/')
def redirecionar_para_m3u8():
    try:
        response = requests.get('https://nossoplayeronlinehd.lat', timeout=10)
        if response.status_code == 200:
            match = re.search(r'https://777\.nossoplayeronlinehd\.lat/token/[a-z0-9]+/nossoplayer\.m3u8', response.text)
            if match:
                return redirect(match.group(0), code=302)
            else:
                return '🔴 Link .m3u8 não encontrado na página.', 404
        else:
            return f'🔴 Erro ao acessar a página: {response.status_code}', 500
    except Exception as e:
        return f'🔴 Exceção ao buscar link: {str(e)}', 500

