__author__ = 'Marcin'

from exceptions import *


class SymbolTypes:
    Terminal, NonTerminal, Epsilon = range(3)


#################################################


class Symbol(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type


#################################################


class Production(object):

    def __init__(self, left_side):
        self.left_side = left_side
        self.right_side = []

    def get_left_side(self):
        return self.left_side

    def get_right_side(self):
        return self.right_side


#################################################


class Grammar(object):

    def __init__(self):
        self.productions = []

    def parse_from_text(self, text):
        for line in text.splitlines():
            try:
                left, right = line.split("->")
            except ValueError as e:
                raise GrammarException("Invalid production format")

            if not (left.isupper() and len(left) == 1):
                raise GrammarException("Left side of the production must be a single non-terminal symbol")
            left_symbol = Symbol(left, SymbolTypes.NonTerminal)

            if "|" in right:
                right_sides = right.split('|')
            else:
                right_sides = [right]

            for right in right_sides:
                p = Production(left_symbol)
                for symbol in right:
                    if symbol == '$':
                        right_symbol = Symbol(symbol, SymbolTypes.Epsilon)
                    elif symbol.isupper():
                        right_symbol = Symbol(symbol, SymbolTypes.NonTerminal)
                    elif symbol not in ' ':
                        right_symbol = Symbol(symbol, SymbolTypes.Terminal)
                    else:
                        raise GrammarException("Invalid symbol")
                    p.get_right_side().append(right_symbol)
                if len(p.get_right_side()) == 0:
                    raise GrammarException("Production cannot be empty")
                self.productions.append(p)

    def to_plain_text(self):
        return '\n'.join([prod.get_left_side().get_name()+'->'+''.join([p.get_name() for p in prod.get_right_side()]) \
                          for prod in self.productions])




