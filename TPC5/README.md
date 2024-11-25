# Relatório do TPC5
## Data: 2024.10.07
## Autor: Maria Carneiro a107242

## Resumo 
 
O TPC5 consistiu na criação de uma aplicação em Python para gestão de um conjunto de salas de cinema de um centro comercial. Nesse centro comercial existem algumas salas de cinema (que poderão estar a exibir filmes ou não), cada sala tem uma determinada lotação, uma lista com a referência dos bilhetes vendidos (lugares ocupados; cada lugar é identificado por um número inteiro), e cada sala tem um filme associado.

Para a execução do mesmo elaborei um menu com as seguintes opções, onde todas elas remetem para uma função específica.
* Criar sala
* Remover Sala
* Listar Salas: lista todas as salas existente no cinema
* Lugares Disponíveis: que dá como resultado False se o lugar lugar já estiver ocupado na sala onde o filme está a ser exibido e dará como resultado True se o inverso acontecer;
* Vender bilhetes: que dá como resultado um novo cinema resultante de acrescentar o lugar à lista dos lugares ocupados, na sala onde está a ser exibido o filme;
* Sair: permite fechar a aplicação.

