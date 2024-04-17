import random

def animais() -> dict:
    '''Retorna os animais e seus valores.'''
    return {
        'Avestruz':[1,2,3,4],
        'Águia':[5,6,7,8],
        'Burro':[9,10,11,12],
        'Borboleta':[13,14,15,16],
        'Cachorro':[17,18,19,20],
        'Cabra':[21,22,23,24],
        'Carneiro':[25,26,27,28],
        'Camelo':[29,30,31,32],
        'Cobra':[33,34,35,36],
        'Coelho':[37,38,39,40],
        'Cavalo':[41,42,43,44],
        'Elefante':[45,46,47,48],
        'Galo':[49,50,51,52],
        'Gato':[53,54,55,56],
        'Jacare':[57,58,59,60],
        'Leão':[61,62,63,64],
        'Macaco':[65,66,67,68],
        'Porco':[69,70,71,72],
        'Pavao':[73,74,75,76],
        'Peru':[77,78,79,80],
        'Touro':[81,82,83,84],
        'Tigre':[85,86,87,88],
        'Urso':[89,90,91,92],
        'Veado':[93,94,95,96],
        'Vaca':[97,98,99,100]
    }


def exibe_animais(valores:dict) -> None:
    '''Exibe os animas, seus valores e suas posições.'''
    print('\nSelecione um animal:\n')
    for index, valor in enumerate(valores.items()):
        print(f'{index} - {valor[0]} - {", ".join(map(str, valor[1]))}')


def generate_aposta_numero() -> list:
    '''Retorna a lista de números escolhidos.'''
    return [int(input('\nEscolha um número: ')) for _ in range(4)]


def aposta_numero(valores:dict) -> list:
    '''Verifica se os números selecionados totalizam quatro e se são diferentes entre si.
    Retorna a lista de números.'''
    exibe_animais(valores)
    aposta = generate_aposta_numero()

    while len(set(aposta)) < 4:
        print('Há números repitidos. Informe novamente os números: ')
        aposta = generate_aposta_numero()

    return aposta


def aposta_animal(valores:dict) -> list:
    '''Retorna a lista de números com base no animal.'''
    exibe_animais(valores)
    aposta = list(valores)[int(input('\nEscolha um animal:\n'))]
    numeros = valores[aposta]

    return numeros


def opcoes_aposta() -> int:
    '''Retorna a respota do tipo de aposta.'''
    return int(input('\nDefina o tipo de aposta:\n1- Número\n2- Animal\n\n'))


def define_aposta(valores:dict, aposta:list=None) -> list:
    '''Executa a seleção do tipo de aposta, a aposta em si
    e retorna a lista de números escolhidos.'''
    tipos = {
        1: aposta_numero,
        2: aposta_animal
    }
    resp = opcoes_aposta()
    option = tipos.get(resp)

    while not option:
        resp = opcoes_aposta()
        option = tipos.get(resp)

    aposta = sorted(option(valores))
    print(f'\nAposta: {", ".join(map(str, aposta))}')

    return aposta


def find_animal(valores:list, number:int) -> tuple:
    '''Retorna o animal e seus valores com base no número sorteado.'''
    for valor in valores:
        if number in valor[1]:
            return valor


def winner(aposta:list, animal:tuple) -> bool:
    '''Verifica se o usuário ganhou.'''
    for numero in aposta:
        if numero in animal:
            return True


def resultado(number:int, animal:tuple, aposta:list) -> None:
    '''Exibe o número e o animal sorteado.
    Em seguida, exibe se o joador ganhou.'''
    print(f'\nNúmero: {number}\nAnimal: {animal[0]}\n')

    if winner(aposta, animal[1]):
        print('Você venceu')
    else:
        print('Você perdeu')


def generate_numbers(numeros:list=[]) -> list:
    '''Sorteia quatro números.'''
    while len(set(numeros)) < 4:
        numeros = [random.randint(1,100) for _ in range(4)]
    
    return sorted(numeros)


def sorteio() -> None:
    '''Executa o programa.'''
    valores = animais()
    aposta = define_aposta(valores)
    # numbers= generate_numbers()
    number = random.randint(1,100)
    animal = find_animal(valores.items(), number)
    resultado(number, animal, aposta)
    

sorteio()