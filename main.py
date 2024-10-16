import json
import cx_Oracle

def conectar_oracle():
    try:
        connection = cx_Oracle.connect("teste", "123", "oracle-server:1521/db")
        print("Conexão bem-sucedida ao Oracle!")
        return connection
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao Oracle: {e}")
        return None

def calcular_irrigacao(umidade, area):
    if umidade < 30:
        return area * 0.75 
    elif 30 <= umidade <= 60:
        return area * 0.5 
    else:
        return area * 0.25 

def salvar_dados_irrigacao(arquivo, dados):
    try:
        with open(arquivo, 'w') as file:
            json.dump(dados, file)
            print(f"Dados de irrigação salvos em {arquivo}.")
    except IOError as e:
        print(f"Erro ao salvar arquivo JSON: {e}")

def ler_sensores():
    sensores = []
    while True:
        try:
            id_sensor = int(input("ID do sensor: "))
            umidade = float(input("Umidade (%): "))
            area = float(input("Área (m²): "))
            sensores.append({"id": id_sensor, "umidade": umidade, "area": area})
            continuar = input("Deseja inserir outro sensor? (s/n): ").lower()
            if continuar != 's':
                break
        except ValueError as e:
            print(f"Entrada inválida: {e}")
    return sensores


def registrar_dados_banco(connection, dados):
    try:
        cursor = connection.cursor()
        for dado in dados:
            query = "INSERT INTO irrigacao (sensor_id, umidade, area, agua_necessaria) VALUES (:1, :2, :3, :4)"
            cursor.execute(query, (dado['id'], dado['umidade'], dado['area'], dado['agua_necessaria']))
        connection.commit()
        print("Dados registrados no banco Oracle.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao registrar dados no banco: {e}")

def main():
    connection = conectar_oracle()
    if not connection:
        return

    sensores = ler_sensores()
    dados_irrigacao = []

    for sensor in sensores:
        agua_necessaria = calcular_irrigacao(sensor['umidade'], sensor['area'])
        sensor['agua_necessaria'] = agua_necessaria
        dados_irrigacao.append(sensor)

    salvar_dados_irrigacao('dados_irrigacao.json', dados_irrigacao)

    registrar_dados_banco(connection, dados_irrigacao)

    connection.close()

main()
