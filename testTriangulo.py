import unittest
import triangulo

class TestTriangulo(unittest.TestCase):

    def test_IsocelesL1Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,2,2),"Invalido")
    def test_IsocelesL2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-2,2),"Invalido")
    def test_IsocelesL3Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(1,2,-2),"Invalido")
    def test_IsocelesTodoNegativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-2,-2),"Invalido")
    def test_IsocelesL1L2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-2,2),"Invalido")
    def test_IsocelesL2L3NegativasR(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-2,-2),"Invalido")
    def test_IsocelesL1L3NegativasE(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,2,-2),"Invalido")
    def test_EscalenoL1Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-3,2,4),"Invalido")
    def test_EscalenoL2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(3,-2,4),"Invalido")
    def test_EscalenoL3Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(3,2,-4),"Invalido")
    def test_EscalenoTodoNegativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-3,-2,-4),"Invalido")
    def test_EscalenoL1L2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-3,-2,4),"Invalido")
    def test_EscalenoL2L3NegativasR(self):
        self.assertEqual(triangulo.clasifTriangulo(2,-3,-4),"Invalido")
    def test_EscalenoL1L3NegativasE(self):
        self.assertEqual(triangulo.clasifTriangulo(-2,3,-4),"Invalido")
    def test_EquilateroL1Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,1,1),"Invalido")
    def test_EquilateroL2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-1,1),"Invalido")
    def test_EquilateroL3Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(1,1,-1),"Invalido")
    def test_EquilateroTodoNegativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-1,-1),"Invalido")
    def test_EquilateroL1L2Negativo(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-1,1),"Invalido")
    def test_EquilateroL2L3NegativasR(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-1,-1),"Invalido")
    def test_EquilateroL1L3NegativasE(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,1,-1),"Invalido")
    def test_NoCumpCond(self):
        self.assertEqual(triangulo.clasifTriangulo(1,2,3),"Invalido")
    def test_NoCumpCondL1Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,2,3),"Invalido")
    def test_NoCumpCondL2Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-2,3),"Invalido")
    def test_NoCumpCondL3Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(1,2,-3),"Invalido")
    def test_NoCumpCondL1L2Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-2,3),"Invalido")
    def test_NoCumpCondL2L3Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(1,-2,-3),"Invalido")
    def test_NoCumpCondL1L3Neg(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,2,-3),"Invalido")
    def test_NoCumpCondALLNeg(self):
        self.assertEqual(triangulo.clasifTriangulo(-1,-2,-3),"Invalido")
    def test_entradaString(self):
       self.assertEqual(triangulo.clasifTriangulo("Uno",2,1),"Invalido")
    def test_entradaChar(self):
        self.assertEqual(triangulo.clasifTriangulo('1',2,2),"Invalido")
    def test_entradaFloat(self):
        self.assertEqual(triangulo.clasifTriangulo(4.2,2.2,3.3),"Escaleno")
    def test_escaleno(self):
        self.assertEqual(triangulo.clasifTriangulo(4,2,3),"Escaleno")
    def test_equilatero(self):
        self.assertEqual(triangulo.clasifTriangulo(2,2,2),"Equilatero")
    def test_isocelesLLR(self):
        self.assertEqual(triangulo.clasifTriangulo(2,2,1),"Isoceles")
    def test_isocelesRLL(self):
        self.assertEqual(triangulo.clasifTriangulo(1,2,2),"Isoceles")
    def test_isocelesLLL(self):
        self.assertEqual(triangulo.clasifTriangulo(2,1,2),"Isoceles")

if __name__ == '__main__':
    unittest.main()


