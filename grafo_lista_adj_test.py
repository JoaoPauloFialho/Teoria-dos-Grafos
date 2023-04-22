import unittest
from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo dijkstra
        self.g_dij = MeuGrafo()
        self.g_dij.adiciona_vertice("A")
        self.g_dij.adiciona_vertice("B")
        self.g_dij.adiciona_vertice("C")
        self.g_dij.adiciona_vertice("D")
        self.g_dij.adiciona_vertice("E")
        self.g_dij.adiciona_vertice("F")
        self.g_dij.adiciona_aresta('a1', 'A', 'B', 2)
        self.g_dij.adiciona_aresta('a2', 'A', 'D', 5)
        self.g_dij.adiciona_aresta('a3', 'B', 'D', 1)
        self.g_dij.adiciona_aresta('a4', 'B', 'C', 2)
        self.g_dij.adiciona_aresta('a5', 'B', 'E', 6)
        self.g_dij.adiciona_aresta('a6', 'B', 'F', 7)
        self.g_dij.adiciona_aresta('a7', 'C', 'E', 3)
        self.g_dij.adiciona_aresta('a8', 'D', 'F', 1)

        self.dijkstra5 = MeuGrafo()
        self.dijkstra5.adiciona_vertice("A")
        self.dijkstra5.adiciona_vertice("B")
        self.dijkstra5.adiciona_vertice("C")
        self.dijkstra5.adiciona_aresta('a1', 'A', 'B', 10)
        self.dijkstra5.adiciona_aresta('a2', 'A', 'C', 1)
        self.dijkstra5.adiciona_aresta('a3', 'C', 'B', 1)


        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba com peso
        self.g_p_com_peso = MeuGrafo()
        self.g_p_com_peso.adiciona_vertice("J")
        self.g_p_com_peso.adiciona_vertice("C")
        self.g_p_com_peso.adiciona_vertice("E")
        self.g_p_com_peso.adiciona_vertice("P")
        self.g_p_com_peso.adiciona_vertice("M")
        self.g_p_com_peso.adiciona_vertice("T")
        self.g_p_com_peso.adiciona_vertice("Z")
        self.g_p_com_peso.adiciona_aresta('a1', 'J', 'C', 1)
        self.g_p_com_peso.adiciona_aresta('a2', 'C', 'E', 1)
        self.g_p_com_peso.adiciona_aresta('a3', 'C', 'E', 1)
        self.g_p_com_peso.adiciona_aresta('a4', 'P', 'C', 1)
        self.g_p_com_peso.adiciona_aresta('a5', 'P', 'C', 1)
        self.g_p_com_peso.adiciona_aresta('a6', 'T', 'C', 1)
        self.g_p_com_peso.adiciona_aresta('a7', 'M', 'C', 1)
        self.g_p_com_peso.adiciona_aresta('a8', 'M', 'T', 1)
        self.g_p_com_peso.adiciona_aresta('a9', 'T', 'Z', 1)

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        #Grafo sem paralelas para testar a função DFS
        self.g_p_sem_paralelas_dfs = MeuGrafo()
        self.g_p_sem_paralelas_dfs.adiciona_vertice("J")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("C")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("E")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("P")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("T")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("M")
        self.g_p_sem_paralelas_dfs.adiciona_vertice("Z")
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a3', 'C', 'P')
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a4', 'C', 'T')
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a6', 'T', 'M')
        self.g_p_sem_paralelas_dfs.adiciona_aresta('a7', 'T', 'Z')

        #Grafo sem paralelas para testar a função DFS partindo do vértice T
        self.g_p_sem_paralelas_dfs_vertice_T = MeuGrafo()
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("T")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("C")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("J")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("E")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("P")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("M")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_vertice("Z")
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a1', 'C', 'J')
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a3', 'C', 'P')
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a5', 'C', 'M')
        self.g_p_sem_paralelas_dfs_vertice_T.adiciona_aresta('a7', 'T', 'Z')

        #Grafo sem paralelas para testar a função DFS partindo do vértice Z
        self.g_p_sem_paralelas_dfs_vertice_Z = MeuGrafo()
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("Z")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("T")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("C")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("J")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("E")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("P")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_vertice("M")
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a7', 'Z', 'T')
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a1', 'C', 'J')
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a3', 'C', 'P')
        self.g_p_sem_paralelas_dfs_vertice_Z.adiciona_aresta('a5', 'C', 'M')

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        #Grafo completo para analise da árvore dfs de g_c
        self.g_c_dfs = MeuGrafo()
        self.g_c_dfs.adiciona_vertice("J")
        self.g_c_dfs.adiciona_vertice("C")
        self.g_c_dfs.adiciona_vertice("E")
        self.g_c_dfs.adiciona_vertice("P")
        self.g_c_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs.adiciona_aresta('a4', 'C', 'E')
        self.g_c_dfs.adiciona_aresta('a6', 'E', 'P')

        #Grafo completo para analise da árvore dfs de g_c a partir da raiz E
        self.g_c_dfs_vertice_E = MeuGrafo()
        self.g_c_dfs_vertice_E.adiciona_vertice("E")
        self.g_c_dfs_vertice_E.adiciona_vertice("J")
        self.g_c_dfs_vertice_E.adiciona_vertice("C")
        self.g_c_dfs_vertice_E.adiciona_vertice("P")
        self.g_c_dfs_vertice_E.adiciona_aresta('a2', 'E', 'J')
        self.g_c_dfs_vertice_E.adiciona_aresta('a1', 'J', 'C')
        self.g_c_dfs_vertice_E.adiciona_aresta('a5', 'C', 'P')

        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def testBuscaProfundidade(self):
        self.assertEqual(self.g_p_sem_paralelas_dfs, self.g_p_sem_paralelas_dfs.dfs())
        self.assertEqual(self.g_p_sem_paralelas_dfs_vertice_T, self.g_p_sem_paralelas.dfs("T"))
        self.assertEqual(self.g_p_sem_paralelas_dfs_vertice_Z ,self.g_p_sem_paralelas.dfs("Z"))
        self.assertEqual(self.g_c_dfs ,self.g_c.dfs())
        self.assertEqual(self.g_c_dfs_vertice_E, self.g_c.dfs("E"))

    def testBuscaEmLargura(self):
        print(self.g_p.bfs())

    def testDijkstra(self):
        self.assertEqual(self.g_dij.dijkstra("A", "F"), ['A','B','D','F'])
        self.assertEqual(self.g_dij.dijkstra("B", "C"), ['B','C'])
        self.assertEqual(self.g_dij.dijkstra('A', 'E'), ['A','B','C','E'])
        self.assertEqual(self.g_dij.dijkstra('E', 'D'), ['E', 'C', 'B', 'D'])
        self.assertEqual(self.g_dij.dijkstra('E', 'F'), ['E', 'C', 'B', 'D', 'F'])
        self.assertEqual(self.dijkstra5.dijkstra("A", 'B'), ['A', 'C', 'B'])
        self.assertEqual(self.dijkstra5.dijkstra("B", 'A'), ['B', 'C', 'A'])
        self.assertEqual(self.dijkstra5.dijkstra("A", "C"), ["A", 'C'])
        self.assertEqual(self.dijkstra5.dijkstra('C', 'B'), ["C", 'B'])
        self.assertEqual(self.dijkstra5.dijkstra('B', 'C'), ["B", 'C'])
