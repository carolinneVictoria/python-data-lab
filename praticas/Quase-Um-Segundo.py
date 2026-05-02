import time
import sys

def digitar_frase(frase, velocidade=0.05):
    """Imprime uma frase letra por letra, simulando digitação."""
    for char in frase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(velocidade)
    print()

def reproduzir_letra(frases, pausa_entre_frases=1.0, velocidade=0.05):
    """Reproduz as frases da letra no terminal."""
    print("\n" + "="*50)
    print("🎵  Quase um Segundo — Gal Costa  🎵")
    print("="*50 + "\n")
    time.sleep(1)

    for frase in frases:
        if frase == "":
            print()  # linha em branco entre estrofes
            time.sleep(pausa_entre_frases * 0.5)
        else:
            digitar_frase(frase, velocidade)
            time.sleep(pausa_entre_frases)


frases = [
    "Eu queria ver no escuro do mundo",
    "Aonde está tudo que você quer",
    "Pra me transformar no que te agrada",
    "No que me faça ver",
    "Quais são as cores e as coisas pra te prender",
    "Eu tive um sonho ruim e acordei chorando",
    "Por isso eu te liguei",
    "",
    "Será que você ainda pensa em mim",
    "Será que você ainda pensa em mim...",
]

if __name__ == "__main__":
    reproduzir_letra(
        frases,
        pausa_entre_frases=2.0,   # segundos entre frases
        velocidade=0.08            # velocidade de digitação
    )