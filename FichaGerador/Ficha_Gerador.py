import random
import time
import func

atributos = []
lista_habilidades = []
nível = 1
pv = 0


lista_raca = ['Anão', 'Elfo', 'Humano', 'Orc']
lista_classe = ['Bárbaro', 'Arcanista', 'Cavaleiro', 'Clérigo', 'Druida', 'Inventor', 'Guerreiro']
lista_magias_arc = [['1- Misseis Mágicos'], ['2- Armadura Arcana'], ['3- Cone de Chamas'], ['4- Cura Arcana'], ['5- Ataque Certeiro'], ['6- Arma Mágica'], ['7- Toque Vampírico']]
lista_magias_div = [['1- Curar Ferimentos'], ['2- Manto da Fé'], ['3- Arma Espiritual'], ['4- Riso Incrontrolável'], ['5- Bênção'], ['6- Aparência Divina']]
lista_magias_nat = [['1- Armadura Arbórea'], ['2- Arma Natural'], ['3- Controlar Plantas'], ['4- Curar Ferimentos'], ['5- Orientação dos Ermos'], ['6- Buraco de coelho'], ['7- '], ['']]

while True:

    for pj_raca in range(len(lista_raca)):
        print(f'{pj_raca + 1} - {lista_raca[pj_raca]}')

    time.sleep(1)
    numescolharaca = int(input('Digite o numero da classe: ')) - 1
    if numescolharaca < 0:
        numescolharaca = 10000
    time.sleep(1)

#Confirmação com o usuário
    if numescolharaca < len(lista_raca):
        print("\nCerto! Sua raça será", lista_raca[numescolharaca])
        if numescolharaca == 0:
            print("Você receberá +4 em constituição e +2 em força.")
        elif numescolharaca == 1:
            print("Você receberá +4 em destreza e +2 em carisma.")
        elif numescolharaca == 2:
            print("Você receberá +2 em três atributos a sua escolha.")
        elif numescolharaca == 3 and numescolharaca != -1:
            print("Você receberá +4 em força, +2 em constituição e -2 em carisma.")
    else:
        print('\nesse numero não consta na lista\n')
        continue
    time.sleep(1)

    resposta_raca = str(input("Você tem certeza da sua escolha? Essa escolha não pode ser desfeita! (S/N)"))
    if resposta_raca in "Ss":
        break
    elif resposta_raca in "Nn":
        time.sleep(1)
        continue
    else:
        time.sleep(1)
        print('\nTente denovo\n')
        time.sleep(1)

