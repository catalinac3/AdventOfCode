from ..adventofcode.day3 import getRepeatedElements 

datatest = ['vJrwpWtwJgWrhcsFMMfFFhFp',
'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
'PmmdzqPrVvPwwTWBwg',
'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
'ttgJtRGJQctTZtZT',
'CrZsJsPPZsGzwwsLwLmpwMDw']
def day3_test():
    repeated = getRepeatedElements(datatest)
    assert repeated == {'p', 'L', 'P', 'v', 't', 's'}
