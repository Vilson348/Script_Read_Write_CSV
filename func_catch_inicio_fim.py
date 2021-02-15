"""
Esta função captura os numeros das linhas que contem o primeiro e o segundo header do parametro alvo
O endereço do header é utilizado para escrita dos dois cabeçalhos a partir do arquivo original
"""
# Teste da função
# dataset_name = "study_dataset.csv"  # Conjunto de dados para estudo
# target_group = "Games"  # Grupo alvo da captura

def inicio_fim_index(dataset_id, target_grp):
    import csv

    #  Inicialização de variáveis
    delimiter_charac = ";"
    i = 0
    line_count = 0  # Contador de linha
    first_line = 0
    last_line = 0
    inicio_bloco = 0
    x = -1
    with open(dataset_id, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter_charac)  # separe por vírgula ou ponto e vírgula
        for line in spamreader:
            ...
            line_count += 1
            linha = line  # line é uma variável do tipo lista, com os campos das tabelas
            # result = str(linha).find("End of Block")  # Transf. linha em string e verifica ocor. seq. string "End of Block"
            if line_count > 2:  # Começa varredura a partir da terceira linha
                if target_grp in line:
                    if first_line == 0:
                        first_line = line_count - 2
                    last_line = line_count
                if line_count == last_line:
                    inicio_bloco = 1
                if inicio_bloco == 1 and line_count != last_line:
                    return first_line, last_line



# Teste da função
# print(inicio_fim_index(dataset_name, target_group))