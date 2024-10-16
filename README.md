Descrição do Projeto
Este projeto tem como objetivo monitorar dados de sensores de umidade do solo e calcular a quantidade de água necessária para a irrigação de áreas agrícolas. A solução visa otimizar o uso da água, garantindo que a irrigação seja eficiente, baseada nos dados coletados dos sensores, e evitando desperdícios.

O sistema coleta dados de umidade e área coberta pelos sensores, realiza cálculos para determinar a quantidade de irrigação necessária, salva os dados em arquivos JSON e registra os mesmos em um banco de dados Oracle para armazenamento e análise futura.

Funcionalidades
Leitura de Sensores: O sistema simula a leitura de sensores que medem a umidade do solo e a área coberta.
Cálculo de Irrigação: Com base nos níveis de umidade, o sistema calcula a quantidade de água necessária para cada área.
Armazenamento de Dados: Os dados são armazenados localmente em um arquivo JSON para facilitar consultas posteriores.
Registro no Banco de Dados: Os dados de irrigação são registrados em um banco de dados Oracle, permitindo controle e auditoria do processo de irrigação.