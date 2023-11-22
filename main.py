import algorithm
import treatring_data as t_data

station_origin = t_data.get_number(input("\nEm qual estação você está?\n"))

line_origin = t_data.get_line(station_origin, "origem")

station_destination = t_data.get_number(input("\nPara qual estação você deseja ir?\n"))

line_destination = t_data.get_line(station_destination, "destino")

try:
    melhor_caminho, time = algorithm.heuristic_search(station_origin,
                                                  station_destination,
                                                  line_origin,
                                                  line_destination)
except TypeError:
    print("Error")

a = melhor_caminho

print(f"\n\nO melhor caminho é visitando as seguintes estações: {str(a)[1:-1]}. O tempo total da viagem será: {time} minutos.")

