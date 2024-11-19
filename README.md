Projeto de Automação Residencial via Modbus TCP/IP com Python e Banco de Dados
Este projeto visa desenvolver um sistema de automação industrial utilizando CLPs (Controladores Lógicos Programáveis) e o protocolo Modbus TCP/IP para controlar e monitorar dispositivos domésticos. O sistema se comunica com os dispositivos conectados ao CLP, permitindo o controle de iluminação, temperatura, segurança e outros sistemas automatizados, além de armazenar os dados coletados em um banco de dados para análise posterior.

Objetivo
O objetivo deste projeto é fornecer uma solução acessível para automação residencial, onde o usuário pode monitorar e controlar os dispositivos conectados ao CLP de forma automática. O sistema permite a leitura de registradores e memórias (coils) para acompanhar o estado de dispositivos como lâmpadas, sensores e atuadores, e a escrita em registradores e memórias para acionar ou desativar dispositivos conforme necessário.

Funcionalidades
- Monitoramento em Tempo Real: Leitura contínua de estados de sensores e atuadores conectados ao CLP.
- Controle Automático de Dispositivos: Escrita em registradores e memórias (coils) do CLP para acionar ou desativar dispositivos (luzes, ventiladores, travas, etc.).
- Armazenamento de Dados: Todos os dados lidos dos dispositivos são armazenados em um banco de dados - - - para registro histórico e análise futura.
- Adaptável a Diversos CLPs: Suporte ao protocolo Modbus TCP/IP, amplamente utilizado em sistemas de automação.
- Requisitos
- Ferramentas e Tecnologias
- Para rodar este projeto, você precisará das seguintes ferramentas e bibliotecas instaladas:

Python 3.x: O projeto é desenvolvido em Python.
CLP compatível com Modbus TCP/IP: Um CLP configurado para comunicar via Modbus TCP/IP para o controle e monitoramento de dispositivos.
Banco de Dados: O projeto usa SQLite por padrão, mas pode ser facilmente adaptado para MySQL ou PostgreSQL.
Bibliotecas Python Necessárias
Execute o comando abaixo para instalar as dependências:

1- Execute no Terminal:
    pip install pymodbus

2- Para MySQL ou PostgreSQL, você também pode precisar de:
    pip install mysql-connector-python  # Para MySQL
    pip install psycopg2  # Para PostgreSQL

Como o Sistema Funciona
O sistema se comunica com o CLP usando o protocolo Modbus TCP/IP para:

- Monitorar o Estado dos Dispositivos: Leitura contínua dos registradores e memórias (coils) do CLP, que podem estar ligados a lâmpadas, sensores de temperatura, sensores de presença, entre outros dispositivos.

- Controlar Dispositivos de Forma Automática: O sistema pode ativar ou desativar dispositivos residenciais enviando comandos de escrita para o CLP. Por exemplo, acender uma luz ou abrir uma porta.

- Armazenar Dados para Análise: Cada leitura do CLP é registrada em um banco de dados, permitindo a  análise de dados históricos, como o uso de energia ou o comportamento de sensores ao longo do tempo.



Para mais informações pode entrar em contato pelo email devcarlos24@gmail.com
