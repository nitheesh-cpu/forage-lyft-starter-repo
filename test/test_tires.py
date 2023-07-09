from tire.carrigan_tires import CarriganTires
from tire.octoprime_tires import OctoprimeTires

import unittest


class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.9, 0.8, 0.7]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_true2(self):
        tire_wear = [0.8, 0.94, 0.8, 0.7]
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.6, 0.8, 0.7]
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.6, 0.6, 0.6, 0.6]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())
