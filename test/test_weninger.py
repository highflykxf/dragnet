
import unittest
from dragnet import weninger

import numpy as np

class TestWeningerSxDx(unittest.TestCase):
    def test_weninger_sx_sdx(self):

        from dragnet import weninger
        import numpy as np
        from dragnet import weninger_OLD


        x = np.linspace(0, 10, 10)
        actual = weninger.weninger_sx_sdx(x)
        expected = np.array(
            [[ 0.47448994,  2.22222222],
            [ 1.18661763,  2.22222222],
            [ 2.22759261,  2.22222222],
            [ 3.33348203,  2.22214787],
            [ 4.44444444,  2.21961138],
            [ 5.55555556,  2.18707981],
            [ 6.66651797,  2.02019401],
            [ 7.77240739,  1.63420945],
            [ 8.81338237,  1.14625352],
            [ 9.52551006,  0.79272618]])
        self.assertTrue(np.allclose(actual, expected))


if __name__ == "__main__":
    unittest.main()


