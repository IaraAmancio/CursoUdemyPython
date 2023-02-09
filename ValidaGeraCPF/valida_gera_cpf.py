from random import randint

def funcValidarCPF(cpf) -> bool:
    try:

        numeros = str(cpf).replace('.','').replace('-','').replace(' ','')

        if digitosIguais(numeros):
            return False

        if len(numeros) == 11:

            primeiroDigito = gerarDigito1(numeros)
            segundoDigito = gerarDigito2(numeros)

            if ((str(primeiroDigito) == numeros[-2]) and (str(segundoDigito) == numeros[-1])):
                return True
            else:
                return False

        else:
            return False

    except Exception as e:
        print('erro')

def gerarDigito1(cpf) -> int:
    soma = 0
    sequencia = [10,9,8,7,6,5,4,3,2]
    for i, n in enumerate(sequencia):
        soma += n * int(cpf[i])

    primeiro_digito = 11 - (soma % 11) if (soma % 11) >= 2 else 0
    return primeiro_digito

def gerarDigito2(cpf) -> int:
    soma = 0
    sequencia = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i, n in enumerate(sequencia):
        soma += n * int(cpf[i])

    segundo_digito = 11 - (soma % 11) if (soma % 11) >= 2 else 0
    return segundo_digito

def digitosIguais(cpf) -> bool:
    for i in range(0, 9):
        if str(cpf).count(str(i)) == 11:
            return True
    return False



def funcGerarCPF() -> str:
    numeros = []
    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))

    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))

    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))
    numeros.append(str(randint(0,9)))


    numeros.append(str(gerarDigito1(''.join(numeros))))
    numeros.append(str(gerarDigito2(''.join(numeros))))

    numeros.insert(3,'.')
    numeros.insert(7,'.')
    numeros.insert(11,'-')

    numeros = ''.join(numeros)

    return str(numeros)

