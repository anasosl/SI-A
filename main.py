import algorithm

estate_origin = input("\nEm qual estação você está?\n")

estate_destination = input("\nPara qual estação você deseja ir?\n")

melhor_caminho = algorithm.heuristic_search(estate_origin, estate_destination)