#Projeto EP1 - Jogo de Gabriel Yamashita e Luis Felipe

import random
atk=random.randint(1,5)
atk_ninja = random.randint(1,5)
vida=10
vida_ninja=10
vida_bi=10
vida_raul=12

def sexto_andar():
    if n_profs >= 3:
        print("- 6 andar (0 min)")
        
def acesso_raul():
    if n_profs == 3:
        print("Parabéns {0}! Agora que você conseguiu encontrar 3 dos 4 professores o 6° andar foi liberado para você como fase final. Porém você pode continuar explorando e tentando encontrar os 2 outros professores, mas o tempo continua correndo.".format(name))

def tempo_restante(cont_tempo):
    y=150-cont_tempo
    if y < 0:
        return 0
    else:
        return y

print("------------------------------------")
print("Digite 'Iniciar' para iniciar o jogo")
print("------------------------------------")
start=input('Digite aqui: ')
while start != "Iniciar":
    print("Inválido")
    start=input("Digite Novamente: ")

name=input("Digite seu nome: ")

print("")
print("----------------------------------------------")
print("Bom dia {0}!".format(name))
print("Você deixou para última hora para entregar o seu EP e agora tem que correr atrás do prejuízo. Para isso você precisa encontrar o Raul (Professor da matéria) e conseguir um adiamento para a entrega, para isso você terá que encontrar 3 dos outros 4 professores das outras matérias (GDE, ModSim, Instrumed e NatDes), e caso você encontre todos ganhará um bônus. Agora são 15:30 e você terá ate as 18:00, ou seja, 150 minutos para achar o Raul.")

begin=input("Você está pronto? ")

while begin != 'sim' and begin != 'Sim':
    
    if begin != 'Sim' or begin != 'sim':
        print("Digite 'Sim' quando estiver")
    begin=input("Você está pronto? ")

n_profs=0
cont_tempo=0

cont_win=0

cont_biblioteca=0
cont_helpdesk=0
cont_sala1=0
cont_sala2=0
cont_cafe=0
cont_sala1m=0
cont_sala2m=0
cont_games=0
cont_lab=0
cont_entidades=0
cont_restaurante=0

game_on = False 
first_time = True

