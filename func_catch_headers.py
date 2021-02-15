"""
Esta função captura os endereços dos parâmetros em um dicionário. Retorna nulo se parametro não existe na B.D.
O dicionário com o Header é utilizado na func_writer para aplicação do filtro/customização de dados
"""
# Teste da função
# dataset_name = "study_dataset.csv"  # Conjunto de dados para estudo
# target_group = "Games"  # Grupo alvo da captura

def header_index(dataset_id, target_grp):
    import csv

    #  Inicialização de variáveis
    delimiter_charac = ";"
    i = 0
    line_count = 0  # Contador de linha
    param_addr = []  # Lista com os Headers
    pline_count = 0
    with open(dataset_id, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=delimiter_charac)  # separe por vírgula ou ponto e vírgula
        for line in spamreader:
            ...
            line_count += 1
            linha = line  # line é uma variável do tipo lista, com os campos das tabelas
            # result = str(linha).find("End of Block")  # Transf. linha em string e verifica ocor. seq. string "End of Block"
            if line_count > 2:  # Começa varredura a partir da terceira linha
                if target_grp in line:
                    for i in range(len(previous_line_target)):
                        param_addr.append(i)
                    dic1 = dict(zip(previous_line_target, param_addr))  # Se o param, busc. ñ existe dics retorna None
                    # Aqui, em pline_count, está o N# da Linha Header de Dados
                    return dic1
                else:
                    ...
                previous_line_target = line
                pline_count += 1  # Pode eliminar func_catch_inicio_fim/No target_grp  está  n# linha Header de Dados



#  Teste da Função
# dic1 = header_index(dataset_name, target_group)
# if dic1:
#      ...
#      print(dic1["Grupo"])
#      print(dic1["Coluna1"])
#      print(dic1["Coluna2"])
# else:
#      ...
#      print("Parâmetro buscado não existe")
# print(dic1)
