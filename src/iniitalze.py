import random

def generate(n):
    return [[random.random() for _ in range(32)] for __ in range(n)]
