#Projeto de Escalonador de Processos 

Disciplina: 

Algoritmos e Estrutura de Dados I 

Professor: 

Dimmy Magalhães 

Aluno: 

Enzo Lacerda de Santana 

Repositório: 

https://github.com/IRONIA-Charger/icevos-scheduler.git 

 

1. Descrição do Projeto 

Esse projeto consiste na implementação de um escalonador fictício chamado “ICEVOS”. Ele é responsável por permitir quem irá ser executado, e utilizar a CPU no momento.  Aplicando regras para prevenir a inanição (starvation) de processos menos importantes. 

 

2. Estruturas de Dados e Funcionalidades 

O projeto utiliza e implementa as seguintes estruturas e lógicas, baseado no contexto do trabalho: 

Classe Processo: Uma estrutura básica que representa um processo com atributos como ID, nome, prioridade (1, 2 ou 3), ciclos necessários e recurso requerido (DISCO ou nulo). 

Classe ListaProcesso: Uma implementação de lista encadeada, criada do zero para gerenciar a fila de processos 

Classe Scheduler: A lógica central do escalonador, que gerencia as filas de alta, média e baixa prioridade, além de uma fila para processos bloqueados. 

Lógica de Escalonamento: O Scheduler executa os processos com base em suas prioridades. 

Lógica da Anti-Inanição: A cada 5 ciclos de alta prioridade, a CPU é obrigatoriamente a executar um processo de média ou baixa prioridade 

Gerenciamento de Recursos (Bloqueio): Processos que precisam do recurso "DISCO" são movidos para uma lista de bloqueados e reinseridos em sua fila de origem no ciclo seguinte. 

3. Como Executar o Projeto 

Para executar a simulação do escalonador, siga os passos abaixo: 

Pré-requisitos: 

Python 3.10.11 ou superior instalado. 

Instruções: 

Clone este repositório para o seu ambiente local: git clone https://github.com/IRONIA-Charger/icevos-scheduler.git 

Navegue até a pasta do projeto: cd icevos-scheduler

Execute o arquivo principal a partir do terminal: python simulador.py 

A saída da simulação será exibida diretamente no console, detalhando a execução de cada ciclo e o estado de todas as listas. 

4. Estrutura do Repositório  

 simulador.py: Contém o código-fonte principal do projeto, incluindo as classes Processo, ListaProcessos, Scheduler e a Main. 

relatorio_analise.pdf: O relatório em PDF com a análise técnica do projeto. 

README.md: Este arquivo de documentação. 

