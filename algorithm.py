import data

def linha_comum(a,b):
  return [x for x in a if x in b]

def astar(o, d, line_o, line_d):
  cur_station = o
  cur_line = line_o

  print("\n Ordem da fronteira: [f, g, estação, precursor, linha]")
  #[f, g, cur_station, precursor, linha]
  frontiers = [[0,0, cur_station, o, line_o]]
  f = 0
  g = 0
  i = 0
  path = []
  visited = []
  predecessor = {}

  while (cur_station != d or cur_line != line_d):
    i += 1
    frontiers.sort()
    print(f"\nA {i}ª fronteira é {frontiers}")
    g = frontiers[0][1]
    cur_station = frontiers[0][2]

    predecessor.update({cur_station: frontiers[0][3]})
    cur_line = frontiers[0][4]
    frontiers.pop(0)
    visited.append(cur_station)

    if (cur_station == d):
      path.append(d)
      c = predecessor[d]
      path.append(c)
      while (predecessor[c] != o):
        c = predecessor[c]
        path.append(c)

      if (path[-1] != o):
        path.append(o)
      path.reverse()

      #baldeação final
      if (cur_line != line_d):
        g += 4
      return path, g

    for s in data.distancias_reais[cur_station-1]:
      if ((s not in visited)):

        g1 = g + data.get_time(data.distancias_reais[cur_station-1][s])
        f = g1 + data.get_time(data.distancias_diretas[cur_station-1][d-1])

        if (cur_line not in data.estacoes_linhas[s-1]):
          f = f + data.tempo_baldeacao
          g1 = g1 + data.tempo_baldeacao
          line = linha_comum(data.estacoes_linhas[cur_station-1], data.estacoes_linhas[s-1])
          frontiers.append([round(f,2), round(g1,2), s, cur_station, line[0]])

        else:
          frontiers.append([round(f,2), round(g1,2), s, cur_station, cur_line])

def heuristic_search(e_origin, e_destination, l_origin, l_destination):
  o = int(e_origin)
  d = int(e_destination)

  return astar(o, d, l_origin, l_destination)


