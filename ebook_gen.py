
from datetime import datetime

def run_ebook_task():
    print("[AUREA] Iniciando criação de e-book...")
    title = "7 Hábitos para uma Mente Focada"
    content = generate_content()
    filename = f"ebook_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{title}\n\n{content}")
    print(f"[AUREA] E-book salvo como {filename}")

def generate_content():
    sections = [
        "Acordar cedo com propósito",
        "Eliminar distrações digitais",
        "Alimentação e foco mental",
        "Respiração e meditação consciente",
        "Priorizar uma tarefa por vez",
        "Cuidar do sono",
        "Cultivar silêncio e reflexão diária"
    ]
    content = ""
    for i, section in enumerate(sections, 1):
        content += f"{i}. {section}\n"
        content += "   Texto gerado com IA explicando o hábito...\n\n"
    return content
