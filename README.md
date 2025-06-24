# Modelagem de Redes - Trabalho A2 (Capítulo 3)

Este repositório contém o trabalho da disciplina **Introdução à Modelagem (2025.1)** da EMAp, ministrada pelo Prof. Walter Sande. O objetivo é implementar e analisar diferentes modelos de geração e crescimento de redes, além de comparar suas propriedades.

## Descrição do Trabalho

O trabalho está dividido em duas partes principais:

### Parte A: Modelos de Geração de Redes
1. **Modelo de Erdős-Rényi (Rede Aleatória)**: Gera uma rede onde cada aresta é criada com uma probabilidade fixa `p`.
2. **Modelo de Watts-Strogatz (Mundo Pequeno)**: Parte de uma rede regular em anel e redireciona arestas com uma probabilidade dada.
3. **Rede Aleatória com Comunidades**: Similar ao modelo de Erdős-Rényi, mas com probabilidades diferenciadas para ligações dentro e entre comunidades.

### Parte B: Modelos de Crescimento de Redes
1. **Modelo de Anexação Uniforme**: Novos nós se conectam a nós existentes com probabilidade uniforme.
2. **Modelo de Barabási-Albert (Anexação Preferencial)**: Novos nós preferem se conectar a nós já bem conectados.
3. **Modelo de Price**: Combina anexação preferencial e uniforme, com uma proporção ajustável.

### Tarefa Adicional (Item 2)
Análise comparativa de quatro redes pré-definidas (Redes A, B, C e D) usando medidas de centralidade (grau, closeness, betweenness e PageRank) para nós específicos.

## Requisitos
- Python (com bibliotecas como NetworkX, Matplotlib, NumPy) ou MATLAB.

## Estrutura do Repositório
- `src/`: Códigos para gerar e analisar os modelos.
  - `erdos_renyi.py`
  - `watts_strogatz.py`
  - `rede_comunidades.py`
  - `modelo_uniforme.py`
  - `modelo_preferencial.py`
  - `modelo_price.py`
  - `rede_item2.py`
- `data/`: Arquivos de dados, como `redes.xlsx` com as listas de arestas.
- `results/`: Visualizações, gráficos e métricas calculadas.
- `report/`: Relatório detalhando metodologia, análises e conclusões.
## Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/aliicerabello/trabalho-redes.git]
