
import requests

def run_translation_task():
    print("[AUREA] Iniciando tarefa de tradução...")
    text = "A inteligência artificial está mudando o mundo."
    source_lang = "pt"
    target_lang = "en"
    translated = translate_google(text, source_lang, target_lang)
    print(f"[AUREA] Tradução: {translated}")

def translate_google(text, source, target):
    try:
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source}&tl={target}&dt=t&q={text}"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()[0][0][0]
            return result
        else:
            print("[AUREA] Erro na API do Google. Código:", response.status_code)
            return "[Falha na tradução]"
    except Exception as e:
        print(f"[AUREA] Erro durante a tradução: {e}")
        return "[Erro ao traduzir]"
