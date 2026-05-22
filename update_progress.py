#!/usr/bin/env python3
"""
Atualiza automaticamente a porcentagem do badge no README.md
com base na data atual entre o início e o fim do curso.
"""

from datetime import date
import re

START_DATE = date(2026, 2, 9)   # 09/02/2026
END_DATE   = date(2028, 12, 14) # 14/12/2028

def calc_progress() -> float:
    today = date.today()
    if today <= START_DATE:
        return 0.0
    if today >= END_DATE:
        return 100.0
    total = (END_DATE - START_DATE).days
    elapsed = (today - START_DATE).days
    return round((elapsed / total) * 100, 1)

def update_readme(progress: float):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Substitui o valor de progress=XX% na URL do badge
    updated = re.sub(
        r"(github-readme-educational-badge[^\"']*progress=)[^&\"'%]+(%25|%)",
        rf"\g<1>{progress}\2",
        content,
    )

    # Fallback: substitui progress=XX sem encode
    if updated == content:
        updated = re.sub(
            r"(progress=)[\d.]+",
            rf"\g<1>{progress}",
            content,
        )

    if updated == content:
        print("⚠️  Padrão de progress não encontrado no README. Verifique a URL do badge.")
        return

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated)

    print(f"✅ README.md atualizado com progress={progress}%")

if __name__ == "__main__":
    progress = calc_progress()
    print(f"📅 Progresso calculado: {progress}%")
    update_readme(progress)
