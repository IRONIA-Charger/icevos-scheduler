import os
# -------------------------
# Classe Processo (nó da lista)

class Processo:
    def __init__(self, id, prioridade, nome, ciclos_necessarios, recurso_necessario=None):
        self.id = id
        self.nome = nome
        self.prioridade = prioridade  # 1=Alta, 2=Média, 3=Baixa
        self.ciclos_necessarios = ciclos_necessarios
        self.recurso_necessario = recurso_necessario
        self.proximo = None  # ponteiro para o próximo processo


# -------------------------
# Lista encadeada simples

class ListaProcessos:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.primeiro is None

    def adicionarFinal(self, processo):
        if self.esta_vazia():
            self.primeiro = self.ultimo = processo
        else:
            self.ultimo.proximo = processo
            self.ultimo = processo
        self.tamanho += 1

    def removerInicio(self):
        if self.esta_vazia():
            return None
        removido = self.primeiro
        self.primeiro = self.primeiro.proximo
        if self.primeiro is None:
            self.ultimo = None
        self.tamanho -= 1
        removido.proximo = None  # limpa referência
        return removido

    def mostrarLista(self):
        if self.esta_vazia():
            print("Lista vazia")
            return
        atual = self.primeiro
        while atual:
            print(f"[P{atual.id}-{atual.nome}]", end=" → ")
            atual = atual.proximo
        print("None")
#-----------
#Scheduler
        
class Scheduler:
    def __init__(self):
        self.lista_alta = ListaProcessos()
        self.lista_media = ListaProcessos()
        self.lista_baixa = ListaProcessos()
        self.lista_bloqueados = ListaProcessos()
        self.ciclo = 0
        self.cont_alta = 0

    def adicionar(self, p):
        if p.prioridade == 1:
            self.lista_alta.adicionarFinal(p)
        elif p.prioridade == 2:
            self.lista_media.adicionarFinal(p)
        elif p.prioridade == 3:
            self.lista_baixa.adicionarFinal(p)

    def mostrar_estado(self):
        print("Alta: ", end=""); self.lista_alta.mostrarLista()
        print("Média:", end=" "); self.lista_media.mostrarLista()
        print("Baixa:", end=" "); self.lista_baixa.mostrarLista()
        print("Bloq.:", end=" "); self.lista_bloqueados.mostrarLista()

    def desbloquear(self):
        if not self.lista_bloqueados.esta_vazia():
            p = self.lista_bloqueados.removerInicio()
            self.adicionar(p)
            print(f"-> Desbloqueado: P{p.id}")

    def escolher_processo(self):
        # Anti-inanição
        if self.cont_alta >= 5:
            if not self.lista_media.esta_vazia():
                self.cont_alta = 0
                return self.lista_media.removerInicio()
            elif not self.lista_baixa.esta_vazia():
                self.cont_alta = 0
                return self.lista_baixa.removerInicio()
            self.cont_alta = 0

        # Execução padrão
        if not self.lista_alta.esta_vazia():
            self.cont_alta += 1
            return self.lista_alta.removerInicio()
        elif not self.lista_media.esta_vazia():
            return self.lista_media.removerInicio()
        elif not self.lista_baixa.esta_vazia():
            return self.lista_baixa.removerInicio()
        return None

    def executar_ciclo(self):
        self.ciclo += 1
        print(f"\n--- CICLO {self.ciclo} ---")
        self.mostrar_estado()
        self.desbloquear()

        p = self.escolher_processo()
        if not p:
            print("-> CPU ociosa")
            return

        # Bloqueio por recurso
        if p.recurso_necessario == "DISCO" and not hasattr(p, "bloqueado_antes"):
            p.bloqueado_antes = True
            self.lista_bloqueados.adicionarFinal(p)
            print(f"-> P{p.id} precisa de DISCO. Bloqueado.")
            return

        # Execução normal
        p.ciclos_necessarios -= 1
        if p.ciclos_necessarios > 0:
            self.adicionar(p)
            print(f"-> P{p.id} executou, faltam {p.ciclos_necessarios} ciclos.")
        else:
            print(f"-> P{p.id}-{p.nome} TERMINOU.")
#------          
#Main
            
def main():
    s = Scheduler()
    # Obtém o caminho completo para a pasta do script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'processos.txt')

    try:
        with open(file_path, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                # Extrai os dados da linha
                id = int(dados[0])
                prioridade = int(dados[1])
                nome = dados[2]
                ciclos = int(dados[3])
                recurso = dados[4] if len(dados) > 4 else None
                
                # Cria e adiciona o processo
                proc = Processo(id, prioridade, nome, ciclos, recurso)
                s.adicionar(proc)
    except FileNotFoundError:
        print("Erro: O arquivo 'processos.txt' não foi encontrado. Verifique se ele está na mesma pasta do seu código.")
        return
    while (not s.lista_alta.esta_vazia() or
           not s.lista_media.esta_vazia() or
           not s.lista_baixa.esta_vazia() or
           not s.lista_bloqueados.esta_vazia()):
        s.executar_ciclo()

    print("\n--- FIM DA SIMULAÇÃO ---")


if __name__ == "__main__":
    main()
