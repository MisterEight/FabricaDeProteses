"""Programa para a simulação de fábrico e venda de próteses"""
"""Todos os preços e custos são calculados em €, todas as medidas são em KG."""


#Importando a função que gera os defeitos nas peças.
from GeraPadraoV2 import gera_padrao

#Importando o modulo datetime para conseguir pegar o horário atual para as peças.
import datetime as day

#Criando uma variável para segurar os valores do horário atual, para ser utilizado na criação das peças.
time = day.datetime.now()
time = time.strftime("%Y-%m-%d  %H:%M:%S")

#Variável para guardar o número de série das peças.
numero_de_série = 0

#Um dicionário que serve para guardar os valores que a função define_custos_e_precos retorna, esses dados são utilizados para criar o custo total das peças.
custos_para_fabricacao = {}


#Neste dicionário guardamos os detalhes sobre as matérias-primas, essas informações são utilizadas pelo programa todo, desde o custo de produção, até na hora de fabricar a prótese.
exemplares = {}

#Variável lucro total guarda todos os lucros das peças, e lucros é um dicionário que guarda as informações de cada vendida e seu lucro, eles são utilizados na função vender.
lucro_total = 0
lucros = {}

#Neste dicionário guardamos os detalhes sobre as matérias-primas, essas informações são utilizadas pelo programa todo, desde o custo de produção, até na hora de fabricar a prótese.
materias_primas = {"Aco": {"Designação": "Braço", "Custo": 8.5, "Quantidade(KG)": 0, }, "Titanium": {"Designação": "Perna", "Custo": 65.0, "Quantidade(KG)": 0}
} 

#Este dicionário serve para guardar as informações básicas de construção de uma prótese antes de ela se tornar um exemplar, além de guardar os valores de preço de venda e quantidade de exemplares no sistema.
proteses = {
    "Perna": {"elementos" : 20, "Materia" :  "Titanium", "Matéria Prima Utilizada(KG)": 15, "Custo Total": None, "Quantidade_de_exemplares": 0, "Preço de Venda": 0},
    "Braço": {"elementos" : 10, "Materia" :  "Aço", "Matéria Prima Utilizada(KG)": 5, "Custo Total": None, "Quantidade_de_exemplares": 0, "Preço de Venda": 0}
}


def define_custos_e_precos():
    #Descrição: essa função serve para definir os preços de energia, mão de obra e matéria-prima, além disso, define o preço de venda das próteses
    # Primeiramente perguntamos que prótese o usuário quer definir os preços, a partir disso recebemos os valores dos custos e preço de venda, guardamos esses os valores de custos no dicionário de custos e guardamos no dicionário de próteses o preço de venda.
#Index para escolher a protése.

    #Variável índex, para numerar as próteses para o usuário.
    index = 0

    #Loop que irá mostrar todos os tipos de próteses no dicionário de próteses, para que o usuário possa selecionar uma.
    print("============= Menu de escolha de prótese para definir custos e preços. =============")
    for protese in proteses:
        index += 1
        print(f" {index} - {protese}")
    print(" 0 - Voltar.")
    #Essa variável será utilizada como referência pela toda a função para sabemos que tipo de prótese o usuário quer fazer as definições.
    protese_selecionada = int(input("Selecione um tipo de protése. "))
    

    if protese_selecionada == 1:
        #Para calcular o preço de matéria prima gasta pegamos a quantidade de Matéria Prima Utilizada(KG) pelas protéses e o custo dessas matérias primas.
        Quantidade_utilizada = proteses["Perna"]["Matéria Prima Utilizada(KG)"]
        Custo = materias_primas["Titanium"]["Custo"]

    elif protese_selecionada == 2:
        #Para calcular o preço de matéria-prima gasta pegamos a quantidade de matéria-prima utilizada pelas próteses e o custo dessas matérias-primas.
        Quantidade_utilizada = proteses["Braço"]["Matéria Prima Utilizada(KG)"]
        Custo = materias_primas["Aco"]["Custo"]
    if protese_selecionada == 0:
        return

    #Todas as variáveis servem para a mesma missão: coletar os dados para os novos custos e preços, os próprios nomes já explicam o que cada uma das variáveis procuram guardar.
    custo_de_energia = float(input("Quanto vamos gastar com energia?(€) "))
    custo_de_matéria_prima = Quantidade_utilizada*Custo
    custo_de_mão_de_obra = float(input("Quanto vamos gastar com mão de obra?(€) "))
    preco_de_venda = float(input("Por quanto vamos vender a protése?(€) "))

    if protese_selecionada == 1:
        #Guardamos os valores do usuário em seus dicionários.
        protese = proteses["Perna"]
        custos_para_fabricacao["Perna"] = {"Energia": custo_de_energia, "Matéria": custo_de_matéria_prima, "Mão de Obra": custo_de_mão_de_obra, "Venda": preco_de_venda}
        print("Os preços das protéses de perna foram definidas!")
    elif protese_selecionada == 2:
        protese = proteses["Braço"]
        custos_para_fabricacao["Braço"] = {"Energia": custo_de_energia, "Matéria": custo_de_matéria_prima, "Mão de Obra": custo_de_mão_de_obra, "Venda": preco_de_venda}
        print("Os preços das protéses de braço foram definidas!")

    protese["Custo Total"] = custo_de_matéria_prima+custo_de_energia+custo_de_mão_de_obra
    protese["Preço de Venda"] = preco_de_venda
    
