#!/usr/bin/env python3

import unittest


class Animal:
    def __init__(self, name, species, weight):
        self.name = name
        self.species = species
        self.weight = weight


class TestAnimal(unittest.TestCase):
    def example(self):
        return Animal("Oscar", "Dog", 10)

    def test_name(self):
        oscar = self.example()
        oscar.name = "Oscar"
        self.assertEqual(oscar.name, "Oscar")

    def test_species(self):
        oscar = self.example()
        oscar.species = "doggy"
        self.assertEqual(oscar.species, "doggy")

    def test_weight(self):
        oscar = self.example()
        oscar.weight = 10
        self.assertEqual(oscar.weight, 10)


if __name__ == "__main__":
    unittest.main()
