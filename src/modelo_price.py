# -*- coding: utf-8 -*-
"""modelo_price.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JNKIdjzE5G9dzWWXk7V7N5WlYDYYxRoE
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def modelo_price(G, n_novos, m=None, aleatorio=False, min_m=1, max_m=3, preferencia=0.5):
    """
    rede G com o modelo de Price: parte preferencial, parte uniforme.

    parâmetros:
    - G: grafo inicial (NetworkX)
    - n_novos: número de novos nós a adicionar
    - m: número fixo de ligações por novo nó (ignorado se aleatorio=True)
    - aleatorio: se True, sorteia m entre min_m e max_m (inclusive)
    - preferencia: proporção das ligações feitas com anexação preferencial (entre 0 e 1)
    """
    proximo_id = max(G.nodes) + 1

    for _ in range(n_novos):
        G.add_node(proximo_id)

        # define quantas conexões esse nó terá
        if aleatorio:
            m_atual = random.randint(min_m, min(max_m, len(G.nodes) - 1))
        else:
            m_atual = min(m, len(G.nodes) - 1)

        # separa quantidade de conexões preferenciais e uniformes
        m_pref = int(preferencia * m_atual)
        m_uni = m_atual - m_pref

        # nós existentes, sem o novo nó
        nos_existentes = [n for n in G.nodes if n != proximo_id]

        # anexação preferencial
        alvos_pref = []
        if m_pref > 0:
            graus = np.array([G.degree(n) for n in nos_existentes])
            if graus.sum() == 0:
                alvos_pref = random.sample(nos_existentes, m_pref)
            else:
                probs = graus / graus.sum()
                alvos_pref = list(np.random.choice(nos_existentes, size=m_pref, replace=False, p=probs))

        # anexação uniforme
        alvos_restantes = list(set(nos_existentes) - set(alvos_pref))
        alvos_uni = random.sample(alvos_restantes, min(m_uni, len(alvos_restantes)))

        # adiciona as arestas
        for alvo in alvos_pref + alvos_uni:
            G.add_edge(proximo_id, alvo)

        proximo_id += 1

    return G

# redes iniciais
G_fixo = nx.complete_graph(10)
G_aleat = nx.complete_graph(10)

# modelo de Price
G_fixo = modelo_price(G_fixo, n_novos=90, m=3, preferencia=0.6, aleatorio=False)
G_aleat = modelo_price(G_aleat, n_novos=90, aleatorio=True, min_m=1, max_m=4, preferencia=0.6)

# visualização e análise
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

nx.draw(G_fixo, with_labels=False, node_color='lightblue', node_size=50, ax=axs[0, 0])
axs[0, 0].set_title("Modelo de Price (m fixo = 3)")

nx.draw(G_aleat, with_labels=False, node_color='lightgreen', node_size=50, ax=axs[0, 1])
axs[0, 1].set_title("Modelo de Price (m aleatório 1–4)")

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
    print("Diâmetro:", nx.diameter(G))

imprimir_metricas(G_fixo)
imprimir_metricas(G_aleat)