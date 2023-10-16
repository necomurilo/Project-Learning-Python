"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim) (or, and, not)
    <- Contagem de complexidade (ruim)
"""
velocidade = 70  # velocidade atual do carro
local_carro = 90  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima permitida
LOCAL_1 = 100  # local onde está o radar
RADAR_RANGE = 1  # alcance do radar

vel_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 =  local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = vel_carro_passou_radar_1 and vel_carro_passou_radar_1

if vel_carro_passou_radar_1:
    print('Velocidade carro passou do radar rodoviário')

if carro_multado_radar_1:
    print('Carro passou radar rodoviário')

if carro_multado_radar_1 and vel_carro_passou_radar_1:
    print('O carro foi multado no radar 3.753')