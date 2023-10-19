import unittest

from sort import Dinosaurs



class TestDinosaurs(unittest.TestCase):
    def test_herbyShouldComeBack(self):
        unit = Dinosaurs(["raptor", "t-rex"])
        results = unit.sort(["triceratops","raptor", "t-rex","brachiosaurus", "lemons", "stegosaurus", "allosaurus"])
        self.assertEquals(results,["triceratops", "brachiosaurus", "lemons", "stegosaurus", "allosaurus"])
        
if __name__=='__main__':
    unittest.main()