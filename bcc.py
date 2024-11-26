def processar_arquivo(caminho_arquivo):
    estatisticas_alunos = {}
    estatisticas_assuntos = {}

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                cod_aluno, assunto, gabarito, resposta = linha.split(';')
                cod_aluno = int(cod_aluno)

                if cod_aluno not in estatisticas_alunos:
                    estatisticas_alunos[cod_aluno] = {'acertos': 0, 'erros': 0}
                if resposta == gabarito:
                    estatisticas_alunos[cod_aluno]['acertos'] += 1
                else:
                    estatisticas_alunos[cod_aluno]['erros'] += 1

                if assunto not in estatisticas_assuntos:
                    estatisticas_assuntos[assunto] = {'acertos': 0, 'erros': 0}
                if resposta == gabarito:
                    estatisticas_assuntos[assunto]['acertos'] += 1
                else:
                    estatisticas_assuntos[assunto]['erros'] += 1

    print("Estatísticas por aluno:")
    for aluno, stats in estatisticas_alunos.items():
        total = stats['acertos'] + stats['erros']
        taxa_acerto = (stats['acertos'] / total) * 100
        print(f"Aluno {aluno}: acertou {stats['acertos']}, errou {stats['erros']}, obtendo uma taxa de acerto de {taxa_acerto:.2f}%")

    print("\nEstatísticas por assunto:")
    for assunto, stats in estatisticas_assuntos.items():
        total = stats['acertos'] + stats['erros']
        taxa_acerto = (stats['acertos'] / total) * 100
        print(f"{assunto}: acertou {stats['acertos']}, errou {stats['erros']}, obtendo uma taxa de acerto de {taxa_acerto:.2f}%")

caminho_arquivo = 'entrada.txt'
processar_arquivo(caminho_arquivo)