#Gera os atributos do personagem
if resposta_raca in "Ss":
    print("Confirmado! Você será um", lista_raca[numescolharaca])
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
    if numescolharaca == 0:
        forcabonus = int(((forca + 2) - 10) / 2)
        dexbonus = int(((dex) - 10) / 2)
        conbonus = int(((con + 4) - 10) / 2)
        intbonus = int(((intel) - 10) / 2)
        sabbonus = int(((sab) - 10) / 2)
        carbonus = int(((car) - 10) / 2)
        atributosbonus = [forcabonus, dexbonus, conbonus, intbonus, sabbonus, carbonus]
    elif numescolharaca == 1:
        forcabonus = int(((forca) - 10) / 2)
        dexbonus = int(((dex + 4) - 10) / 2)
        conbonus = int(((con) - 10) / 2)
        intbonus = int(((intel) - 10) / 2)
        sabbonus = int(((sab) - 10) / 2)
        carbonus = int(((car + 2) - 10) / 2)
        atributosbonus = [forcabonus, dexbonus, conbonus, intbonus, sabbonus, carbonus]
    elif numescolharaca == 3:
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
    while True:
        for pjclasse in range(len(lista_classe)):
            print(f'{pjclasse + 1} - {lista_classe[pjclasse]}')

        time.sleep(1)
        numescolhaclass = int(input('Digite o numero da classe: ')) - 1
        if numescolhaclass < 0:
            numescolhaclass = 10000
        time.sleep(1)
        if numescolharaca < len(lista_raca):
            print(f'certo, sua classe sera {lista_classe[numescolhaclass]}')
            if resposta_raca in "Ss":
                break
        else:
            print('tente denovo')
        
    #toda essa sequência das classes pode melhorar
    if numescolhaclass == 0:
        print("Você recebe as habilidades: 'Fúria', 'Vitalidade Bárbara' e RD 1.")
        Fúria = str("Fúria: Você recebe +2 em ataques e dano. Também recebe RD1 cumulativo com outras.")
        VitBarb = str("Vitalidade Barbara: Você soma sua força e constituição nos seus pontos de vida totais e na defesa.")
        ReDa = str("Redução de dano: Você ignora uma quantidade X de dano de qualquer tipo.")
        lista_habilidades = ([Fúria, VitBarb], [ReDa])
        pv = func.pv_calculo(20, conbonus, forcabonus)
        defesa = func.defesa_calculo(10, dexbonus, forcabonus, conbonus, int(nível / 2)) 
        pm = 0
        time.sleep(5)
        break
    elif numescolhaclass == 1:
        print("Você recebe as habilidades: 'Magias', 'Defesa Arcana' e 'Grimório' onde possui 3 magias anotadas.")
        Magias = str("Magias: Você pode lançar magias, arcanas ou divinas, pelo custo de PMs. Você pode lançar magias mais fortes a cada 4 níveis e aprende uma nova a cada nível de personagem.")
        Grimorio = str("Grimorio: Você pode estudar suas magias anotadas aqui e lança-las. Para estudar, escolha metade das magias que conhece (Arredondado para baixo) e gaste 1 hora de estudo. Você poderá lançar as magias escolhidas livremente até o proximo descanso.")
        DefArcana = str("Defesa Arcana: Você soma sua inteligência à sua defesa")
        Grimorio_Anotado = []
        lista_habilidades = ([Magias, Grimorio], [DefArcana])
        pv = func.pv_calculo(6, conbonus, 0)
        defesa = func.defesa_calculo(10, dexbonus, intbonus, int(nível / 2), 0) 
        pm = func.pm_calculo(6, intbonus)
        time.sleep(5)
        print("Escolha 3 dentre as seguintes magias.")
        for lista_magia_vert in lista_magias_arc:
            for item in lista_magia_vert:
                print("[", item, "] ")
        print("Digite o número da magia a escolher e aperte enter.")
        #esse ciclo de elif pra escolher a magia pode melhorar, mas não sei como
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
        time.sleep(5)
        break
    elif numescolhaclass == 2:
        print("Você recebe as habilidades: 'Código de Honra', 'Combatente Escolático' e Redução de Dano 1")
        CodHonra = str("Código de Honra: Você segue um código de ética restrito. Você não pode se beneficiar das seguintes condições:'Caído', 'Flanqueado', 'desprevenido'; Em compensação, pode causar +4 de dano contra inimigos caso tenha sido afetado por uma condição como essas neste combate.")
        ComEsco = str("Combatente Escolático: Você recebe uma habilidade de combate pelo seu treinamento especial. Você também pode usar armaduras pesadas.")
        ReDa = str("Redução de dano: Você ignora uma quantidade X de dano de qualquer tipo.")
        lista_habilidades = [[CodHonra], [ComEsco], [ReDa]]
        pv = func.pv_calculo(20, conbonus, 0)
        defesa = func.defesa_calculo(10, dexbonus, int(nível / 2), 0, 0) 
        pm = 0
        break
    

    elif numescolhaclass == 3:
        print("Você recebe as habilidades: 'Devoção', 'Magias', e 'Fé Esmagadora'.")
        Devocao = str("Devoção: Você recebe uma habilidade especial vinda da sua fé, mas precisa seguir as Obrigações&Restrições da sua igreja.")
        Magias = str("Magias: Você pode lançar magias, arcanas ou divinas, pelo custo de PMs. Você pode lançar magias mais fortes a cada 4 níveis e aprende uma nova a cada nível de personagem.")
        FeEsmag = str("Fé Esmagadora: Você recebe um bônus contra criaturas que sejam devotas de outro deus. Além disso, soma sua sabedoria na sua defesa.")
        lista_habilidades = [[Devocao], [Magias], [FeEsmag]]
        biblia_anotada = []
        pv = func.pv_calculo(16, conbonus, 0)
        pm = func.pm_calculo(4, sabbonus)
        defesa = func.defesa_calculo(10, dexbonus, sabbonus, int(nível / 2), 0)  
        for lista_magia_vert in lista_magias_div:
            for item in lista_magia_vert:
                print("[", item, "] ")
        print("Digite o número da magia a escolher e aperte enter. (Escolha três.)")
        for i in range(3):
            esc_mag = input()
            if esc_mag == str(1):
                biblia_anotada.append(['Curar Ferimentos: Cura 2d8+2 pontos de vida (Custo: 1PM)'])
            elif esc_mag == str(2):
                biblia_anotada.append(['Manto da Fé: Soma seu nível de clérigo na defesa do alvo da magia. (Custo: 1PM)'])
            elif esc_mag == str(3):
                biblia_anotada.append(['Arma Espiritual: Conjura uma arma a sua escolha para usar em combate. (Custo: 1PM)'])
            elif esc_mag == str(4):
                biblia_anotada.append(['Riso Incrontrolável: O alvo precisa ser bem sucedido em um teste de vontade, ou perderá o turno rindo. (Custo: 2PM)'])
            elif esc_mag == str(5):
                biblia_anotada.append(['Benção: O alvo da magia pode somar seu bônus de sabedoria em quaisquer testes pela cena. (Custo: 4PM)'])
            elif esc_mag == str(6):
                biblia_anotada.append(['Aparência Divina: O alvo da magia recebe +2 no bônus de carisma pelo dia. (Custo: 2PM)'])
            else:
                print("Esta não é uma magia valida. Digite corretamente ou escolha outra.")
        break

    elif numescolhaclass == 4:
        print("Você recebe as habilidades: 'Forma Selvagem', 'Conhecimento dos ermos' e 'Magias'.")
        Magias = str("Magias: Você pode lançar magias, arcanas ou divinas, pelo custo de PMs. Você pode lançar magias mais fortes a cada 4 níveis e aprende uma nova a cada nível de personagem.")
        Forma_selvagem = str("Você pode se transformar em uma criatura (animal ou monstro), ganhando atributos relativos a ela.")
        Conhecimento_Ermos = str("Você recebe bônus em quaisquer testes realizados em ambientes selvagens.")
        lista_habilidades = [[Forma_selvagem], [Magias], [Conhecimento_Ermos]]
        pv = func.pv_calculo(16, conbonus, 0)
        pm = func.pm_calculo(4, sabbonus)
        defesa = func.defesa_calculo(10, dexbonus, 0, int(nível / 2), 0)
        for lista_magia_vert in lista_magias_nat:
            for item in lista_magia_vert:
                print("[", item, "] ")
        break



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
if pjclasse == "clérigo":
    print("Seus conhecimentos religiosos lhe concederam as seguintes magias:")
    for biblia_Anotada_Vert in biblia_anotada:
            for magiasgr in biblia_Anotada_Vert:
                print("[", magiasgr, "] ")

time.sleep(10)
print("\n")
print("a")
acao = input()  
