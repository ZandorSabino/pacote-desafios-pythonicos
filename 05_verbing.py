"""
05. verbing

Dada uma string, se seu tamanho for pelo menos 3,
adicione 'ing' no seu fim, a menos que a string
já termine com 'ing', nesse caso adicione 'ly'.

Se o tamanho da string for menor que 3, não altere nada.

Retorne o resultado da string.
"""

def verbing(s):
    '''Alternativa
    if len(s) >= 3:
        if 'ing' in s[-3:]:
            s = ''.join([s,'ly'])
        else:
            s = ''.join([s,'ing'])
    return s
    '''

    #return s if len(s) < 3 else ''.join([s,'ly']) if 'ing' in s[-3:] else ''.join([s,'ing'])
    return s if len(s) < 3 else ''.join([s,'ly']) if s.endswith('ing') else ''.join([s,'ing'])

# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(verbing, 'hail', 'hailing')
    test(verbing, 'swiming', 'swimingly')
    test(verbing, 'do', 'do')
