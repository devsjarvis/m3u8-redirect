from flask import Flask, redirect
import requests
import re

app = Flask(__name__)

@app.route('/')
def redirecionar_para_m3u8():
    try:
        html = requests.get('https://nossoplayeronlinehd.lat').text
        match = re.search(r'https://777\.nossoplayeronlinehd\.lat/token/[a-z0-9]+/nossoplayer\.m3u8', html)
        if match:
            return redirect(match.group(0), code=302)
        return 'Link .m3u8 não encontrado.', 404
    except Exception as e:
        return f'Erro ao buscar link: {str(e)}', 500
