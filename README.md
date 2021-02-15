*** Script de Leitura e Escrita de Arquivos csv
===============================================
O objetivo deste script é testar alguns conceitos de manipulação de dados em Python, através da leitura de um dataset no formato csv, aplicação de filtros e escrita no arquivo de saída.

Este Script testa:
 - Interface gráfica com a Biblioteca Tkinter
	- Checkbox
	- Radio Button
	- Button
	- Label
	- Textentry
	- Frame
 	- Centralização da Janela na tela do Desktop
	- Posicionamento dos frames na janela
 - Criação de funções e passagem de parâmetros para funções
 - Manipulação de Dicionários em Python
 - Manipulação de Lsitas em Python
 - Leitura de arquivos .csv / Escrita em arquivos .csv na mesma rotina
 - Documentação do Script para melhor compreensão e manutenção

O Script mantém algumas linhas do arquivo original, que são consideradas como cabeçalhos do dataset e do bloco de dados selecionado.
Na janela principal deve ser selecionado os seguintes parâmetros:
 - Arquivo de entrada
 - Caminho do arquivo de saída, já convertido (Aplicado o filtro)
 - Grupo
 - Parametros selecionados a serem filtrados na escrita do arquivo de saída

Os parâmetros Básicos de entrada são listados abaixo:
 - dataset_name = "study_dataset.csv"  # Conjunto de dados para estudo
 - arquivo_saida = "C:/Users/User/Documents/"  # Espec. caminho diretório saída e nome arquivo
 - target_group = "Games"  # Grupo alvo da captura
 - delimiter_charac  # Caracter Delimitador capturado pela func_delimiter
 - Parâmetros # Parâmetros que farão parte da escrita no arquivo de saida

Todos os 3 primeiros parâmetros precisam ser definidos, senão o script não roda.

Estrutura do Script:
 - main.py  # Interface gráfica com as chamadas para as funções do script

 - func_writer # Faz a leitura e escrita dos dados no arquivo de saida
 - func_catch_headers.py # Esta função captura os endereços dos parâmetros em um dicionário. Retorna nulo se parametro não existe na B.D.
 - func_catch_inicio_fim.py  #Esta função captura o numero da linha que contem o header do parametro alvo
 

Observações importantes a cerca das funções
-------------------------------------------
**func_writer** - Esta função faz a leitura da base de dados original e realiza a escrita dos dados na nova base de dados de saída, com base nos parâmetros selecionados.
Como a estrutura da Base de Dados, possui sistemas de Quoting diferentes, para os cabeçalhos e blocos de dados foi necessário realizar a escrita dos dados de saída, alterando-se dinamicamente o sistema de quoting, em três escritas distintas.
 - quote_sys = 0  # 0=csv.QUOTE_MINIMAL, 1=csv.QUOTE_ALL

O Fluxo de escrita é realizado da seguinte forma:
 - 1 - Passo - Realizar escrita dos cabeçalhos com quoting=csv.QUOTE_MINIMAL (0)
 - 2 - Passo - Realizar a escrita do bloco de dados alvo das conversões, com quoting=csv.QUOTE_ALL (1)
 - 3 - Passo - Finalizar com as duas ultimas linhas da base depois do bloco de dados, com quoting=csv.QUOTE_MINIMAL (0)

O sistema de Quoting precisa mudar entre a escrita dos cabeçalhos e do Bloco de dados

Sequencia de escrita dos dados - (0,0) - Esc. Cabeçalhos, (1,1) - Esc. Bloco Dados (2,0) - Escreve rodapé

Esta sequência é montada na função: **func_chamada_escrita**, que só faz isto e repassa os parâmetros de entrada, recebidos através de uma lista: **input_param_list**, recebida do **Script principal main.py**.

**func_chamada_escrita** - Esta função gera as tuplas de escrita, c/ var. parâmetros de entrada: input_param_list e tabém tipo_escrita e quote_sys.

Parametros selecionados representam os cabeçalhos de algumas colunas que podem ser filtradas. Como esta aplicação é um teste de conceitos, nem todas as colunas estão disponíveis. Grupo, Coluna1, Coluna2 e Coluna3 (Cada Bloco de dados posssui cabeçalhos diferentes, por isto são chamados de colunas na segunda linha de cada cabeçalho).