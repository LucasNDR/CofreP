import random
import time

atributos = []
lista_habilidades = []
pvmaxplayer = 0
pvatualplayer = 0
pm = 0
defesa = 0
nível = 1
xp = 0
DadoDanoPlayer = 6
pmgastos = 0
pmatual = pm - pmgastos


DadoDanoIni = 6
pvmaxinimigo = 0
pvatualinimigo = 0


forcainimigo = 0

DanoInimigo = (random.randint(1, DadoDanoIni)) + forcainimigo


lista_raca = ['Anão', 'Elfo', 'Humano', 'Orc']
lista_classe = ['Bárbaro', 'Arcanista', 'Cavaleiro', 'Clérigo', 'Druida', 'Inventor', 'Guerreiro']
lista_magias = [['1- Misseis Mágicos'], ['2- Armadura Arcana'], ['3- Cone de Chamas'], ['4- Cura Arcana'], ['5- Ataque Certeiro'], ['6- Arma Mágica'], ['7- Toque Vampírico']]

while True:
    print(lista_raca)
    print("Qual a sua raça?")
    racaec = str(input())
    pj_raca = racaec.lower()
    time.sleep(1)

#Confirmação com o usuário
    print("Certo! Sua raça será", pj_raca)
    if pj_raca == "anão":
        print("Você receberá +4 em constituição e +2 em força.")
    elif pj_raca == "elfo":
        print("Você receberá +4 em destreza e +2 em carisma.")
    elif pj_raca == "humano":
        print("Você receberá +2 em três atributos a sua escolha.")
    elif pj_raca == "orc":
        print("Você receberá +4 em força, +2 em constituição e -2 em carisma.")
    time.sleep(1)
    
    resposta_raca = str(input("Você tem certeza da sua escolha? Essa escolha não pode ser desfeita! (S/N)"))
    if resposta_raca in "Ss":
        break

#Gera os atributos do personagem
if resposta_raca in "Ss":
    print("Confirmado! Você será um", pj_raca)
    for i in range (6):
        atributos.append(random.randint(6, 20))
    print("Estes são seus atributos:")
    forca = atributos[0]
    dex = atributos[1]
    con = atributos[2]
    intel = atributos[3]
    sab = atributos[4]
    car = atributos[5]
    #isso pode com certeza pode melhorar
    if pj_raca == "anão":
        forcabonus = int(((forca + 2) - 10) / 2)
        dexbonus = int(((dex) - 10) / 2)
        conbonus = int(((con + 4) - 10) / 2)
        intbonus = int(((intel) - 10) / 2)
        sabbonus = int(((sab) - 10) / 2)
        carbonus = int(((car) - 10) / 2)
        atributosbonus = [forcabonus, dexbonus, conbonus, intbonus, sabbonus, carbonus]
    elif pj_raca == "elfo":
        forcabonus = int(((forca) - 10) / 2)
        dexbonus = int(((dex + 4) - 10) / 2)
        conbonus = int(((con) - 10) / 2)
        intbonus = int(((intel) - 10) / 2)
        sabbonus = int(((sab) - 10) / 2)
        carbonus = int(((car + 2) - 10) / 2)
        atributosbonus = [forcabonus, dexbonus, conbonus, intbonus, sabbonus, carbonus]
    elif pj_raca == "orc":
        forcabonus = int(((forca + 4) - 10) / 2)
        dexbonus = int(((dex) - 10) / 2)
        conbonus = int(((con + 2) - 10) / 2)
        intbonus = int(((intel) - 10) / 2)
        sabbonus = int(((sab) - 10) / 2)
        carbonus = int(((car - 2) - 10) / 2)
        atributosbonus = [forcabonus, dexbonus, conbonus, intbonus, sabbonus, carbonus]
print(atributosbonus)
time.sleep(5)

