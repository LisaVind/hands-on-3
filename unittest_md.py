import sys, unittest
from md import calcenergy
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT

class MdTests(unittest.TestCase):

    def test_calcenergy(self):

        atoms = FaceCenteredCubic(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                                  symbol="Cu",
                                  size=(3, 3, 3),
                                  pbc=True)
        atoms.calc = EMT()

        ekin, epot = calcenergy(atoms)


        if ekin is not None and epot is not None:
            self.assertTrue(True)
        else:
            self.assertTrue(False)


if __name__ == '__main__':
    tests = [unittest.TestLoader().loadTestsFromTestCase(MdTests)]
    testsuite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner(verbosity=0).run(testsuite)
    sys.exit(not result.wasSuccessful())
