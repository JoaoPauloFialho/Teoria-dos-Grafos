from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError("Vértice {} não existe no grafo".format(V))

        v_obj = self.get_vertice(V)
        i_v = self.indice_do_vertice(v_obj)
        arestas = []
        for j in range(len(self.vertices)):
            for a in self.matriz[i_v][j]:
                aresta = self.matriz[i_v][j][a]
                arestas.append(aresta)
        return arestas
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        E = []

        for i in range(len(self.vertices)):
            linha = []

            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) >= 1:
                    linha.append(1)
                else:
                    linha.append(0)

            E.append(linha)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):

                if E[j][i] == 1:
                    for k in range(len(self.vertices)):
                        E[j][k] = E[j][k] if E[j][k] > E[i][k] else E[i][k]
        return E

    def ordenacao_vertices_fonte(self):
        """
        Função para encontrar os vértices fonte
        :return: lista com vértices fonte
        """
        vertices = []
        for i in range(len(self.vertices)):
            vertice_fonte = True

            for j in range(len(self.vertices)):
                if len(self.matriz[j][i]) != 0:
                    vertice_fonte = False

            if vertice_fonte:
                vertices.append(self.vertices[i].rotulo)

        return vertices

    def khan(self):
        """
        Algoritmo de khan para realizar a ordenação topológica de um grafo
        :return: Lista ordenada dos vértices
        """
        grafo_khan = deepcopy(self)
        ordenacao = []

        while len(grafo_khan.vertices) != 0:
            vertices_fonte = grafo_khan.ordenacao_vertices_fonte()

            for i in vertices_fonte:
                arestas = grafo_khan.arestas_sobre_vertice(i)

                for j in arestas:
                    grafo_khan.remove_aresta(j.rotulo)

                grafo_khan.remove_vertice(i)
                ordenacao.append(i)

        return ordenacao