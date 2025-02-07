import geopy.distance
from geopy.geocoders import Nominatim
import pycep_correios
from pycep_correios import exceptions


def titulo_menu2(txt):
    print(linha_menu2())
    print(txt.center(180))


def linha_menu2():
    return "-" * 180


def titulo(txt):
    print(linha())
    print(txt.center(57))
    print(linha())


def sub_titulo(txt):
    print(linha_subtitulo())
    print(txt.center(105))
    print(linha_subtitulo())


def linha_subtitulo():
    return "-" * 105


def linha():
    return "-" * 57


def menu_inicial():
    titulo("MENU PRINCIPAL")
    print('''⎪ [1] - Informações a respeito dos materiais recicláveis ⎪ 
⎪ [2] - Informações a respeito dos pontos de coleta      ⎪
⎪ [3] - Localização dos pontos de coleta                 ⎪
⎪ [4] - Calculadora                                      ⎪
⎪ [5] - Sair                                             ⎪
⎪________________________________________________________⎪
     ''')


def menu_material():
    print('''                __________________________
                ⎪ [1] - Plástico          ⎪  
                ⎪ [2] - Vidro             ⎪                
                ⎪ [3] - Metal             ⎪
                ⎪ [4] - Papel             ⎪
                ⎪ [5] - Pilhas e baterias ⎪
                ⎪ [6] - Voltar            ⎪ 
                ⎪ [7] - Sair              ⎪
                ⎪_________________________⎪               
     ''')


def menu_material2():
    print('''               __________________________
               ⎪ [1] - Plástico          ⎪  
               ⎪ [2] - Vidro             ⎪           
               ⎪ [3] - Metal             ⎪
               ⎪ [4] - Papel             ⎪
               ⎪ [5] - Pilhas e baterias ⎪
               ⎪ [6] - Oleo vegetal      ⎪
               ⎪ [7] - Voltar            ⎪
               ⎪ [8] - Sair              ⎪
               ⎪_________________________⎪              
     ''')


def abrir_arquivo(diretorio):
    arq = open(f"files/{diretorio}", "r", encoding="utf8")
    for line in arq:
        print(line)


def opcao(escolha):
    global p1
    while escolha != "1" and escolha != "2":
        escolha = str(input("Escolha inexistente, por favor insira um número referente ao menu acima "))

    else:
        if escolha == "1":
            cep = str(input("Digite seu CEP "))
            while len(cep) != 8 or cep == "99999999":
                print("CEP Invalido")
                cep = str(input("Digite um cep valido "))

            else:

                try:
                    endereco = pycep_correios.get_address_from_cep(cep)

                except exceptions.InvalidCEP as eic:
                    cep = str(input("CEP inválido, digite novamente "))
                    endereco = pycep_correios.get_address_from_cep(cep)

                except exceptions.CEPNotFound as ecnf:
                    cep = str(input("CEP não encontrado, digite novamente "))
                    endereco = pycep_correios.get_address_from_cep(cep)

                except exceptions.Timeout as errt:
                    print("Erro de conexão, verifique sua conexão com a internet e execute novamente o programa")
                    quit()

                else:
                    locator = Nominatim(user_agent="aps")
                    location = locator.geocode(endereco["logradouro"] + "," + endereco["cidade"] + "," +
                                               endereco["uf"])
                    p1 = (location.latitude, location.longitude)

        else:
            locator = Nominatim(user_agent="aps")
            location = locator.geocode(str(input("Digite seu endereço (EXEMPLO: Av Padre Guilherme Ary, 81,"
                                                 " Campinas - SP) ")))
            while location is None:
                location = locator.geocode(str(input("Endereço inválido, insira outro (EXEMPLO: Av Padre Guilherme "
                                                     "Ary, 81, Campinas - SP):  ")))
            else:
                p1 = (location.latitude, location.longitude)


menu_inicial()



escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))

