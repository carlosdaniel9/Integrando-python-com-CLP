# create to carlos daniel   12/10/2024

import sqlite3
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import logging
import time

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Configurações do CLP (ajuste conforme necessário)
IP_CPL = '192.168.0.10'  # IP do CLP
PORTA_CPL = 502          # Porta Modbus padrão
INTERVALO_LEITURA = 5    # Tempo (em segundos) entre as leituras/escritas

# Conectar ao banco de dados SQLite (ou criar, se não existir)
conn = sqlite3.connect('dados_clp.db')
cursor = conn.cursor()

# Criar uma tabela para armazenar os dados, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS clp_data (
    timestamp TEXT,
    registers TEXT,
    coils TEXT
)
''')

try:
    # Iniciar conexão com o CLP
    client = ModbusTcpClient(IP_CPL, port=PORTA_CPL)
    connection = client.connect()
    
    if connection:
        print("Conectado ao CLP ", IP_CPL, " na porta ", PORTA_CPL)
        
        # Loop contínuo para leitura/escrita e inserção no banco de dados
        while True:
            try:
                # ---- Leitura de registradores (Holding Registers) ----
                # Ler 10 registradores a partir do endereço 0
                response_registers = client.read_holding_registers(0, 10, unit=1)
                
                if not response_registers.isError():
                    registers_data = str(response_registers.registers)
                    print("Registradores lidos: ", registers_data)
                else:
                    print("Erro ao ler registradores")
                    registers_data = "Erro"
                
                # ---- Leitura de memória (Coils) ----
                # Ler 8 bits de memória (coils) a partir do endereço 0
                response_coils = client.read_coils(0, 8, unit=1)
                
                if not response_coils.isError():
                    coils_data = str(response_coils.bits)
                    print("Memórias lidas (Coils): ", coils_data)
                else:
                    print("Erro ao ler memórias (coils)")
                    coils_data = "Erro"
                
                # ---- Inserção dos dados no banco de dados ----
                timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
                cursor.execute('INSERT INTO clp_data (timestamp, registers, coils) VALUES (?, ?, ?)',
                               (timestamp, registers_data, coils_data))
                conn.commit()  # Salvar mudanças no banco de dados
                
                # ---- Escrita em registradores (Holding Registers) ----
                # Escrever o valor 500 no registrador de endereço 1
                write_register = client.write_register(1, 500, unit=1)
                
                if not write_register.isError():
                    print("Valor 500 escrito no registrador de endereço 1")
                else:
                    print("Erro ao escrever no registrador")
                
                # ---- Escrita em memória (Coils) ----
                # Escrever o valor True no bit de memória (coil) no endereço 0
                write_coil = client.write_coil(0, True, unit=1)
                
                if not write_coil.isError():
                    print("Valor True escrito na memória (coil) endereço 0")
                else:
                    print("Erro ao escrever na memória (coil)")
                
                # Esperar por um tempo antes da próxima iteração
                time.sleep(INTERVALO_LEITURA)

            except KeyboardInterrupt:
                print("Execução interrompida pelo usuário.")
                break

    else:
        print("Falha ao conectar ao CLP")

except ModbusException as e:
    print("Erro Modbus: ", e)

finally:
    # Fechar a conexão
    client.close()
    print("Conexão com CLP fechada")
    
    # Fechar a conexão com o banco de dados
    conn.close()
    print("Conexão com banco de dados fechada")
