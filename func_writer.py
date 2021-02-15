"""
Esta função faz a leitura do Dataset, manipula os dados e faz a escrita do arquivode saida.csv.
Parametros de entrada: (dataset_name, arquivo_saida, target_group, delimiter_charac, tipo_escrita, quote_sys)
"""

def func_escrita(dataset_name, arquivo_saida, target_group, delimiter_charac
                 , param1, param2, param3, param4, tipo_escrita, quote_sys):
    import csv
    from func_catch_headers import header_index
    from func_catch_inicio_fim import inicio_fim_index

    #  Inicialização de variáveis
    # Cuidado c/ "IndexError: list index out of range" nem todas as tabelas são do mesmo tamanho
    dic1 = header_index(dataset_name, target_group)
    # Incío Blk posição inicio_fim_blk[0] e fim inicio_fim_blk[1]
    inicio_fim_blk = inicio_fim_index(dataset_name, target_group)
    #i = 0  # Contador de Linha nula
    line_count = 0  # Contador de linha
    header_count = 0
    list_out = []
    with open(arquivo_saida, mode='a') as database_file:
        database_writer = csv.writer(database_file, delimiter=delimiter_charac, quotechar='"', quoting=quote_sys, lineterminator='\n')
        ...
        with open(dataset_name, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter_charac)  # separe por vírgula ou ponto e vírgula
            for line in spamreader:
                linha = line  # line é uma variável do tipo lista, com os campos das tabelas
                result = str(linha).find("End of Block")  # Transf. linha->string e verif. ocor. seq. str "End of Block"
                if line_count <= 2 and tipo_escrita == 0:  # Primeiras três linhas da B.D.
                    database_writer.writerow(line)
                if line_count == (inicio_fim_blk[0] - 1) and tipo_escrita == 0:  # Primeiro Cabeçalho Grupo de dados
                    database_writer.writerow(line)
                if line_count == inicio_fim_blk[0] and tipo_escrita == 0:  # Segundo cabeçalho do Grupo de dados
                    database_writer.writerow(line)
                if target_group in line and tipo_escrita == 1:  # Bloco de Dados alvo customiz. está aqui
                    ...  # func_customize deve ser chamada aqui p/ customizar os dados do grupo alvo
                    #database_writer.writerow(line)  # Escreve linha original sem customização
                    # End. campos alvo conv.: line[dic1["Grupo"]], line[dic1["Column1"]], line[dic1["Column2"]]...
                    if param1 == 1:
                        list_out.append(line[dic1["Grupo"]])
                    if param2 == 1:
                        list_out.append(line[dic1["Coluna1"]])
                    if param3 == 1:
                        list_out.append(line[dic1["Coluna2"]])
                    if param4 == 1:
                        list_out.append(line[dic1["Coluna3"]])
                    print(list_out)
                    database_writer.writerow(list_out)  # Escreve linha customizada
                    list_out = []
                    #print(line[dic1[param1]], line[dic1[param2]], line[dic1[param3]], line[dic1[param4]])
                if result > 0 and tipo_escrita == 2:  # Escrita do rodapé da B.D.
                    database_writer.writerow([])
                    database_writer.writerow(line)
                line_count += 1


# func_chamada_escrita gera as tuplas de escrita, c/ var. parâmetros tipo_escrita e quote_sys
def func_chamada_escrita(input_param_list):
    print(*input_param_list)
    ...
    tuplas_escritas = ((0, 0), (1, 1), (2, 0))
    for i in range(3):
        func_escrita(*input_param_list, *tuplas_escritas[i])


# Para Teste da Função
# Sequencia de escrita- (0,0) - Esc. Cabeçalhos, (1,1) - Esc. Bloco Dados (2,0) - Escreve rodapé
# Parametros de entrada
# dataset_name = "xxxx.csv"  # Conjunto de dados para estudo
# arquivo_saida = "C:/Users/User/Documents/arquivosaida.csv"  # Espec. caminho diretório saída e nome arquivo
# target_group = "Games"  # Grupo alvo da captura
# tipo_escrita = 1  # 0= Escreve Cabeçalho, 1= Escreve Bloco de dados, 2= Escreve Rodape
# quote_sys = 0  # 0=csv.QUOTE_MINIMAL, 1=csv.QUOTE_ALL
# # Lista de parametros de entrada
# input_param_list = (dataset_name, arquivo_saida, target_group, delimiter_charac)
# func_chamada_escrita(input_param_list)