while escolha_inicial != "5":

    if escolha_inicial != "1" and escolha_inicial != "2" and escolha_inicial != "3" and escolha_inicial != "4" and \
            escolha_inicial != "5":

        escolha_inicial = str(input("Escolha inválida, digite novamente "))

    elif escolha_inicial == "1":

        titulo("MENU DOS MATERIAIS RECICLÁVEIS")
        menu_material()
        escolha_material = str(input("Qual opção deseja escolher do menu acima? "))

        while escolha_material != "7": #WHILE RESPONSAVEL POR MOSTRAR AS INFORMAÇÕES DOS MATERIAIS

            if escolha_material == "1": #TEXTO PLÁSTICO
                sub_titulo("A RECICLAGEM DO PLÁSTICO NO BRASIL")
                abrir_arquivo("plastico.txt")
                break

            elif escolha_material == "2": #TEXTO VIDRO
                sub_titulo("A RECICLAGEM DO VIDRO NO BRASIL")
                abrir_arquivo("vidro.txt")
                break

            elif escolha_material == "3": #TEXTO METAL
                sub_titulo("A RECICLAGEM DO METAL NO BRASIL")
                abrir_arquivo("metal.txt")
                break

            elif escolha_material == "4": #TEXTO PAPEL
                sub_titulo("A RECICLAGEM DO PAPEL NO BRASIL")
                abrir_arquivo("papel.txt")
                break

            elif escolha_material == "5":
                sub_titulo("A RECICLAGEM DAS PILHAS E BATERIAS NO BRASIL")
                abrir_arquivo("baterias.txt")
                break

            elif escolha_material == "6": #ELIF RESPOSAVEL PELA FUNÇÃO "VOLTAR" DO MENU, RETORNA O MENU INICIAL
                menu_inicial()
                escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))
                break

            elif escolha_material == "7": #ELIF RESPOSAVEL POR FECHAR O PROGRAMA
                print("Sair")

            else:
                escolha_material = input("Escolha inválida, digite novamente ")

        if escolha_material == "7":

            titulo("PROGRAMA FINALIZADO")
            quit()

    elif escolha_inicial == "2":

        titulo("MATERIAIS EM PONTOS DE COLETA")
        menu_material2()

        escolha_material2 = str(input("Deseja obter informações dos ecopontos que recolhem qual tipo de material? "))

        while escolha_material2 != "8":

            if escolha_material2 != "1" and escolha_material2 != "2" and escolha_material2 != "3" \
                    and escolha_material2 != "4" and escolha_material2 != "5" and escolha_material2 != "6" \
                    and escolha_material2 != "7":

                escolha_material2 = str(input("Opção inválida, digite novamente "))

            elif escolha_material2 == "1" or escolha_material2 == "2" or escolha_material2 == "3" or \
                    escolha_material2 == "4":

                abrir_arquivo("tabela_geral.txt")
                break

            elif escolha_material2 == "5" or escolha_material2 == "6":

                abrir_arquivo("tabela_especifica.txt")
                break

            elif escolha_material2 == "7":

                menu_inicial()
                escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))
                break

        else:

            titulo("PROGAMA FINALIZADO")
            quit()

    elif escolha_inicial == "3":

        print(linha())
        print('''[ 1 ] - CEP
[ 2 ] - Endereço
                ''')

        escolha = str(input("Como deseja inserir sua localização? "))

        opcao(escolha)

        # Localização dos ecopontos

        lista_latitude = [-22.8172754, -22.9096444, -22.9046067, -22.891067, -22.916885, -22.9102275, -22.9617947,
                          -22.9420215, -22.885851, -22.9773029, -22.9486031, -22.936197]
        lista_longitude = [-47.1018107, -47.0685557, -47.1076838, -47.1041653, -47.0368281, -47.0711608, -47.190478,
                           -47.0309465, -47.1281875, -47.177823, -47.0582585, 47.1207617]

        lista_lat_oleo = [-22.9258933, -22.8942854, -22.89136, -22.9465589, -22.8439297, -22.9051623]

        lista_long_oleo = [-47.08159, -47.0604147, -47.0260114, -47.0314758, -47.1023985, -46.9801448]

        # Lista vazia onde sera inserido a distancia do usuário até os ecopontos

        lista_dist = []

        # Lista com o nome dos ecopontos

        lista_ecoponto = ["Ecoponto Barão Geraldo", "Ecoponto Central", "Ecoponto Jardim Pacaembu",
                          "Ecoponto Jardim Eulina", "Ecoponto Jardim Paranapanema",
                          "Cooperativa de Reciclagem São Bernardo", "Ecoponto Parque Itajaí",
                          "Ecoponto Jardim São Gabriel", "Ecoponto Parque Via Norte", "Ecoponto Vida Nova",
                          "Ecoponto Vila Campos Sales", "Ecoponto Vila União"]

        lista_oleovegetal = ["Tenda Atacado", "Carrefour Cambuí", "Carrefour Iguatemi", "Carrefour Von Zuben",
                             "Tenda Dom Pedro", "Carrefour Dom Pedro"]

        print('''__________________________
⎪ [1] - Plástico          ⎪  
⎪ [2] - Vidro             ⎪                
⎪ [3] - Metal             ⎪ 
⎪ [4] - Papel             ⎪
⎪ [5] - Pilhas e baterias ⎪
⎪ [6] - Óleo Vegetal      ⎪
⎪_________________________⎪
''')

        material = str(input("Deseja obter a informação dos pontos de coleta de qual material? "))

        while material != "1" and material != "2" and material != "3" and material != "4" and material != "5" and \
                material != "6":

            material = str(input("Escolha inválida, digite novamente "))

        else:

            if material == "1" or material == "2" or material == "3" or material == "4":

                lista_dist = []

                y = 0
                while y < len(lista_latitude):
                    dist_ecoponto = geopy.distance.distance(p1, (lista_latitude[y], lista_longitude[y])).km
                    lista_dist.append(dist_ecoponto)
                    y = y + 1
                print(linha())

                print('''[ 1 ] - Ecoponto mais próximo
[ 2 ] - Ecopontos dentro de um determinado raio''')

                funcao = str(input("Qual função deseja realizar? "))

                while funcao != "1" and funcao != "2":

                    funcao = str(input("Função inválida, escolha alguma função presente no menu acima "))

                else:

                    if funcao == "1":

                        # variavel que recebe a posição do valor a cima na lista de distancia

                        posicao = lista_dist.index(min(lista_dist))

                        print("O ecoponto mais próximo de você para o material escolhido é o :", lista_ecoponto[posicao])

                    elif funcao == "2":

                        raio = int(input("A partir de um raio de quantos quilometros deseja listar os pontos de "
                                         "coleta? "))

                        # cria uma lista com todos os valores da lista_dist menores ou igual a 5

                        lista_raio = [x for x in lista_dist if x <= raio]

                        # verifica cada valor de lista_raio na lista_dist para saber seu indice
                        # compara com o indice da lista_ecoponto para pegar o nome dos locais

                        x = 0

                        if lista_raio == []:
                            print("Não possuem ecopontos dentro de um raio de 5 km do seu endereço")
                        else:
                            print(linha())
                            print(f"O(s) ecopontos dentro de um raio de {raio} km do seu endereço são :")
                            while x < len(lista_raio):
                                posicao1 = lista_dist.index(lista_raio[x])
                                print(lista_ecoponto[posicao1])
                                x = x + 1

                    menu_inicial()
                    escolha_inicial = str(input("Qual opção deseja escolher? "))

            else:

                lista_dist = []

                y = 0
                while y < len(lista_lat_oleo):
                    dist_ecoponto = geopy.distance.distance(p1, (lista_lat_oleo[y], lista_long_oleo[y])).km
                    lista_dist.append(dist_ecoponto)
                    y = y + 1

                print(linha())

                print('''[ 1 ] - Ecoponto mais próximo
[ 2 ] - Ecopontos dentro de um determinado raio''')

                funcao = str(input("Qual função deseja realizar? "))

                while funcao != "1" and funcao != "2":

                    funcao = str(input("Função inválida, escolha alguma função presente no menu acima "))

                else:

                    if funcao == "1":

                        # variavel que recebe a posição do valor a cima na lista de distancia

                        posicao = lista_dist.index(min(lista_dist))

                        print("O ecoponto mais próximo de você para o material escolhido é o :", lista_oleovegetal[posicao])

                    elif funcao == "2":

                        raio = int(
                            input("A partir de um raio de quantos quilometros deseja listar os pontos de coleta? "))

                        # cria uma lista com todos os valores da lista_dist menores ou igual a 5

                        lista_raio = [x for x in lista_dist if x <= raio]

                        # verifica cada valor de lista_raio na lista_dist para saber seu indice
                        # compara com o indice da lista_ecoponto para pegar o nome dos locais

                        x = 0

                        if lista_raio == []:
                            print("Não possuem ecopontos dentro de um raio de 5 km do seu endereço")
                        else:
                            print(linha())
                            print(f"O(s) ecopontos dentro de um raio de {raio} km do seu endereço são :")
                            while x < len(lista_raio):
                                posicao1 = lista_dist.index(lista_raio[x])
                                print(lista_oleovegetal[posicao1])
                                x = x + 1

                    menu_inicial()
                    scolha_inicial = str(input("Qual opção deseja escolher? "))

    elif escolha_inicial == "4":

        print('''__________________________
⎪ [1] - Plástico          ⎪  
⎪ [2] - Vidro             ⎪                
⎪ [3] - Metal             ⎪
⎪ [4] - Papel             ⎪
⎪ [5] - Voltar            ⎪
⎪ [6] - Sair              ⎪
⎪_________________________⎪               
             ''')

        material = input('Qual opção você deseja? ')


        while material != "6":


            while material != "1" and material != "2" and material != "3" and material != "4" and material != "5" and material != "6":
                material = input("Escolha inválida, digite um número referente ao menu acima ")

            else:

                if material == "1":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''__________________________
