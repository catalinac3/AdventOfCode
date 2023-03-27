from ..adventofcode.day3 import repeatedItem
from dataclasses import dataclass

def test_repeatedItem():

    @dataclass
    class TestCase:
        inputList: list
        expectedItem: str

    testCases = [TestCase(inputList=['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg'],
                          expectedItem="r"),
                 TestCase(inputList=['wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw'],
                          expectedItem='Z')]

    for test in testCases:
        assert repeatedItem(test.inputList) == test.expectedItem