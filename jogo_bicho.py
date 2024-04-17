import random

def animais() -> dict:
    '''Retorna os animais e seus valores.'''
    return {
        'Avestruz': [1, 2, 3, 4],
        'Águia': [5, 6, 7, 8],
        'Burro': [9, 10, 11, 12],
        'Borboleta': [13, 14, 15, 16],
        'Cachorro': [17, 18, 19, 20],
        'Cabra': [21, 22, 23, 24],
        'Carneiro': [25, 26, 27, 28],
        'Camelo': [29, 30, 31, 32],
        'Cobra': [33, 34, 35, 36],
        'Coelho': [37, 38, 39, 40],
        'Cavalo': [41, 42, 43, 44],
        'Elefante': [45, 46, 47, 48],
        'Galo': [49, 50, 51, 52],
        'Gato': [53, 54, 55, 56],
        'Jacare': [57, 58, 59, 60],
        'Leão': [61, 62, 63, 64],
        'Macaco': [65, 66, 67, 68],
        'Porco': [69, 70, 71, 72],
        'Pavao': [73, 74, 75, 76],
        'Peru': [77, 78, 79, 80],
        'Touro': [81, 82, 83, 84],
        'Tigre': [85, 86, 87, 88],
        'Urso': [89, 90, 91, 92],
        'Veado': [93, 94, 95, 96],
        'Vaca': [97, 98, 99, 100]
    }


def exibe_animais(valores: dict) -> None:
    '''Exibe os animais, seus valores e suas posições.'''
    print('\nSelecione um animal:\n')
    for index, (animal, valores) in enumerate(valores.items(), 1):
        print(f'{index} - {animal} - {", ".join(map(str, valores))}')


def generate_aposta_numero() -> list:
    '''Retorna a lista de números escolhidos.'''
    return [int(input('\nEscolha um número: ')) for _ in range(4)]


def aposta_numero(valores: dict) -> list:
    '''Verifica se os números selecionados totalizam quatro e se são diferentes entre si.
    Retorna a lista de números.'''
    exibe_animais(valores)
    aposta = generate_aposta_numero()

    while len(set(aposta)) < 4:
        print('Há números repetidos. Informe novamente os números: ')
        aposta = generate_aposta_numero()

    return sorted(aposta)


def aposta_animal(valores: dict) -> list:
    '''Retorna a lista de números com base no animal.'''
    exibe_animais(valores)
    animal_index = int(input('\nEscolha um animal:\n')) - 1
    animal = list(valores.keys())[animal_index]
    numeros = valores[animal]
    return numeros


def define_aposta(valores: dict) -> list:
    '''Executa a seleção do tipo de aposta e retorna a lista de números escolhidos.'''
    tipos = {1: aposta_numero, 2: aposta_animal}
    resp = opcoes_aposta()

    while resp not in tipos:
        print('Opção inválida. Tente novamente.')
        resp = opcoes_aposta()

    aposta_func = tipos[resp]
    aposta = sorted(aposta_func(valores))
    print(f'\nAposta: {", ".join(map(str, aposta))}\n')
    return aposta


def find_animal(valores: list, number: int) -> tuple:
    '''Retorna o animal e seus valores com base no número sorteado.'''
    for animal, valores in valores:
        if number in valores:
            return animal, valores


def winner(aposta: list, animal: tuple) -> bool:
    '''Verifica se o usuário ganhou.'''
    return any(numero in aposta for numero in animal[1])


def resultado(number: int, animal: tuple, aposta: list) -> None:
    '''Exibe o número e o animal sorteado e se o jogador ganhou.'''
    print(f'\nNúmero: {number}\nAnimal: {animal[0]}\n')

    if winner(aposta, animal):
        print('Você venceu')
    else:
        print('Você perdeu')


def generate_numbers(qntd: int = 4) -> list:
    '''Gera uma lista de números aleatórios.'''
    return sorted(random.sample(range(1, 101), qntd))


def sorteio() -> None:
    '''Executa o programa.'''
    valores = animais()
    aposta = define_aposta(valores)
    resp = tipo_sorteio()

    if resp == 1:
        sorteio_simples(valores, aposta)
    elif resp == 2:
        sorteio_solto(aposta)


def sorteio_simples(valores: dict, aposta: list):
    number = random.randint(1, 100)
    animal = find_animal(valores.items(), number)
    resultado(number, animal, aposta)


def sorteio_solto(aposta: list):
    qntd = int(input("\nInforme a quantidade de números sorteados: "))
    while qntd <= 0:
        print("Quantidade inválida. Tente novamente.")
        qntd = int(input("\nInforme a quantidade de números sorteados: "))

    numbers = generate_numbers(qntd)
    exibe_numeros_apostas(numbers, aposta)

    if resultado_mult(numbers, aposta):
        print('\nVocê venceu')
    else:
        print('\nVocê perdeu')


def exibe_numeros_apostas(numbers: list, aposta: list):
    print('\nNúmeros:')
    for num in numbers:
        print(f'- {num}')
    print(f'\nSua aposta: {", ".join(map(str, aposta))}')


def resultado_mult(numbers: list, aposta: list) -> bool:
    return any(num in aposta for num in numbers)


def opcoes_aposta() -> int:
    '''Retorna a resposta do tipo de aposta.'''
    return int(input('\nDefina o tipo de aposta:\n1- Número\n2- Animal\n\n'))


def tipo_sorteio() -> int:
    '''Retorna o tipo de sorteio escolhido.'''
    r = int(input("Defina o tipo de sorteio:\n1- Simples\n2- Múltiplo\n\n"))
    while r not in [1, 2]:
        print("Opção inválida")
        r = int(input("Defina o tipo de sorteio:\n1- Simples\n2- Múltiplo\n\n"))
    return r


if __name__ == "__main__":
    sorteio()
