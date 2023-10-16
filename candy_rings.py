print('---------------------------------------------------')

# Pegar as entradas do total de doces e quantas posições cada jogador quer andar
total_candies = int(input('Digite o número total de doces: '))
player1_length = int(input('Digite quantas posições tu quer andar Kleitin: '))
player2_length = int(input('Digite quantas posições tu quer andar Marquin: '))

print('---------------------------------------------------')

# Verificar se o número de posições que cada jogador quer andar é maior que o número total de doces
if(player1_length > total_candies or player2_length > total_candies):
    print('O número escolhido não pode ser maior que o número total de doces.')
    exit()

# Criar uma lista com todos os doces
candies = list(range(1, total_candies + 1))

# Inicializar as posições dos jogadores
player1_pos = player1_length - 1
player2_pos = total_candies - player2_length
all_candies = total_candies

# Inicializar as variáveis de soma de doces
player1_candies_sum = 0
player2_candies_sum = 0
common_candies_sum = 0

while candies:
    # Armazenar as posições dos doces que cada jogador pegou
    player1_candie = candies[player1_pos]
    player2_candie = candies[player2_pos]

    # Verificar se os doces que cada jogador pegou são iguais
    if player1_candie == player2_candie:
        candies.remove(player1_candie)
        common_candies_sum += 1
        print('Posição do Xandim:', player1_candie)
    else:
        candies.remove(player1_candie)
        candies.remove(player2_candie)
        player1_candies_sum += 1
        player2_candies_sum += 1
        print('Posição do Kleitim:',player1_candie, '|', 'Posição do Marquim:', player2_candie)

    # Esse bloco atualiza as posições dos jogadores a cada rodada
    total_candies = len(candies)
    if total_candies > 0:
        if player1_length > total_candies and total_candies <= all_candies/2:
            player1_pos -= 1

        if total_candies <= all_candies/2:
            if player2_length > total_candies:
                player2_pos -= 1
            player2_pos += 1
        
        player1_pos = (player1_pos + player1_length - 1) % total_candies
        player2_pos = (player2_pos - player2_length - 1) % total_candies

print('---------------------------------------------------')

# Fim do while caso a lista de doces esteja vazia
print('FIM DE JOGOOOO!')

print('---------------------------------------------------')

# Imprimir o total de doces que cada jogador pegou
print('Total de doces do Kleitim:', player1_candies_sum)
print('Total de doces do Marquim:', player2_candies_sum)
print('Total de doces do Xandim:', common_candies_sum)

print('---------------------------------------------------')

