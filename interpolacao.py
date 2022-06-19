msg = """
Olá, {nome}.
Tem interesse em comprar novas {produto}?

Nosso produto é ótimo para resolver {texto}.

Aproveite, acesse agora mesmo {link} e aproveite a nossa promoção!

Apenas {qtd} unidade disponível!

Preço promocional de APENAS R${valor:.2f}"""

nomes = ['Jorge', 'Elias', 'João']
for nome in nomes:
    print(msg.format(nome=nome, produto='caneta', texto='problemas com escrita', link='http://belascanetas.com.br', qtd=1, valor=29.90))
    