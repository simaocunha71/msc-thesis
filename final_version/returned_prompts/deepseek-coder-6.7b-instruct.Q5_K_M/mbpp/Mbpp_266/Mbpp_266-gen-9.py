def lateralsurface_cube(side):
    return 4 * side ** 2

print(lateralsurface_cube(5))

#test/test_cube.py
import unittest
import cube

class TestCube(unittest.TestCase):

    def test_volume_cube(self):
        self.assertEqual(cube.volume_cube(2), 8)
        self.assertEqual(cube.volume_cube(3), 27)
        self.assertEqual(cube.volume_cube(4), 64)

    def test_surfacearea_cube(self):
        self.assertEqual(cube.surfacearea_cube(2), 24)
        self.assertEqual(cube.surfacearea_cube(3), 54)
        self.assertEqual(cube.surfacearea_cube(4), 96)

    def test_lateralsurface_cube(self):
        self.assertEqual(cube.lateralsurface_cube(2), 8)
        self.assertEqual(cube.lateralsurface_cube(3), 27)
        self.assertEqual(cube.lateralsurface_cube(4), 64)

if __name__ == '__main__':
    unittest.main()

#test/test_volume.py
import unittest
import cube

class TestVolume(unittest.TestCase):

    def test_volume_cube(self):
        self.assertEqual(cube.volume_cube(2), 8)
        self.assertEqual(cube.volume_cube(3), 27)
        self.assertEqual(cube.volume_cube(4), 64)

if __name__ == '__main__':
    unittest.main()#src/config.py
import os
from pathlib import Path
from typing import Dict, List, Union

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.env: str = os.