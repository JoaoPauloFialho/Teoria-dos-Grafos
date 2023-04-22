from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vertices = self.vertices
        vertices_rotulos = []
        nao_adjacentes = set()

        for v in vertices:
            vertices_rotulos.append(v.rotulo)

        for i in range(len(vertices)):
            vertices_nao_adjacentes_atuais = vertices_rotulos[i:]
            vertices_nao_adjacentes_atuais.remove(vertices[i].rotulo)
            for j in range(len(vertices)):

                arestas = self.matriz[i][j]
                for a in arestas:
                    aresta = arestas[a]

                    if(aresta.v1 == vertices[i]):
                        if(aresta.v2.rotulo in vertices_nao_adjacentes_atuais):
                            vertices_nao_adjacentes_atuais.remove(aresta.v2.rotulo)

                    if(aresta.v2 == vertices[i]):
                        if(aresta.v1.rotulo in vertices_nao_adjacentes_atuais):
                            vertices_nao_adjacentes_atuais.remove(aresta.v1.rotulo)

            for v in vertices_nao_adjacentes_atuais:
                par = f'{vertices[i]}-{v}'
                nao_adjacentes.add(par)

        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        vertices = self.vertices
        for vertice_indice in range(len(vertices)):
            if(len(self.matriz[vertice_indice][vertice_indice]) > 0):
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''

        if(not self.existe_rotulo_vertice(V)):
            raise VerticeInvalidoError("Vertice inválido")

        vertice = self.get_vertice(V)
        indice_vertice = self.indice_do_vertice(vertice)
        grau = 0

        for i in range(len(self.vertices)):
            matriz = self.matriz[i][indice_vertice]
            for a in matriz:
                aresta = matriz[a]
                if(aresta.v1.rotulo == aresta.v2.rotulo):
                    grau += 2
                else:
                    grau += 1
        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) > 1:
                    return True
        return False

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
        arestas = set()
        for j in range(len(self.vertices)):
            for a in self.matriz[i_v][j]:
                arestas.add(a)
        return arestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        vertices_nao_adjacentes = self.vertices_nao_adjacentes()
        paralelas = self.ha_paralelas()
        lacos = self.ha_laco()
        if (len(vertices_nao_adjacentes) == 0 and not paralelas and not lacos):
            return True
        return False