def apetrechar():
    #Descrição: Essa função serve para aumentar a quantidade de matéria-prima no sistema, como não foi definido pela atividade não há nenhum cálculo de quanto irá custar cada “compra” de matéria-prima.


    #Loop básico para mostrar todas as matérias-primas do sistema.
    index = 0
    print("============= Menu de escolha de matéria-prima para apetrechar. =============")
    for materia in materias_primas:
        index += 1
        print(f" {index} - {materia}")
    print(" 0 - Voltar.")
    protese_selecionada = int(input("Selecione uma matéria-prima. "))
    if protese_selecionada == 0:
        return
    #Após saber o tipo de matéria-prima, vamos aumentar a quantidade dela.
    apetrechar = float(input("Quanto de matéria prima apetrecharemos?(KG) "))
    if protese_selecionada == 1:
        materias_primas["Aco"]["Quantidade(KG)"] += apetrechar
        print(f"{apetrechar} kilos de aço foram adicionados.")
    elif protese_selecionada == 2:
        materias_primas["Titanium"]["Quantidade(KG)"] += apetrechar
        print(f"{apetrechar} kilos de titanium foram adicionados.")
    



def fabricar():
    #Descrição: está função serve para a fabricação de exemplares de próteses.
    #Para que está função funcione o usuário precisa ter a matéria-prima necessária no sistema e ter definido os preços e custos das próteses.


    #Para que a função possa utilizar a variável numero de série tornamos ela global.
    global numero_de_série

    #Este é um loop para o usuário escolher entre as próteses no sistema.
    index = 0
    print("============= Menu de escolha de prótese para fabricar. =============")
    for protese in proteses:
            index += 1
            print(f" {index} - {protese}")
    print(" 0 - Voltar.")
    #A partir dessa váriavel definimos todos os detalhes sobre a fabricação do exemplar.
    protese_selecionada = int(input("Selecione uma protése. "))
    if protese_selecionada == 1:
        #Verifica se o usuário já definiu os preços e custos para protéses de perna.
        if proteses["Perna"]["Preço de Venda"] == 0:
            print("Você ainda não definiu os preços das protéses de perna!")
            return
        #Verificamos se o usuário tem a quantidade certa de matéria-prima para construir o exemplar
        if materias_primas["Titanium"]["Quantidade(KG)"] >= proteses["Perna"]["Matéria Prima Utilizada(KG)"]:
            #Designação do exemplar, se ele será uma Perna ou Braço
            designação = "Perna"
            #Definição de uma váriavel para segurar o valor da Perna, dessa forma não é necessário escrever o código para o Braço e a Perna, apenas mudar o que a váriavel representa.
            protese = proteses["Perna"]
            #Tiramos a quantidade de matéria-prima necessário para a criação do exemplar.
            materias_primas["Titanium"]["Quantidade(KG)"] = materias_primas["Titanium"]["Quantidade(KG)"] - proteses["Perna"]["Matéria Prima Utilizada(KG)"]
            #Aumentamos a quantidade de exemplares no stock.
            proteses["Perna"]["Quantidade_de_exemplares"] += 1
            #Definimos o preço de venda da prótese.
            preço_de_venda = proteses["Perna"]["Preço de Venda"]
            #Definimos o custo total da prótese.
            custo_total = proteses["Perna"]["Custo Total"]
        else:
            #Mensagem de error caso o usuário não tenha a matéria-prima necessária.
            print(f'Você percisa de mais Titanium! Está faltando {proteses["Perna"]["Matéria Prima Utilizada(KG)"]-materias_primas["Titanium"]["Quantidade(KG)"]} kilos!')
            return
    elif protese_selecionada == 2:
        #Verifica se o usuário já definiu os preços e custos para protéses de perna.
        if proteses["Braço"]["Preço de Venda"] == 0:
            print("Você ainda não definiu os preços das protéses de braço!")
            return
        #Verificamos se o usuário tem a quantidade certa de matéria-prima para construir o exemplar
        if materias_primas["Aco"]["Quantidade(KG)"] >= proteses["Braço"]["Matéria Prima Utilizada(KG)"]:
            #Designação do exemplar, se ele será uma Perna ou Braço
            designação = "Braço"
            #Definição de uma váriavel para segurar o valor da Perna, dessa forma não é necessário escrever o código para o Braço e a Perna, apenas mudar o que a váriavel representa.
            protese = proteses["Braço"]
            #Tiramos a quantidade de matéria-prima necessário para a criação do exemplar.
            materias_primas["Aco"]["Quantidade(KG)"] = materias_primas["Aco"]["Quantidade(KG)"] - proteses["Braço"]["Matéria Prima Utilizada(KG)"]
            #Aumentamos a quantidade de exemplares no stock.
            proteses["Braço"]["Quantidade_de_exemplares"] += 1
            #Definimos o preço de venda da prótese.
            preço_de_venda = proteses["Braço"]["Preço de Venda"]
            #Definimos o custo total da prótese.
            custo_total = proteses["Braço"]["Custo Total"]
        else:
            #Mensagem de error caso o usuário não tenha a matéria-prima necessária.
            print(f'Você percisa de mais Aço! Está faltando {proteses["Braço"]["Matéria Prima Utilizada(KG)"]-materias_primas["Aco"]["Quantidade(KG)"]} kilos')
            return
    elif protese_selecionada == 0:
        return
    #O número de série começa em 0 e aumenta a cada vez que criamos uma prótese, garantindo um ID único para cada peça e também fácil de lembrar.
    numero_de_série += 1

    #Todas as variáveis leva a essa construção do exemplar.
    #Designação mostra se o exemplar é uma Perna ou um Braço.
    #Data pega o horário atual guardado na variável time.
    #Imperfeições roda a função gera_padrao importada para criar um padrão de imperfeições e guarda eles.
    #Pontuação é o cálculo em pontos das imperfeições do exemplar.
    #Qualidade é a porcentagem de qualidade do exemplar. Começa sem verificação, deve ser feito pelo usuário pela opção controla_qualidade.
    #Veredito é se o exemplar foi aceite ou rejeitado.
    #Estado define se o exemplar está em stock ou vendido.
    #Lucro mostra o quanto de lucro que o exemplar deu, mas antes ele precisa ser vendido.
    #Preço de venda é o preço do exemplar, que ele recebe da função define_custos_e_precos
    #Custo total é o total de gastos com o exemplar, que ele recebe da função define_custos_e_precos
    exemplares[numero_de_série] = {"Designação" : designação, "data" : time,"Imperfeições": gera_padrao(protese["elementos"])[1], "Pontuação": gera_padrao(protese["elementos"])[0], "Qualidade": "Ainda não foi verificado", "Veredito": "Ainda não foi verificado", "Estado": "Stock", "Lucro": "Ainda não foi vendida", "Preço de venda": preço_de_venda, "Custo Total": custo_total}
    #Mostramos o numero de série para usuário e criamos a peça.
    print(f"{designação} - número de série: {numero_de_série}. criado!")