while game_on == False:
    
    if first_time:
        print("")
        print("-----------------")
        print("Entrada do Insper:")
        print("-----------------")
        print("Você está na entrada do Insper e pode escolher dentre as opções a seguir:")
        print("")
        print("- Entrar (0 min)")
        print("- Sair (10 min)")
        print("")
        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
        
        entrada=input("Opção: ")
        
        while entrada != 'Entrar' and entrada != "Sair":
            print("Inválido!")
            entrada=input("Digite Novamente: ")
        
        first_time = False
         
    elif not first_time:
        
        entrada = "Entrar"
        
    
    if entrada == "Entrar":
        
        cont_tempo+=0
        
        print("")
        print("-----------------")
        print("Saguão da Entrada:")
        print("-----------------")  
        print("Agora que você entrou no saguão do Insper você pode escolher duas opções:")
        print("")
        print("- Biblioteca (5 min)")
        print("- Elevadores (0 min)")
        print("")
        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
        
        escolha1=input("Opção: ")
        
        while escolha1 != 'Biblioteca' and escolha1 != 'Elevadores':
            print("Inválido")
            escolha1=input("Opção: ")
            
        if escolha1 == 'Biblioteca':
            
            if cont_biblioteca >= 1:
                
                print("")
                print("Você ja entrou nessa sala!")
            
            else:
            
                cont_biblioteca+=1
                cont_tempo+=5
                
                print("")
                print("----------")
                print("Biblioteca")
                print("----------")
                print("Oh não.. Você encontrou um veterano! Você pode escolher dentre as opções abaixo:")
                print("")
                print("- Lutar (5 min)")
                print("- Voltar para a Entrada (10 min)")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                biblioteca=input('Opção: ')
                
                while biblioteca != 'Lutar' and biblioteca != 'Voltar para a Entrada':
                    print("Inválido")
                    biblioteca=input("Opção: ")
                
                if biblioteca == "Lutar":
                    
                    cont_tempo+=5
                    
                    print("")
                    print("--------")
                    print("Veterano")
                    print("--------")
                    print("sua vida é {0} e a vida do veterano é {1}".format(vida,vida_bi))
                    print("seu ataque é de {0}".format(atk))
                    print("")
                    print("Agora faça sua escolha:")
                    print("")
                        
                    luta_bi="Lutar"
                        
                    while vida_bi>0 or luta_bi=="Lutar":
                        
                        
                        print("- Lutar")
                        print("- Fugir")
                        print("")
                                
                        luta_bi=input("Opção: ")
                                
                        while luta_bi != "Lutar" and luta_bi != "Fugir":
                            print("Inválido!")
                            luta_bi=input("Digite Novamente: ")
                                
                        if luta_bi == "Lutar":
                            vida-=atk_ninja
                            vida_bi-=atk
                            
                            if vida < 0:
                                vida = 0
                            if vida_bi < 0:
                                vida_bi = 0
                            if vida == 0 and vida_bi > 0:
                                print("perdeu")
                                break
                            if vida > 0 and vida_bi == 0:
                                print("ganhou")
                                print("Você ganho um item, enquanto ele estava atordoado")
                                print("Casaco do Insper: te dá mais 2 de vida")
                                vida+=2
                                break
                            print("Sua vida é {0} e a vida do veterano é {1}".format(vida,vida_bi))
                        
                        if luta_bi == "Fugir":
                            print("Essa foi por pouco! Tome mais cuidado da proxima vez!")
                            break
                    print("Sua vida agora é {0}".format(vida))
                    
                    
                if biblioteca == "Voltar para a Entrada":
                    
                    cont_tempo+=10
                        
        elif escolha1 == 'Elevadores':
            
            cont_tempo+=0
            
            print("")
            print("--------")
            print("Elevador")
            print("--------")
            print("Você pode escolher entre 4 andares abaixo:")
            print("")
            print("- 2 andar (1 min)")
            print("- 3 andar (1 min)")
            print("- 4 andar (1 min)")
            print("- 5 andar (1 min)")
            sexto_andar()
            print("")
            print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
            print("")
            
            numero_andar=input('Opção: ')
            
            while numero_andar != "2 andar" and numero_andar != "3 andar" and numero_andar != "4 andar" and numero_andar != "5 andar" and numero_andar != "6 andar":
                print("Inválido!")
                numero_andar=input('Digite Novamente: ')
            
            if numero_andar == "2 andar":
                
                cont_tempo+=1
                
                print("")
                print("-------")
                print("2 Andar")
                print("-------")
                print("Agora que você entrou no 2° andar você tem algumas opções para escolher.")
                print("(As salas 1 e 2 são aleatórias, em uma terá um mini Boss e na outra terá um prêmio)")
                print("")
                print("- Help Desk (1 min)")
                print("- Sala 1 (30 min)")
                print("- Sala 2 (30 min)")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                escolha2andar=input("Opção: ")
                
                while escolha2andar != "Help Desk" and escolha2andar != "Sala 1" and escolha2andar != "Sala 2":
                    print("Inválido!")
                    escolha2andar=input("Digite Novamente: ")
                
                if escolha2andar == "Help Desk":
                    
                    if cont_helpdesk >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_helpdesk=1
                        cont_tempo+=1
                        
                        print("")
                        print("---------")
                        print("Help Desk")
                        print("---------")
                        print("Atendente: Bom dia {0}!".format(name))
                        print("Atendente: Aqui é um lugar do Insper em que ajudamos qualquer um, como estamos cientes que hoje você precisa entregar o seu EP e precisa falar com o Raul daremos a você uma dica de onde um dos professores está.")
                        print("Atendente: A dica é que as vezes o Victor (professor de NatDes) está comendo la no Restaurante do 5° andar.")
                        print("Atendente: Boa sorte nesta jornada!")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        
                elif escolha2andar == "Sala 1":
                    
                    if cont_sala1 >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_sala1+=1
                        cont_tempo+=30
                        cont_tempo-=10
                        
                        print("")
                        print("------")
                        print("Sala 1")
                        print("------")
                        print("Você entrou na Sala 1 e deperou-se com um prêmio!")
                        print("Parabéns você ganhou um salto no tempo!")
                        print("Você conseguiu mais 10 minutos para achar o Raul.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                    
                elif escolha2andar == "Sala 2":
                    
                    if cont_sala2 >=1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_sala2+=1
                        cont_tempo+=30
                        
                        print("")
                        print("------")
                        print("Sala 2")
                        print("------")
                        print("")
                        print("-----")
                        print("Ninja")
                        print("-----")
                        print("Oh não...Você encontou um ninja!")
                        print("Agora você terá que lutar conta ele.")
                        print("")
                        print("sua vida é {0} e a vida do ninja é {1}".format(vida,vida_ninja))
                        print("seu ataque é de {0}".format(atk))
                        print("")
                        print("Agora faça sua escolha:")
                        print("")
                        
                        luta_ninja="Lutar"
                        
                        while vida_ninja>0 or luta_ninja=="Lutar":
                            
                            print("- Lutar")
                            print("- Fugir")
                            print("")
                                
                            luta_ninja=input("Opção: ")
                                
                            while luta_ninja != "Lutar" and luta_ninja != "Fugir":
                                print("Inválido!")
                                luta_ninja=input("Digite Novamente: ")
                                
                            if luta_ninja == "Lutar":
                                vida-=atk_ninja
                                vida_ninja-=atk
                                if vida < 0:
                                    vida = 0
                                if vida_ninja < 0:
                                    vida_ninja = 0
                                if vida == 0 and vida_ninja > 0:
                                    print("perdeu")
                                    break
                                if vida > 0 and vida_ninja == 0:
                                    print("ganhou")
                                    break
                                print("Sua vida é {0} e a vida do ninja é {1}".format(vida,vida_ninja))
                            
                            if luta_ninja == "Fugir":
                                print("Essa foi por pouco! Tome mais cuidado da proxima vez!")
                                break
                            
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                    
            
            elif numero_andar == "3 andar":
                
                cont_tempo+=1
                
                print("")
                print("-------")
                print("3 Andar")
                print("-------")
                print("Agora que você entrou no 3° andar você tem algumas opções para escolher.")
                print("Entre elas temos a Moça do Café, a Sala 1 de ModSim e a Sala 2 de ModSim.")
                print("(Nas salas de ModSim, em uma delas o Pelicano está dando monitoria e a outra Sala está vazia)")
                print("")
                print("- Café (5 min)")
                print("- Sala 1 (20 min)")
                print("- Sala 2 (20 min)")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                escolha3andar=input("Opção: ")
                
                while escolha3andar != "Café" and escolha3andar != "Sala 1" and escolha3andar != "Sala 2":
                    print("Inválido!")
                    escolha3andar=input("Digite Novamente: ")
                    
                if escolha3andar == "Café":
                    
                    if cont_cafe >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                    
                        cont_cafe+=1
                        cont_tempo+=5
                        cont_tempo-=30
                        
                        print("")
                        print("----------------")
                        print("Carrinho do Café")
                        print("----------------")
                        print("Moça: Bom dia {0}!".format(name))
                        print("Moça: Como hoje é o dia da sua entrega do EP iremos dar uma ajuda para você!")
                        print("Moça: Como ajuda daremos a você 30 minuntos a mais para você achar o Raul, irei colocar um tipo de sonífero que fará com que ele durma por 30 minutos o que lhe dará mais tempo.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                    
                elif escolha3andar == "Sala 1":
                    
                    if cont_sala1m >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_sala1m+=1
                        cont_tempo+=20
                        
                        print("")
                        print("----------------")
                        print("Sala 1 de ModSim")
                        print("----------------")
                        print("Você entra na Sala e acaba percebendo que ela está vazia. Perde um tempo, porém sabe que agora ele está na Sala 2 de ModSim.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        
                        
                elif escolha3andar == "Sala 2":
                    
                    if cont_sala2m >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_sala2m+=1
                        n_profs+=1
                        cont_tempo+=20
                        
                        print("")
                        print("----------------")
                        print("Sala 2 de ModSim")
                        print("----------------")
                        print("Ao entrar na sala você se depara com o Pelicano de professor de ModSim.")
                        print("")
                        print("Pelicano: Olá {0}, tudo bem? Estava falando com o Raul e ele me contou que hoje seria o dia da entrega do seu EP, e acredito que você esteja com ele atrasado.".format(name))
                        print("Pelicano: Por isso irei te ajudar, e direi a ele que tinha esquecido de ter passado a vocês um Projeto e que por isso vocês acabaram se enrolando com o tempo.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        print("")
                        print("Você achou {0} dos professores.".format(n_profs))
                        print("")
                        acesso_raul()
                
            if numero_andar == "4 andar":
                
                cont_tempo+=1
                
                print("")
                print("-------")
                print("4 Andar")
                print("-------")
                print("Agora que você entrou no 4° andar você tem algumas opções para escolher.")
                print("")
                print("- Sala de Games (20 min)")
                print("- Lab de Instrumed (30 min)")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                escolha4andar=input("Opção: ")
                
                while escolha4andar != "Sala de Games" and escolha4andar != "Lab de Instrumed":
                    print("Inválido!")
                    escolha4andar=input("Digite Novamente: ")
                    
                if escolha4andar == "Sala de Games":
                    
                    if cont_games >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_games+=1
                        cont_tempo+=20
                        cont_tempo+=30
                        
                        print("")
                        print("-------------")
                        print("Sala de Games")
                        print("-------------")
                        print("Você entra na Sala de Games, encontra varios veteranos e bixos jogando.")
                        print("Por fim, você começa a jogar Mario Kart e Smash juntando-se a eles.") 
                        print("Passados 30 minutos você percebe que se distraiu tempo demais e sai correndo da sala.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        
                elif escolha4andar == "Lab de Instrumed":
                    
                    if cont_lab >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_lab+=1
                        n_profs+=1
                        cont_tempo+=30
                        
                        print("")
                        print("----------------")
                        print("Lab de Instrumed")
                        print("----------------")
                        print("Ao chegar no laboratório você acaba encontrando o Carlos professor de Instrumed.")
                        print("")
                        print("Carlos: Bom dia {0}, vou te ajudar com o seu problema sobre o EP, fiquei sabendo dele por outros alunos que vieram aqui antes e porque todos os outros semestres acontece a mesma coisa.".format(name))
                        print("Vou falar para ele que eu te passei um experimento com um relatório de última hora e por isso você acabou ficando ocupado e perdeu o tempo do seu EP.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        print("")
                        print("Você achou {0} dos professores.".format(n_profs))
                        print("")
                        acesso_raul() 
                
            if numero_andar == "5 andar":
                
                cont_tempo+=1
                
                print("")
                print("-------")
                print("5 Andar")
                print("-------")
                print("Agora que você entrou no 5° andar você tem algumas opções para escolher.")
                print("")
                print("- Sala de Entidades (20 min)")
                print("- Restaurante (20 min)")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                escolha5andar=input("Opção: ")
                
                while escolha5andar != "Sala de Entidades" and escolha5andar != "Restaurante":
                    print("Inválido!")
                    escolha5andar=input("Digite Novamente: ")
                    
                if escolha5andar == "Sala de Entidades":
                    
                    if cont_entidades >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_entidades+=1
                        cont_tempo+=20
                        
                        print("")
                        print("-----------------")
                        print("Sala de Entidades")
                        print("-----------------")
                        print("Você entrou na Sala de Entidades e se depara com um Veterano e ja pensa 'A não mais um veterano',porém você percebe que o Pedrão.")
                        print("")
                        print("Pedrão: Eae {0}, beleza? Ta precisando de ajuda em algo cara?".format(name))
                        print("Suas escolhas são:")
                        print("'Sim, tava precisando de ajuda para encontrar o Raul para tentar adiar minha EP.'")
                        print("'Não, valeu to precisando correr.'")
                        print("")
                        print("- Sim (5 min)")
                        print("- Não (0 min)")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        print("")
                    
                    sala_entidades=input("Opção: ")
                    
                    while sala_entidades != "Sim" and sala_entidades != "Não":
                        print("Inválido")
                        sala_entidades=input("Digite Novamente: ")
                        
                    if sala_entidades == "Sim":
                        
                        cont_tempo+=5
                        vida+=5
                        
                        print("Pedrão: Beleza, vou te dar um item aqui que vai te ajudar com o Raul, espera ai que eu vou buscar e ja te dou.")
                        print("Depois de um tempo...")
                        print("Eae voltei, toma aqui seu item, ele vai te dar mais 5 de vida, ou seja, você vai ficar agora com {0} de vida.".format(vida))
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        
                    elif sala_entidades == "Não":
                        
                        cont_tempo+=0
                        
                        print("Pedrão: Suave então, falou e boa sorte ai!")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                    
                elif escolha5andar == "Restaurante":
                    
                    if cont_restaurante >= 1:
                        
                        print("")
                        print("Você ja entrou nessa sala!")
                        
                    else:
                        
                        cont_restaurante+=1
                        n_profs+=1
                        cont_tempo+=20
                        
                        print("")
                        print("-----------")
                        print("Restaurante")
                        print("-----------")
                        print("Você olha para as mesas do Restaurante e se depara com o Vitor de NatDes.")
                        print("Victor: Bom dia {0}, fiquei sabendo que hoje é o dia da sua entrega do seu EP por isso, você pode falar com o Raul que eu te passei uma entrega de protótipo e isso te consumiu muito tempo.".format(name))
                        print("Victor: Se ele vier me perguntar irei dizer que é verdade.")
                        print("")
                        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                        print("")
                        print("Você achou {0} dos professores.".format(n_profs))
                        print("")
                        acesso_raul()
            
            if numero_andar == "6 andar":
                if n_profs == 4:
                    atk*=2
                
                print("")
                print("-------")
                print("6 andar")
                print("-------")
                print("Você está no 6° andar agora e terá que enfrentar o Raul para conseguir o adiamentodo EP.")
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("")
                
                raul=input("Você está pronto? ")
                
                while raul != "Sim" and raul != "sim":
                    print ("Inválido!")
                    raul=input("Digite Novamente: ")
                    
                if raul == "Sim" or raul == "sim":
                    print("")
                    print("-----------------")
                    print("Raul - Fase Final")
                    print("-----------------")
                    print("Você entra na sala do Raul e encontra ele.")
                    print("Raul: Olá {0}, não acredito que você esteja aqui para entregar o seu EP, então provavelmente você está querendo um adiamento dele, bom isso só será possível se você conseguir me derrotar.".format(name))
                    print("Raul: Mas devo avisa-lo que até somente uma pessoa conseguiu me derrotar. Então boa sorte porque você irá precisar!")
                    
                    aceitar=input("Começar Luta? ")
                    
                    while aceitar != "Sim" and aceitar != "sim":
                        print("Inválido")
                        aceitar=input("Digite Novamente: ")
                        
                    if aceitar == "Sim" or aceitar == "sim":
                        
                        print("sua vida é {0} e a vida do Raul é {1}".format(vida,vida_raul))
                        print("seu ataque é de {0}".format(atk))
                        print("")
                        luta_raul="Atacar"
                        
                        while vida_raul>0 or luta_raul=="Atacar":
                            print("Atacar")
                            luta_raul=input("Faça sua escolha: ")
                            if luta_raul == "Atacar":
                                vida-=atk_ninja
                                vida_raul-=atk
                                print("Sua vida é {0} e a vida do Raul é {1}".format(vida,vida_raul))
                                
                                if vida < 0:
                                    vida = 0
                                if vida_raul < 0:
                                    vida_raul = 0
                                if vida == 0 and vida_raul > 0:
                                    break
                                if vida > 0 and vida_raul == 0:
                                    cont_win+=1
                                    break
                                            
                                            
                                                
                                                
    elif entrada == "Sair":
            
        n_profs+=1  
        cont_tempo+=10
        
        print("")
        print("---------")
        print("Fumódromo:")
        print("---------")
        print("Você encontrou um dos professores: O Fernando de GDE! Ele está fumando aqui fora.")
        print("")
        print("Fernando: Parabéns você encontrou o Easter Egg do jogo!")
        print("Fernando: Agora, se você quiser tenho uma charada para você, caso acerte você ganhará o tempo que foi perdido para sair do Insper. ")
        print("")
        print("- Aceitar")
        print("- Recusar")
        print("")
        print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
        print("")
        
        riddle=input("Opção: ")
        
        while riddle != 'Aceitar' and riddle != "Recusar":
            print("Inválido!")
            riddle=input('Digite Novamente: ')
        
        if riddle == "Aceitar":
            print("")
            print("A charada é: 'O Palmeiras tem mundial?'")
            print("")
            print("- Sim")
            print("- Não")
            print("")
            
            palmeiras=input("Opção: ")
            
            while palmeiras != 'Sim' and palmeiras != 'Não':
                print("Inválido")
                palmeiras=input("Opção: ")
            
            if palmeiras == 'Sim':
                print("")
                print("Fernando: Meu caro Engenheiro/a, com uma resposta dessas você vai tirar 0 na PF de GDE! Tome cuidado!")
                print("Fernando: Já que você errou a charada irá entrar para o Saguão do Insper mas com 10 minutos já passados.")
                print("")
                print("Você achou {0} dos professores.".format(n_profs))
                print("")
                acesso_raul()
                
            elif palmeiras == 'Não':
                
                cont_tempo-=10
                
                print("")
                print('Fernando: Ainda bem que você sabe meu caro Engenheiro/a! Agora você irá entrar no Saguão do Insper dessa vez!')
                print("")
                print("Você tem {0} minutos restantes.".format(tempo_restante(cont_tempo)))
                print("") 
                print("Você achou {0} dos professores.".format(n_profs))
                print("")
                acesso_raul()
                
        elif riddle == "Recusar":
            print("")
            print('Fernando: Tudo bem, você entrar para o Saguão do Insper, entretanto o tempo já passou em 10 minutos')
            print("")
            acesso_raul()
            
    if cont_tempo >= 150 or vida == 0: 
    
        game_on = True
        
        print("")
        print("Você passou do tempo e não conseguiu encontrar o Raul!")
        print("Por isso você tirou 0 no EP")
        print("")
        print("---------")
        print("GAME OVER")
        print("---------")
        
    elif cont_win == 1:
        
        game_on = True
        
        print("")
        print("Raul: Meus parabéns, {0}! Irei adiar o seu EP, seus argumentos foram bem convincentes em relação aos trabalhos que você teve que entregar para os outros professores.".format(name))
        print("Parabéns você conseguiu adiar o seu EP.")
        print("")
        print("-------------------------")
        print("WIN - VOCÊ GANHOU O JOGO!")
        print("-------------------------")