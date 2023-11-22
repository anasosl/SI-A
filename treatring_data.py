import data

def get_number(string):
    try: 
        string = string.split(" ")
        if (string[1][0] == "E" or string[1][0] == "e"):
            string = string[1][1:]
        else:
            ans = int(string[1]) 
    except:
        if (type(string) != int and (string[0] == "E" or string[0] == "e")):
            ans = int(string[1:])
        elif (type(string) != int):
          ans = int(string[0]) 
        else: 
          ans = string
          
    return int(ans)

def get_line(s_o, type_stantion):
  s_origin = get_number(s_o)
  question = (f"\nA sua estação de {type_stantion} tem as seguintes linhas: ")
  if (len(data.estacoes_linhas[s_origin-1]) > 1):
    for l in data.estacoes_linhas[s_origin-1]:
      if (l == data.estacoes_linhas[s_origin-1][-1]):
        question += " e " + l + ". "
      elif (l == data.estacoes_linhas[s_origin-1][-2]):
        question += l
      else:
        question += l + ", "
    if (type_stantion == "origem"):
       question += "Qual dessas você está?\n"
    else:
       question += "Para qual dessas você quer ir?\n"
    return input(question)
  else:
    print(f"\nSua linha de {type_stantion} é a {data.estacoes_linhas[s_origin-1][0]}!")
    return data.estacoes_linhas[s_origin-1][0]