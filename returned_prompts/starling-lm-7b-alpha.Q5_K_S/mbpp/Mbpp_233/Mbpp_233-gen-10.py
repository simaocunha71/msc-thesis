
import math
import unittest
def lateralsuface_cylinder(r: float, h: float) -> float:
    return 2 * math.pi * r * h

class TestLateralSurfaceArea(unittest.TestCase):
    def test_lateral_surface_area(self):
        self.assertAlmostEqual(lateralsuface_cylinder(10,5), 314.15000000000003, rel_tol=0.001)

if __name__ == '__main__':
    unittest.main()