⎪    TIPOS DE PLÁSTICO    ⎪
⎪                         ⎪
⎪ [1] - Garrafa PET       ⎪
⎪ [2] - Plástico diversos ⎪
⎪ [3] - Voltar            ⎪
⎪_________________________⎪
''')

                    plastico = input("Qual tipo de plástico voce possuí? ")

                    while plastico != "3":

                        if plastico != "1" and plastico != "2":
                            plastico = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif plastico == "1":
                            valor = kilo * 0.8
                            print(f"Você receberá por {kilo} quilos de garrafa PET R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break


                        else:
                            valor = kilo * 0.5
                            print(f"Você receberá por {kilo} de plásticos diversos  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "2":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''_______________________
⎪    TIPOS DE VIDRO    ⎪
⎪                      ⎪
⎪ [1] - Branco         ⎪
⎪ [2] - Verde / Marrom ⎪
⎪ [3] - Voltar         ⎪
⎪______________________⎪
''')

                    vidro = input("Qual tipo de vidro voce possuí? ")

                    while vidro != "3":

                        if vidro != "1" and vidro != "2":
                            vidro = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif vidro == "1":
                            valor = kilo * 0.38
                            print(f"Você receberá por {kilo} quilos de vidro branco R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        else:
                            valor = kilo * 0.35
                            print(f"Você receberá por {kilo} quilos de vidro verde / marrom  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "3":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''__________________________
⎪      TIPOS DE METAL     ⎪
⎪                         ⎪
⎪ [1] - Metal             ⎪   
⎪ [2] - Inox              ⎪
⎪ [3] - Alumínio          ⎪
⎪ [4] - Sucata de latinha ⎪
⎪ [5] - Ferro misto       ⎪
⎪ [6] - Voltar            ⎪
⎪_________________________⎪
''')

                    metal = input("Qual tipo de metal você possuí? ")

                    while metal != "6":

                        if metal != "1" and metal != "2" and metal != "3" and metal != "4" and metal != "5":
                            metal = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif metal == "1":
                            valor = kilo * 12
                            print(f"Você receberá por {kilo} quilos de metal R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "2":
                            valor = kilo * 3.5
                            print(f"Você receberá por {kilo} quilos de inox R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "3":
                            valor = kilo * 3.6
                            print(f"Você receberá por {kilo} quilos de alumínio R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "4":
                            valor = kilo * 4.5
                            print(f"Você receberá por {kilo} quilos de sucata de latinha R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        else:
                            valor = kilo * 0.75
                            print(f"Você receberá por {kilo} quilos de ferro misto R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "4":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''_________________
⎪ TIPOS DE PAPEL ⎪
⎪                ⎪
⎪ [1] - Branco   ⎪
⎪ [2] - Mista    ⎪
⎪ [3] - Papelão  ⎪
⎪ [4] - Voltar   ⎪
⎪________________⎪
 ''')

                    papel = input("Qual tipo de papel voce possuí? ")

                    while papel != "4":

                        if papel != "1" and papel != "2" and papel != "3":
                            papel = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif papel == "1":
                            valor = kilo * 0.45
                            print(f"Você receberá por {kilo} quilos de papel branco R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                        elif papel == "2":
                            valor = kilo * 0.2
                            print(f"Você receberá por {kilo} quilos de asparas mista R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                        else:
                            valor = kilo * 0.15
                            print(f"Você receberá por {kilo} quilos de papelão  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                    else:
                        break

                else:

                    menu_inicial()
                    escolha_inicial = input("Escolha uma opção do menu acima ")

                break

        else:
            titulo("PROGRAMA FINALIZADO")
            quit()

    else:
        titulo("PROGRAMA FINALIZADO")
        quit()

else:
    titulo("PROGRAMA FINALIZADO")
    quit()