#escolha de classe de personagem
while True:
    print("Qual sua classe?")
    time.sleep(1)
    print(lista_classe)
    classeec = str(input())
    pjclasse = classeec.lower()
    time.sleep(1)
    print("Certo! Sua classe será", pjclasse)
    #toda essa sequência das classes pode melhorar
    if pjclasse == "bárbaro":
        print("Você recebe as habilidades: 'Fúria', 'Vitalidade Bárbara' e RD 1.")
        Fúria = str("Fúria: Você recebe +2 em ataques e dano. Também recebe RD1 cumulativo com outras.")
        VitBarb = str("Vitalidade Barbara: Você soma sua força e constituição nos seus pontos de vida totais e na defesa.")
        ReDa = str("Redução de dano: Você ignora uma quantidade X de dano de qualquer tipo.")
        lista_habilidades = ([Fúria, VitBarb], [ReDa])
        pv = 20 + (conbonus + forcabonus)
        defesa = 10 + int(conbonus + dexbonus + forcabonus + (nível / 2))
        time.sleep(5)
        break
    elif pjclasse == "arcanista":
        print("Você recebe as habilidades: 'Magias', 'Defesa Arcana' e 'Grimório' onde possui 3 magias anotadas.")
        Magias = str("Magias: Você pode lançar magias, arcanas ou divinas, pelo custo de PMs. Você pode lançar magias mais fortes a cada 4 níveis e aprende uma nova a cada nível de personagem.")
        Grimorio = str("Grimorio: Você pode estudar suas magias anotadas aqui e lança-las. Para estudar, escolha metade das magias que conhece (Arredondado para baixo) e gaste 1 hora de estudo. Você poderá lançar as magias escolhidas livremente até o proximo descanso.")
        DefArcana = str("Defesa Arcana: Você soma sua inteligência +50% à sua defesa")
        Grimorio_Anotado = []
        lista_habilidades = ([Magias, Grimorio], [DefArcana])
        pv = 6 + (conbonus)
        defesa = 10 + int((intbonus * 3 / 2) + dexbonus + (nível / 2))
        pm = 6 + (intbonus)
        time.sleep(5)
        print("Escolha 3 dentre as seguintes magias.")
        for lista_magia_vert in lista_magias:
            for item in lista_magia_vert:
                print("[", item, "] ")
        print("Digite o número da magia a escolher e aperte enter.")
        for i in range(3):
            esc_mag = input()
            if esc_mag == str(1):
                Grimorio_Anotado.append(['Misseis Mágicos: Lança 2 orbes mágicos que causam 1d4+1+INT de dano cada. (Custo: 1PM)'])
            elif esc_mag == str(2):
                Grimorio_Anotado.append(['Armadura Arcana: Soma sua inteligência à sua defesa. (Custo: 1PM)'])
            elif esc_mag == str(3):
                Grimorio_Anotado.append(['Cone de Chamas: Causa 2d6 de dano de fogo a inimigos no alcance. (Custo: 1PM)'])
            elif esc_mag == str(4):
                Grimorio_Anotado.append(['Cura Arcana: Cura 2d6 de vida para cada nível de personagem que possua. (Custo: 1PM + Nível de Personagem)'])
            elif esc_mag == str(5):
                Grimorio_Anotado.append(['Ataque Certeiro: O próximo ataque da criatura que foi alvo desta magia acertará automaticamente. (Custo: 4PM)'])
            elif esc_mag == str(6):
                Grimorio_Anotado.append(['Arma Mágica: Os testes com a arma alvo desta magia recebem +2 (Ataque, dano, manobras etc.) (Custo: 2PM)'])
            elif esc_mag == str(7):
                Grimorio_Anotado.append(['Toque Vampírico: causa 2d6 de dano por nível de personagem e recupera metade do dano em PVs. (Custo: 3PM)'])
            else:
                print("Esta não é uma magia valida. Digite corretamente ou escolha outra.")
        print("Essas serão as suas magias:")
        for Grimorio_Anotado_Vert in Grimorio_Anotado:
            for magiasgr in Grimorio_Anotado_Vert:
                print("[", magiasgr, "] ")
        
        break
    elif pjclasse == "cavaleiro":
        print("Você recebe as habilidades: 'Código de Honra', 'Combatente Escolático' e Redução de Dano 1")
        CodHonra = str("Você segue um código de ética restrito. Você não pode se beneficiar das seguintes condições:'Caído', 'Flanqueado', 'desprevenido'; Em compensação, pode causar +4 de dano contra inimigos caso tenha sido afetado por uma condição como essas neste combate.")
        ComEsco = str("Você recebe uma habilidade de combate pelo seu treinamento especial. Você também pode usar armaduras pesadas.")
        ReDa = str("Redução de dano: Você ignora uma quantidade X de dano de qualquer tipo.")
        lista_habilidades = [[CodHonra], [ComEsco], [ReDa]]
        pv = 20 + (conbonus)
        defesa = 10 + int(dexbonus + (nível / 2))



DanoCausado_Player = (random.randint(1, DadoDanoPlayer)) + forcabonus
#n sei como melhorar isso
def DanoParaInimigo1():
    pvatualinimigo = pvmaxinimigo - DanoCausado_Player

def DanoParaInimigo2():
    pvatualinimigo = pvatualinimigo - DanoCausado_Player

def DanoParaPlayer1():
    pvatualplayer = pvmaxplayer - DanoInimigo

def DanoParaPlayer2():
    pvatualplayer = pvatualplayer - DanoInimigo

#Mostra os status do personagem e as habilidades 
print("\n")
print("Seus atributos:", atributosbonus)
print("Pontos de Vida:", pv,"; Sua defesa:", defesa, "; Seus Pontos de Mana:", pm, "; Nível:", nível)
print("Sua Classe:", pjclasse,)
print("Sua raça:", pj_raca)
print("\n")
print("Suas Habilidades:")
for list_hab_Vert in lista_habilidades:
	for item in list_hab_Vert:
	   print("[", item, "] ")
print("\n")
if pjclasse == "arcanista":
    print("Seu grimorio possui as seguintes magias:")
    for Grimorio_Anotado_Vert in Grimorio_Anotado:
            for magiasgr in Grimorio_Anotado_Vert:
                print("[", magiasgr, "] ")
time.sleep(10)
print("\n")
print("a")
acao = input()  

def ficha():
    print("\n")
    print("Seus atributos:", atributosbonus)
    print("Pontos de Vida:", pv,"; Sua defesa:", defesa, "; Seus Pontos de Mana:", pm, "; Nível:", nível)
    print("PVs Atuais:", pvatualplayer,"; PMs Atuais:", pm)
    print("Sua Classe:", pjclasse,)
    print("Sua raça:", pj_raca)
    print("\n")
    if pjclasse == "arcanista":
        print("Seu grimorio possui as seguintes magias:")
        for Grimorio_Anotado_Vert in Grimorio_Anotado:
            for magiasgr in Grimorio_Anotado_Vert:
                print("[", magiasgr, "] ")
    print("\n")
    print("Suas Habilidades:")
    for list_hab_Vert in lista_habilidades:
	    for item in list_hab_Vert:
	        print("[", item, "] ")
print("\n")


if acao == "ficha":
    ficha()