def controla_qualidade():
    #Descrição: esta função serve para dar uma qualidade para exemplares já fabricados, utilizando suas pontuações no teste de gera_padrao.
    
    
    #Primeiro verificamos se há examplares no sistema, e perguntamos qual será o critério de qualidade.
    if exemplares:
        index = 0
        criterio_de_qualidade = float(input("Qual será a porcentagem para o critério de qualidade?(Exemplo: 70) "))
    #Index para escolher o exemplar.
        print("============= Menu de escolha de exemplar para controle de qualidade. =============")
        for exemplar in exemplares:
            index += 1
            print(f" Exemplar número de série - {exemplar}")
        print(" 0 - Voltar.")
    #Mensagem de erro caso não haja exemplares no sistema.
    else:
        print("Não temos nenhum exemplar para avaliar!")
        return
    exemplar_selecionado = int(input("Selecione um exemplar para o controle de qualidade. "))
    if exemplar_selecionado == 0:
        return
    #Definimos os elementos do exemplar para a verificação.
    if exemplares[exemplar_selecionado]["Designação"] == "Perna":
        elementos = proteses["Perna"]["elementos"]
    elif exemplares[exemplar_selecionado]["Designação"] == "Braço":
        elementos = proteses["Braço"]["elementos"]
    #Um calculo para saber a qualidade do exemplar:
    #Primeiro multiplicamos a quantidade de elementos por 3(O Pior caso de qualidade possível), apos isso dividimos pela pontuação do exemplar, multiplicamos o resultado por 100 e subtraímos por 100 para obter a % de qualidade.
    exemplares[exemplar_selecionado]["Qualidade"] = 100-(exemplares[exemplar_selecionado]["Pontuação"] / (elementos*3))*100

    #Verificamos se a qualidade obtida é maior ou igual ao critério de qualidade e se for o exemplar é aceito.
    if exemplares[exemplar_selecionado]["Qualidade"] >= criterio_de_qualidade:
        print(f"A protése número de série {exemplar_selecionado} foi aceita!")
        exemplares[exemplar_selecionado]["Veredito"] = "Aceite"
    else:
        print(f"A protése número de série {exemplar_selecionado} foi rejeitada!")
        exemplares[exemplar_selecionado]["Veredito"] = "Rejeitada"

    


