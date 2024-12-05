import random

class Personagem:
    def __init__(self, nome, hp, forca):
        self.nome = nome
        self.hp = hp
        self.forca = forca
        self.item_equipado = None

    def atacar(self, inimigo):   # metodo atacar
        dano = self.forca   # inicializo o valor da varivael dano
        aleatorio = random.randint(0, 20)   # inicializo a variavel aleatorio com um randomizer de 0 a 20
        if aleatorio == 20: dano += self.forca * 0.5  # condicional para caso o aleatorio alncance o valor maximo, o bonus seja de 50% da força máxima do personagem
        elif 15 <= aleatorio <= 19: dano += self.forca + self.forca *0.3  # condicional para caso o aleatorio seja entre 15 e 19 o bonus seja %30 da força maxima
        elif 10 <= aleatorio <= 14: dano += self.forca + self.forca *0.1  # condicional para caso o aleatorio seja entre 10 e 14 o bonus seja %10 da força maxima
        elif 5 <= aleatorio <= 9: dano = self.forca     # condicional para caso o aleatorio seja entre 5 e 9 nao haja bonus de força
        elif aleatorio < 5: dano = self.forca - self.forca * 0.25    # condicional para caso o aleatorio seja abaixo de 5 tenha um debuff de força de 25%

        inimigo.hp -= dano  # atualiza a vida do inimigo
        print(f"{self.nome} obteve o resultado de {aleatorio}, causando {dano} de dano!")

    def golpe_especial(self, inimigo):  
        dano_especial = self.forca * 2  # golpe especial eh o stats de força do player dobrado
        inimigo.hp -= dano_especial 
        print(f"{self.nome} usou o Golpe Especial e causou {dano_especial} de dano!")

    def equipar_item(self, item):
        if self.item_equipado:  # caso já tenha algum item equipado:
            print(f"{self.nome} já está usando {self.item_equipado.nome}, substituindo por {item.nome}")    # substitui o item
            self.forca -= self.item_equipado.bonus  # retira o bonus do item equipado
        else:
            print(f"{self.nome} equipou um item pela primeira vez!")

        self.item_equipado = item   # atualiza o item equipado
        print(f"{self.nome} equipou o {item.nome}, ganhando um bônus de {item.bonus} força!")
        self.forca += item.bonus    # atualiza a força bonus
        return self.forca       # retorna self.forca pro def __init__
    
    def desequipar_item(self, item):
        if self.item_equipado:
            self.forca -= self.item_equipado.bonus  # retira o stats do item
            print(f"{self.nome} Desequipou o item{self.item_equipado.nome} e perdeu {self.item_equipado.bonus} de força!")  
            self.item_equipado = None   # desequipa o item
        else:
            print("Você não possui nenhum item equipado!")  # caso nao tenha nenhum item equipado

    def esta_vivo(self):    # metodo pra usar na classe Combate
        return self.hp > 0
    
    def exibir_stats(self):
        item_nome = self.item_equipado.nome if self.item_equipado else "Nenhum item equipado"
        print(f"Nome: {self.nome}\nHP: {self.hp}\nForça: {self.forca}\nItem: {item_nome}")




class Item:
    def __init__(self, nome, tipo, bonus):  # pra criar um item
        self.nome = nome
        self.tipo = tipo
        self.bonus = bonus



class Inimigo(Personagem):
    def __init__(self, nome, hp, força):
        super().__init__(nome, hp, força)
        self.bonus_magia = self.forca * 2   # golpe especial do inimigo

    def atacar(self, personagem):
        aleatorio = random.randint(0, 20)   # mesma logica do def atacar da classe personagem
        if aleatorio == 20:
            dano_inimigo = self.forca * 1.5
        elif 15 <= aleatorio <= 19:
            dano_inimigo = self.forca + self.forca * 0.3
        elif 10 <= aleatorio <= 14:
            dano_inimigo = self.forca + self.forca * 0.1
        elif 5 <= aleatorio <= 9:
            dano_inimigo = self.forca
        else:
            dano_inimigo = self.forca - self.forca * 0.25
        
        personagem.hp -= dano_inimigo
        print(f"{self.nome} atacou {personagem.nome} causando {dano_inimigo} de dano.")
        



class Combate:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo
        self.turno = 0
        self.contador_turnos = 0
    
    def alternar_turno(self):
        self.turno = 1 - self.turno

    def iniciar_combate(self):
        while self.personagem.esta_vivo() and self.inimigo.esta_vivo():     # enquanto os 2 personagens estiverem vivos:

            if self.turno == 0:     # se o turno for igual a 0, é a vez do player
                print(f"\nÉ a vez de {self.personagem.nome}!") 

                if self.contador_turnos % 3 == 0:   # a cada 3 turnos o player pode usar um golpe especial
                    print(f"{self.personagem.nome} pode usar o Golpe Especial!")
                    acao = input("Escolha sua ação:\n1 - Atacar\n2 - Golpe Especial\n")
                    if acao == "1":
                        self.personagem.atacar(self.inimigo)
                        print(f"{self.personagem.nome} atacou {self.inimigo.nome}!")
                    else:
                        self.personagem.golpe_especial(self.inimigo)
                        print(f"{self.personagem.nome} atacou {self.inimigo.nome} com um golpe especial!")

                else:   
                    acao = input("Escolha sua ação:\n1 - Atacar\n2 - Golpe Especial (NÃO DISPONÍVEL)\n")
                    if acao == "1":
                        self.personagem.atacar(self.inimigo)
                        print(f"{self.personagem.nome} atacou {self.inimigo.nome}!")
                    while acao != "1":
                        print(f"\nVocê não pode executar essa ação no momento.\n")
                        acao = input("Escolha sua ação:\n1 - Atacar\n2 - Golpe Especial (NÃO DISPONÍVEL)\n")
                        
            else:   
                print(f"\nÉ a vez de {self.inimigo.nome} atacar!")
                aleatorio = random.randint(0,10)    # tem uma chance de 10% do inimigo dar um golpe critico em vc usando magia
                if aleatorio == 10:
                    print(f"{self.inimigo.nome} conseguiu conjurar uma magia contra você, causando {self.inimigo.bonus_magia} de dano!!")
                    self.personagem.hp -= self.inimigo.bonus_magia
                else:       # se ele nao conseguir roletar 10 para dar o golpe, ele vai dar o ataque basico
                    print(f"{self.inimigo.nome} atacou {self.personagem.nome}!")
                    self.inimigo.atacar(self.personagem)
            '''
            print("\n___________________________________________________")
            print(f"\n{self.personagem.nome} tem {self.personagem.hp} HP restantes.")
            print(f"{self.inimigo.nome} tem {self.inimigo.hp} HP restantes.\n")
            print("___________________________________________________")
            '''
            
            self.alternar_turno()   # alterna o turno 
            self.contador_turnos += 1   # atualiza o contador para o player poder ter o golpe especial

        if self.personagem.esta_vivo():
            print("\nVocê venceu!")
            self.personagem.hp += 60
        else:
            print("\nVocê perdeu!")

'''
personagem = Personagem("Gabrieow", 100, 20)
inimigo = Inimigo("deus ancião", 1500, 15)
mata_deus = Item("Matadora de deuses", "Espada", 100)

personagem.equipar_item(mata_deus)
personagem.desequipar_item(mata_deus)
personagem.equipar_item(mata_deus)
personagem.exibir_stats()

combate = Combate(personagem, inimigo)
combate.iniciar_combate()
'''