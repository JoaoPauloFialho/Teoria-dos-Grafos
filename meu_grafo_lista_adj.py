from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *
from bibgrafo.vertice import Vertice
from bibgrafo.aresta import Aresta


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        vertices = self.vertices
        arestas = self.arestas
        nao_adjacentes = set()


        for i in range(len(vertices)):
            vertices[i] = vertices[i].rotulo

        for v in vertices:
            vertices_nao_adjacentes_inicais = vertices[vertices.index(v):]
            vertices_nao_adjacentes_inicais.remove(v)

            if(len(vertices_nao_adjacentes_inicais) == 0):
                continue

            for a in arestas:
                aresta = arestas[a]
                if(aresta.v1.rotulo != v and aresta.v2.rotulo != v):
                    continue

                if(aresta.v1.rotulo == v):
                    if(aresta.v2.rotulo in vertices_nao_adjacentes_inicais):
                        vertices_nao_adjacentes_inicais.remove(aresta.v2.rotulo)
                    continue

                if(aresta.v2.rotulo == v):
                    if(aresta.v1.rotulo in vertices_nao_adjacentes_inicais):
                        vertices_nao_adjacentes_inicais.remove(aresta.v1.rotulo)
                    continue

            for x in vertices_nao_adjacentes_inicais:
                par = f'{v}-{x}'
                nao_adjacentes.add(par)

        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        arestas = self.arestas

        for a in arestas:
            aresta = arestas[a]

            if(aresta.v1.rotulo == aresta.v2.rotulo):
                return True

        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        arestas = self.arestas
        grau = 0
        if(not self.existe_rotulo_vertice(V)):
            raise VerticeInvalidoError("Vertice não existe no grafo")
        
        for a in arestas:
            aresta = arestas[a]

            if(aresta.v1 == aresta.v2):
                grau += 2
                continue

            if(aresta.v1.rotulo == V or aresta.v2.rotulo == V):
                grau += 1
                continue
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        arestas = self.arestas
        arestas_controle = []
        for a in arestas:

            aresta = arestas[a]

            for ac in arestas_controle:
                if(aresta.rotulo != ac.rotulo):

                    verticesA = [aresta.v1.rotulo, aresta.v2.rotulo]
                    verticesB = [ac.v1.rotulo, ac.v2.rotulo]

                    if(verticesA == verticesB):
                        return True

            arestas_controle.append(aresta)

        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if(not self.existe_rotulo_vertice(V)):
            raise VerticeInvalidoError("O vértice não existe no grafo")
        arestas = self.arestas
        asv = set()
        for a in arestas:
            if(arestas[a].v1.rotulo == V or arestas[a].v2.rotulo == V):
                asv.add(a)
        return asv

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        vertices_nao_adjacentes = self.vertices_nao_adjacentes()
        paralelas = self.ha_paralelas()
        lacos = self.ha_laco()
        if(len(vertices_nao_adjacentes) == 0 and not paralelas and not lacos):
            return True
        return False

    def dfs_aux(self, arvore_dfs, raiz):
        """
        Função auxiliar para realizar a recursão da busca em profundidade
        :param arvore_dfs: árvore dfs do grafo
        :param raiz: atual raiz a ser analisada
        :return: arvore dfs
        """
        if (not arvore_dfs.existe_rotulo_vertice(raiz)):
            arvore_dfs.adiciona_vertice(raiz)

        arestas_rotulos = list(self.arestas_sobre_vertice(raiz))
        arestas_rotulos.sort()

        for a in arestas_rotulos:
            if (raiz == self.arestas[a].v1.rotulo):
                proximo = self.arestas[a].v2.rotulo
            else:
                proximo = self.arestas[a].v1.rotulo

            if (not arvore_dfs.existe_rotulo_vertice(proximo)):
                arvore_dfs.adiciona_vertice(proximo)
                arvore_dfs.adiciona_aresta(self.arestas[a])
                self.dfs_aux(arvore_dfs, proximo)

        return arvore_dfs

    def dfs(self, raiz=''):
        """
        Faz uma busca em profundidade no grafo
        :return: retorna a árvore dfs do grafo analisado
        """
        grafo = MeuGrafo()
        if raiz == '':
            raiz = self.vertices[0].rotulo
        return self.dfs_aux(grafo, raiz)

    def bfs_aux(self, arvore_bfs, raiz):
        if(not arvore_bfs.existe_rotulo_vertice(raiz)):
            arvore_bfs.adiciona_vertice(raiz)

        arestas_rotulos = list(self.arestas_sobre_vertice(raiz))
        arestas_rotulos.sort()

        for a in arestas_rotulos:
            if(not arvore_bfs.existe_rotulo_aresta(self.arestas[a].rotulo)):
                if(self.arestas[a].v1.rotulo == raiz):
                    proximo = self.arestas[a].v2.rotulo
                else:
                    proximo = self.arestas[a].v1.rotulo

                if(not arvore_bfs.existe_rotulo_vertice(proximo)):
                    arvore_bfs.adiciona_vertice(proximo)
                    arvore_bfs.adiciona_aresta(self.arestas[a])
                    self.bfs_aux(arvore_bfs, proximo)

        return arvore_bfs

    def bfs(self, raiz=''):
        """
        Faz uma busca em profundidade no grafo
        :return: retorna a árvore bfs do grafo analisado
        :raise: Exception se o grafo possuir laços
        """
        grafo = MeuGrafo()
        if raiz == '':
            raiz = self.vertices[0].rotulo
        return self.bfs_aux(grafo, raiz)

    def dijkstra(self, vi, vf):
        """
        Descobre o caminho menos custoso entre um vértice até outro
        :param vi: vértice inicial
        :param vf: vértice final
        :return: lista com a sequência de vértices que deve ser seguida
        """
        alfa = dict()  # permanente/temporário
        beta = dict()  # peso do menor caminho do vi até o vértice
        pi = dict()  # predecessor do vértice
        analisados = []

        vertice = self.get_vertice(vi)
        alfa[vertice.rotulo] = 0
        beta[vertice.rotulo] = 0
        pi[vertice.rotulo] = "-"

        while(len(analisados) != len(self.vertices)):
            vertice = min(dict(filter(lambda a : a[0] not in analisados, beta.items())))
            arestas = self.arestas_sobre_vertice(vertice)

            for a in arestas:
                aresta = self.arestas[a]
                vertice_analise = aresta.v1.rotulo if aresta.v2.rotulo == vertice else aresta.v2.rotulo

                if vertice_analise not in alfa:
                    alfa[vertice_analise] = 0
                    beta[vertice_analise] = beta[vertice] + aresta.peso #o peso total do caminho é a soma do peso da aresta atual de análise mais todas
                    pi[vertice_analise] = vertice                       #as outras do caminho

                else:
                    novo_beta = beta[vertice] + aresta.peso
                    antigo_beta = beta[vertice_analise]
                    if(novo_beta < antigo_beta):
                        alfa[vertice_analise] = 0
                        beta[vertice_analise] = novo_beta
                        pi[vertice_analise] = vertice

            if(vertice not in analisados):
                analisados.append(vertice)
                alfa[vertice] = 1

        return self.dijkstra_fabricar_caminho(pi, vi, vf)

    def dijkstra_fabricar_caminho(self, pi, vi, vf):
        """
        Função usada para fabricar o caminho de um Vi até um Vf utilizando um pi{} do algoritmo de dijkstra
        :param pi dicionário com antecessores:
        :param vi vértice inicial:
        :param vf vértice final:
        :return lista contendo a sequência de vértices que deve ser seguida:
        """
        vertice_atual = vf
        caminho = []
        cont = 0
        while(True):
            if((vf in caminho) and (vi in caminho)):
                break
            caminho.append(vertice_atual)
            vertice_atual = pi[vertice_atual]

        return list(reversed(caminho))