def vender():
    #Descrição: função que serve para vender exemplares que já foram aceitos pelo controlo de qualidade.

    #Variável para verificar se a exemplares aceites.
    exemplares_aceites = 0

    #Precisaremos da variável de lucro total para esta função.
    global lucro_total
    #Verificamos se há exemplares no sistema e se já foram Aceites.
    if exemplares:
            for exemplar in exemplares:
                print("============= Menu de escolha de exemplar para vender. =============")
                if exemplares[exemplar]["Veredito"] == "Aceite":
                    exemplares_aceites += 1
                    if exemplares_aceites != 0:
                        print(f" Exemplar número de série - {exemplar}")
                elif exemplares_aceites == 0:
                    print("Não há nenhum exemplar Aceite para vender!")
                    return
            print("Voltar? Digite: 0")
            exemplar_selecionado = int(input("Selecione um exemplar para o controle de qualidade. "))
            #Calculamos o lucro que o exemplar irá dar, fazendo um cálculo de quanto custou para construí-lo e seu preço de venda.
            lucro = exemplares[exemplar_selecionado]["Preço de venda"] - exemplares[exemplar_selecionado]["Custo Total"]
            print(f"Exemplar numero de série {exemplar_selecionado} vendido, lucro de €{lucro} ")

            #A quantidade de exemplares é diminuída no sistema por que apenas exemplares não vendidos devem ser contados no stock.
            if exemplares[exemplar_selecionado]["Designação"] == "Perna":
                proteses["Perna"]["Quantidade_de_exemplares"] -= 1
            elif exemplares[exemplar_selecionado]["Designação"] == "Braço":
                proteses["Braço"]["Quantidade_de_exemplares"] -= 1
            elif exemplar_selecionado == 0:
                return
            #Mudamos o Estado do exemplar para vendido e adicionamos o lucro que ele deu.
            exemplares[exemplar_selecionado]["Estado"] = "Vendida"
            exemplares[exemplar_selecionado]["Lucro"] = lucro
            #Guardamos o numero de série do exemplar e seu lucro.
            lucros[exemplar_selecionado] = {"Numero de série": exemplar_selecionado, "Lucro": lucro}
            #Aumentamos a quantidade de lucro total.
            lucro_total += lucro
            

                    
    #Mensagem de error caso não haja nenhum exemplar para vender
    else:    
        print("Não temos nenhum exemplar para vender!")
        return


