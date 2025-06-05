from flask import Flask, redirect
from playwright.sync_api import sync_playwright
import re

app = Flask(__name__)

@app.route('/')
def redirecionar_para_m3u8():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://nossoplayeronlinehd.lat", timeout=20000)
            page.wait_for_timeout(5000)  # espera 5 segundos
            content = page.content()
            browser.close()

            match = re.search(r'https://777\.nossoplayeronlinehd\.lat/token/[a-z0-9]+/nossoplayer\.m3u8', content)
            if match:
                return redirect(match.group(0), code=302)
            else:
                return '🔴 Link .m3u8 não encontrado na página.', 404
    except Exception as e:
        return f'🔴 Erro ao buscar link: {str(e)}', 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
