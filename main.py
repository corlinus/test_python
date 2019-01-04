#!env python3

from smth import Smth
from another import Another
import sys

def main():
    print(sys.path)
    smth = Smth()
    another = Another()
    another.method()
    print(smth.value)

main()