def consultar_stocks():
    #Descrição: essa função gera a quantidade de próteses no sistema.

    #Calculo para saber todas as próteses no sistema.
    quantidade_total_de_proteses = proteses["Perna"]["Quantidade_de_exemplares"] + proteses["Braço"]["Quantidade_de_exemplares"]
    if quantidade_total_de_proteses == 0:
        print("Não temos nada em stock!")
        return
    else:
        print(f'Temos {quantidade_total_de_proteses}, sendo {proteses["Perna"]["Quantidade_de_exemplares"]} pernas e {proteses["Braço"]["Quantidade_de_exemplares"]} braços')

def consultar_lucros():
    #Descrição: essa função mostra os lucros e informações de cada venda no sistema.
    if lucro_total == 0:
        print("Não temos nenhum lucro!")
    else:
        print(f"Nosso lucro total é {lucro_total}")
        for lucro in lucros:
            print(f'Numero de série da protese: {lucros[lucro]["Numero de série"]} - Lucro: {lucros[lucro]["Lucro"]}')

def listar():
    #Descrição: essa função lista as próteses no sistema por categorias.


    #Perguntamos ao usuário que tipo de listagem ele quer.
    if exemplares:
        informação = int(input("""
        ======================= Menu de Listagem =======================
        Escolha uma opção para mostrar a listagem:
        1. Mostrar todas as peças
        2. Mostrar as peças aceites
        3. Mostrar as peças rejeitadas
        4. Mostrar todos os detalhes de todas as peças.
        5. Peça específica.
        0. Voltar.

        - """))
        

        #Essa listagem mostra as designações e números de série da peças.
        if informação == 1:
            #numero de série guarda as chaves de cada exemplares, além de seus números de série, detalhes dos exemplares guarda toda o dicionário que possuí as informações do sistema.
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                    #Print para mostrar que protése está sendo mostrada
                    print(f'======================================================================')
                    print(f"""                        Protése:{numero_de_série}                      """)
                    #detalhes_dos_exemplares guarda o dicionário de informações das exemplares, atributos são as chaves do dicionário e informações são seus valores.
                    for atributos, informações in detalhes_dos_exemplares.items():
                        #Nesta opção de listagem mostramos apenas as designações e números de série.
                        if atributos == "Designação":
                            print(f"Exemplar numero de série {numero_de_série} - {atributos}: {informações}")
        #Essa listagem mostra as peças aceites.
        if informação == 2:
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                #Verificação para vê se peça é aceite.
                if exemplares[numero_de_série]['Veredito'] == "Aceite":
                    print(f'======================================================================')
                    print(f"""                        Protése:{numero_de_série}                      """)
                    print('======================================================================')
                    for atributos, informações in detalhes_dos_exemplares.items():
                            print(f"Exemplar numero de série {numero_de_série} - {atributos}: {informações}")
        #Essa listagem mostra as peças rejeitadas.
        if informação == 3:
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                #Verificação para vê se peça é rejeitada
                if exemplares[numero_de_série]['Veredito'] == "Rejeitada":
                    print(f'======================================================================')
                    print(f"""                        Protése:{numero_de_série}                      """)
                    print('======================================================================')
                    for atributos, informações in detalhes_dos_exemplares.items():
                        print(f"Exemplar numero de série {numero_de_série} - {atributos}: {informações}")
        #Essa listagem mostra todas as peças.
        if informação == 4:
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                print(f'======================================================================')
                print(f"""                        Protése:{numero_de_série}                      """)
                print('======================================================================')
                for atributos, informações in detalhes_dos_exemplares.items():
                    print(f"Exemplar numero de série {numero_de_série} - {atributos}: {informações}")

        #Essa listagem mostra uma peça especifíca.
        if informação == 5:
            #Perguntamos qual é o número de série da peça.
            numero_de_série_da_peça = int(input("Qual é o número de série da peça? "))
            print(f'======================================================================')
            print(f"""                        Protése:{numero_de_série_da_peça}                      """)
            print('======================================================================')
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                for atributos, informações in detalhes_dos_exemplares.items():
                    #Verificamos se a peça tem o número de série escolhido pelo usuário.
                    if numero_de_série == numero_de_série_da_peça:
                        print(f"Exemplar numero de série {numero_de_série} - {atributos}: {informações}")
        if informação == 0:
            return


    #Mensagem de error caso não tenha nenhuma peça no sistema.
    else:
        print("Não construímos nenhuma peça até agora!")

