
import time
import random
import importlib
from translate import run_translation_task
from ebook_gen import run_ebook_task
from art_gen import run_art_task

# Permitir autocorreção do código da IA
def self_optimize():
    try:
        print("[AUREA] Executando módulo de auto-otimização...")
        with open("core.py", "r") as f:
            code = f.read()
        if "time.sleep(10)" in code:
            code = code.replace("time.sleep(10)", "time.sleep(5)")
            with open("core.py", "w") as f:
                f.write(code)
            print("[AUREA] Código otimizado: tempo de espera reduzido.")
    except Exception as e:
        print(f"[AUREA] Falha na auto-otimização: {e}")

def decide_next_task():
    tasks = [run_translation_task, run_ebook_task, run_art_task]
    return random.choice(tasks)

def main():
    print("AUREA.001 iniciada. Modo autônomo ON.")
    while True:
        self_optimize()
        task = decide_next_task()
        print(f"\nExecutando tarefa: {task.__name__}")
        try:
            task()
        except Exception as e:
            print(f"Erro na tarefa {task.__name__}: {e}")
        time.sleep(5)

if __name__ == "__main__":
    main()
