# -*- coding: utf-8 -*-
"""modelo_preferencial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sGCawXY_Pln-UvHYXq3vhkfRVQKZg6Q8
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def anexacao_preferencial(G, n_novos, m=None, aleatorio=False, min_m=1, max_m=3):
    """
    rede G com anexação preferencial (modelo Barabási-Albert).

    parâmetros:
    - G: grafo inicial (NetworkX)
    - n_novos: número de novos nós a adicionar
    - m: número fixo de ligações por novo nó (ignorado se aleatorio=True)
    - aleatorio: se True, sorteia m entre min_m e max_m (inclusive)
    - min_m, max_m: limites de sorteio de m
    """
    proximo_id = max(G.nodes) + 1

    for _ in range(n_novos):
        G.add_node(proximo_id)

        # define quantas conexões esse nó terá
        if aleatorio:
            m_atual = random.randint(min_m, min(max_m, len(G.nodes) - 1))
        else:
            m_atual = min(m, len(G.nodes) - 1)

        # calcular graus acumulados para anexação preferencial
        graus = np.array([G.degree(n) for n in G.nodes if n != proximo_id])
        nos_existentes = [n for n in G.nodes if n != proximo_id]

        if graus.sum() == 0:
            # todos com probabilidade igual se graus forem todos zero
            alvos = random.sample(nos_existentes, m_atual)
        else:
            probabilidades = graus / graus.sum()
            alvos = np.random.choice(nos_existentes, size=m_atual, replace=False, p=probabilidades)

        for alvo in alvos:
            G.add_edge(proximo_id, alvo)

        proximo_id += 1

    return G

# grafo inicial completamente conectado
G_fixo = nx.complete_graph(10)
G_fixo = anexacao_preferencial(G_fixo, n_novos=90, m=3, aleatorio=False)

G_aleat = nx.complete_graph(10)
G_aleat = anexacao_preferencial(G_aleat, n_novos=90, aleatorio=True, min_m=1, max_m=4)

# metricas
def imprimir_metricas(G):
    graus = [grau for _, grau in G.degree()]
    print("Número de nós:", G.number_of_nodes())
    print("Número de arestas:", G.number_of_edges())
    print("Grau médio:", np.mean(graus))
    print("Clustering médio:", nx.average_clustering(G))
    print("Componentes conexas:", nx.number_connected_components(G))
    print("Desvio padrão dos graus:", np.std(graus))
    print("Densidade:", nx.density(G))
    print("Caminho médio:", nx.average_shortest_path_length(G))
    print("Diâmetro:\n", nx.diameter(G))


imprimir_metricas(G_fixo)
imprimir_metricas(G_aleat)


# visualização
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

nx.draw(G_fixo, with_labels=False, node_color='lightblue', node_size=50, ax=axs[0, 0])
axs[0, 0].set_title("Anexação preferencial (m fixo = 3)")

nx.draw(G_aleat, with_labels=False, node_color='lightgreen', node_size=50, ax=axs[0, 1])
axs[0, 1].set_title("Anexação preferencial (m aleatório 1–4)")

graus_fixo = [grau for _, grau in G_fixo.degree()]
graus_aleat = [grau for _, grau in G_aleat.degree()]

axs[1, 0].hist(graus_fixo, bins=range(min(graus_fixo), max(graus_fixo)+2), align='left', color='skyblue', edgecolor='black')
axs[1, 0].set_title("Distribuição de graus (m fixo)")
axs[1, 0].set_xlabel("Grau")
axs[1, 0].set_ylabel("Número de nós")

axs[1, 1].hist(graus_aleat, bins=range(min(graus_aleat), max(graus_aleat)+2), align='left', color='lightgreen', edgecolor='black')
axs[1, 1].set_title("Distribuição de graus (m aleatório)")
axs[1, 1].set_xlabel("Grau")
axs[1, 1].set_ylabel("Número de nós")

plt.tight_layout()
plt.show()