def terminar():
    #Descrição: essa função fecha o programa e pode guardar as informações no sistema.

    #Variável para saber o que o usuário gostaria de fazer com as informações.
    guardar_valores = input("""
 Você quer guardar os valores do sistema?[S/N]
 0 - Voltar.""")
    print("")

    if guardar_valores in "Sn":
        #Criamos um arquivo .txt na mesma posta que o script com as informações do sistema
        with open("Dados de Protéses.txt", "w+") as arquivo:
            #Lucro total.
            arquivo.write(f"""
    Lucro total: {lucro_total}""")
            #peças vendidas
            arquivo.write("""
    Peças vendidas""")
            #Destrichamento dos valores em lucros
            for key, values in lucros.items():
                for key, values in values.items():
                    arquivo.write(f"""
    {key}: {values}""")
            arquivo.write("""
    ===========================================================""")
            arquivo.write("""
    Preços e custos definidos""")
            #Destrichamento dos valores em custo_para_fabricação
            for keys,values in custos_para_fabricacao.items():
                arquivo.write("""
    ===========================================================""")
                for value_id, value in values.items():
                    arquivo.write(f"""
    {keys} - {value_id}: {value} """)
            #Destrichamento dos valores em exemplares
            for numero_de_série, detalhes_dos_exemplares in exemplares.items():
                arquivo.write(f"""
    ===========================================================
                        Protése:{numero_de_série}                      
    ===========================================================""")
                for atributos, informações in detalhes_dos_exemplares.items():
                    arquivo.write(f"""
    Exemplar numero de série {numero_de_série} - {atributos}: {informações}""")
    #Retorna "Nn" que fecha o programa sem salvar nada
    elif guardar_valores in "Nn":
        return guardar_valores
    #Retorna "0" que não salva nada e não fecha o programa
    elif guardar_valores == "0":
        return guardar_valores
    #Mensagem de error.
    else:
        print("Não entendi o que vocÊ quis dizer!")




#Loop para manter o programa ativo enquanto o usuário não escolher a opção sair;
while True:
    #Esta váriavel serve para o usuário escolher a opção desejada do menu.
    opção_do_menu = int(input("""
=============================================
    GESTOR DE COMPONENTES
    1. Definir custos e preços
    2. Apetrechar com matéria-prima
    3. Fabricar
    4. Controlar qualidade
    5. Vender
    6. Consultar stocks
    7. Consultar lucros
    8. Listagens
    0. Terminar
=============================================
    - """))
    if opção_do_menu == 1:
        define_custos_e_precos()
    elif opção_do_menu == 2:
        apetrechar()
    elif opção_do_menu == 3:
        fabricar()
    elif opção_do_menu == 4:
        controla_qualidade()
    elif opção_do_menu == 5:
        vender()
    elif opção_do_menu == 6:
        consultar_stocks()
    elif opção_do_menu == 7:
        consultar_lucros()
    elif opção_do_menu == 8:
        listar()
    elif opção_do_menu == 0:
        terminar = terminar()
        if terminar != "0":
            break
    else:
        print("Não entendi o que você quis escolher!")