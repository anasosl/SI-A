#[index+1][]: origem, [][index+1]: destino, valor: distancia 
distancias_diretas = [[0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6, 9.1, 16.7, 27.3, 27.6, 29.8],
                      [10, 0, 8.5, 14.8, 26.6, 29.1, 26.1, 17.3, 10, 3.5, 15.5, 20.9, 19.1, 21.8], 
                      [18.5, 8.5, 0, 6.3, 18.2, 20.6, 17.6, 13.6, 9.4, 10.3, 19.5, 19.1, 12.1, 16.6], 
                      [24.8, 14.8, 6.3, 0, 12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4], 
                      [36.4, 26.6, 18.2, 12, 0, 3, 2.4, 19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9], 
                      [38.8, 29.1, 20.6, 14.4, 3, 0, 3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2], 
                      [35.8, 26.1, 17.6, 11.5, 2.4, 3.3, 0, 20, 23, 27.3, 34.2, 25.7, 12.4, 15.6], 
                      [25.4, 17.3, 13.6, 12.4, 19.4, 22.3, 20, 0, 8.2, 20.3, 16.1, 6.4, 22.7, 27.6], 
                      [17.6, 10, 9.4, 12.6, 23.3, 25.7, 23, 8.2, 0, 13.5, 11.2, 10.9, 21.2, 26.6], 
                      [9.1, 3.5, 10.3, 16.7, 28.2, 30.3, 27.3, 20.3, 13.5, 0, 17.6, 24.2, 18.7, 21.2], 
                      [16.7, 15.5, 19.5, 23.6, 34.2, 36.7, 34.2, 16.1, 11.2, 17.6, 0, 14.2, 31.5, 35.5], 
                      [27.3, 20.9, 19.1, 18.6, 24.8, 27.6, 25.7, 6.4, 10.9, 24.2, 14.2, 0, 28.8, 33.6], 
                      [27.6, 19.1, 12.1, 10.6, 14.5, 15.2, 12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0, 5.1], 
                      [29.8, 21.8, 16.6, 15.4, 17.9, 18.2, 15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1, 0]]


#index+1: origem, chave: vizinho, valor: distancia 
distancias_reais = [{2: 10}, #1
                    {1: 10, 3: 8.5, 9: 10, 10: 3.5}, #2
                    {2: 8.5, 4: 6.3, 9: 9.4, 13: 18.7}, #3
                    {3: 6.3, 5: 13, 8: 15.3, 13: 12.8}, #4
                    {4: 13, 6: 3, 7: 2.4, 8: 30}, #5
                    {5: 3}, #6
                    {5: 2.4}, #7
                    {4: 15.3, 5: 30, 9: 9.6, 12: 6.4}, #8
                    {2: 10, 3: 9.4, 8: 9.6, 11: 12.2}, #9
                    {2: 3.5}, #10
                    {9: 12.2}, #11
                    {8: 6.4}, #12
                    {3: 18.7, 4: 12.8, 14: 5.1}, #13
                    {13: 5.1}] #14


#index+1: origem, chave: (vizinho, linha), valor: distancia 
distancias_reais_duplo = [{(2, 'azul'): 10, (2, 'amarela'): 10},
                          {(1, 'azul'): 10, (3, 'azul'): 8.5, (3, 'vermelha'): 8.5, 
                            (9, 'amarela'): 10, (9, 'vermelha'): 10, 
                            (10, 'amarela'): 3.5},
                          {(2, 'azul'): 8.5, (2, 'amarela'): 8.5, (4, 'azul'): 6.3, 
                            (4, 'verde'): 6.3, (9, 'amarela'): 9.4, 
                            (9, 'vermelha'): 9.4, (13, 'verde'): 18.7},
                          {(3, 'azul'): 6.3, (3, 'vermelha'): 6.3, (5, 'azul'): 13, 
                            (5, 'amarela'): 13, (8, 'amarela'): 15.3, 
                            (8, 'verde'): 15.3, (13, 'verde'): 12.8, (14, 'verde'): 11, 
                            (14, 'vermelha'): 11},
                          {(4, 'azul'): 13, (4, 'verde'): 13, (6, 'azul'): 3, 
                            (7, 'amarela'): 2.4, (8, 'amarela'): 30, (8, 'verde'): 30},
                          {(5, 'azul'): 3, (5, 'amarela'): 3},
                          {(5, 'azul'): 2.4, (5, 'amarela'): 2.4},
                          {(4, 'azul'): 15.3, (4, 'verde'): 15.3, (5, 'azul'): 30, 
                            (5, 'amarela'): 30, (9, 'amarela'): 9.6, 
                            (9, 'vermelha'): 9.6, (12, 'verde'): 6.4},
                          {(2, 'azul'): 10, (2, 'amarela'): 10, (3, 'azul'): 9.4, 
                            (3, 'vermelha'): 9.4, (8, 'amarela'): 9.6, 
                            (8, 'verde'): 9.6, (11, 'vermelha'): 12.2},
                          {(2, 'azul'): 3.5, (2, 'amarela'): 3.5},
                          {(9, 'amarela'): 12.2, (9, 'vermelha'): 12.2},
                          {(8, 'amarela'): 6.4, (8, 'verde'): 6.4},
                          {(3, 'azul'): 18.7, (3, 'vermelha'): 18.7, (4, 'azul'): 12.8, 
                            (4, 'verde'): 12.8, (14, 'verde'): 5.1, (14, 'vermelha'): 5.1},
                          {(4, 'azul'): 11, (4, 'verde'): 11, (13, 'verde'): 5.1}]

#chave: linha, valor: lista de estacoes 
linhas_estacoes = {"azul": [1, 2, 3, 4, 5, 6], 
                   "amarela": [2, 5, 7, 8, 9, 10],
                   "verde": [4, 8, 12, 13, 14],
                   "vermelha": [3, 9, 11, 14]}

#index+1: estacao, valores: linhas
estacoes_linhas = [["azul"],
                   ["azul", "amarela"], 
                   ["azul", "vermelha"], 
                   ["azul", "verde"], 
                   ["azul", "amarela"], 
                   ["azul"], 
                   ["amarela"], 
                   ["amarela", "verde"], 
                   ["amarela", "vermelha"], 
                   ["amarela"], 
                   ["vermelha"], 
                   ["verde"], 
                   ["verde", "vermelha"], 
                   ["verde", "vermelha"]]

#km/min
velocidade_media = 0.5
#min
tempo_baldeacao = 4

def get_time(distance):
  return distance / velocidade_media