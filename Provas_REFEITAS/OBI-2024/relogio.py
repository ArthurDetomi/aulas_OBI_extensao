H = int(input())
M = int(input())
S = int(input())

T = int(input())


horas_para_seg = H * 3600
minutos_para_seg = M * 60

hora_inicio_segundos = horas_para_seg + minutos_para_seg + S + T


min_T = hora_inicio_segundos // 60

seg_T = hora_inicio_segundos - (min_T * 60)

hora_T = min_T // 60

min_T = min_T - (hora_T * 60)

hora_final = hora_T % 24


print(hora_final)
print(min_T)
print(seg_T)

