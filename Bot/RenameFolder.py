import os


def renomear_pastas():
    caminho_pasta = "C:\\Diretorio\\Aulas"  # Substitua pelo caminho adequado

    for numero_aula in range(24, 98):
        pasta_atual = f"Aula{numero_aula}"
        pasta_nova = f"Aula {numero_aula}"

        pasta_caminho_atual = os.path.join(caminho_pasta, pasta_atual)
        pasta_caminho_nova = os.path.join(caminho_pasta, pasta_nova)

        if os.path.isdir(pasta_caminho_atual):
            os.rename(pasta_caminho_atual, pasta_caminho_nova)
            print(f"Pasta renomeada: {pasta_atual} -> {pasta_nova}")


renomear_pastas()
