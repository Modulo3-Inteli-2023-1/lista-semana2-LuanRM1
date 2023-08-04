#  Se achar necessario, faça import de outras bibliotecas





# Crie a função que será avaliada no exercício aqui

def is_anagram(palavra1, palavra2):
    if len(palavra1) != len(palavra2):
        return False
    palavra1 = sorted(palavra1)
    palavra2 = sorted(palavra2)
    if palavra1 == palavra2:
        return True
    else:
        return False





# Teste a sua função aqui (caso ache necessário)









