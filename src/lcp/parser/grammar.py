__author__ = 'Marcin'

from exceptions import *
import re


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

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return other.get_name() == self.get_name() and other.get_type() == self.get_type()
        raise NotImplemented()


#################################################


class Production(object):

    def __init__(self, left_side):
        self.left_side = left_side
        self.right_side = []

    def get_left_side(self):
        return self.left_side

    def get_right_side(self):
        return self.right_side

    def __eq__(self, other):
        if isinstance(other, Production):
            return self.left_side == other.get_left_side() and self.right_side == other.get_right_side()
        raise NotImplemented()


#################################################


class Grammar(object):

    def __init__(self):
        self.productions = []
        self.non_terminals = []

    #######################################################

    def parse_from_text(self, text):
        self.productions = []
        self.non_terminals = []

        line_no = 0
        nonterm_pattern = re.compile("^\[[A-Z][^ ]\]$|^[A-Z]$")
        symbol_pattern  = re.compile("\[[A-Z][^ ]\]|[A-Z]|[^ ]")
        for line in text.splitlines():
            line_no += 1
            try:
                left, right = line.split("->")
            except ValueError as e:
                raise GrammarException(line_no, "Invalid production format")

            if not nonterm_pattern.match(left):
                raise GrammarException(line_no, "Left side of the production must be a single non-terminal symbol")
            left_symbol = Symbol(left, SymbolTypes.NonTerminal)
            self.non_terminals.append(left_symbol)

            if "|" in right:
                right_sides = right.split('|')
            else:
                right_sides = [right]

            for right in right_sides:
                p = Production(left_symbol)
                res = symbol_pattern.findall(right)
                if right == '':
                    raise GrammarException(line_no, "Production cannot be empty")
                elif reduce(lambda x, y: x+y, res) != right:
                    raise GrammarException(line_no, "Invalid symbol")
                for symbol in res:
                    if symbol == '$':
                        right_symbol = Symbol(symbol, SymbolTypes.Epsilon)
                    elif nonterm_pattern.match(symbol):
                        right_symbol = Symbol(symbol, SymbolTypes.NonTerminal)
                    elif symbol not in ' ':
                        right_symbol = Symbol(symbol, SymbolTypes.Terminal)
                    p.get_right_side().append(right_symbol)
                self.productions.append(p)

        if len(self.productions) == 0:
            raise GrammarException(0, "Grammar cannot be empty")

        self.check_correctness()

    def check_correctness(self):
        for prod in self.productions:
            for sym in prod.get_right_side():
                if sym.get_type() == SymbolTypes.NonTerminal and sym not in self.non_terminals:
                    raise GrammarException(sym.get_name(), "Undefined non-terminal")

    #######################################################

    def transform_grammar(self):
        self.remove_unnecessary_productions()

    def find_used_nonterminals(self, nonterm, used):
        for symbol in reduce(lambda x, y: x+y, [prod.get_right_side() for prod in self.productions
                                            if prod.get_left_side() == nonterm]):

            if symbol.get_type() == SymbolTypes.NonTerminal and symbol not in used:
                used.add(symbol)
                used.update(self.find_used_nonterminals(symbol, used))
        return used

    def remove_unnecessary_productions(self):
        used_nontermials = self.find_used_nonterminals(self.productions[0].get_left_side(),
                                                       {self.productions[0].get_left_side()})
        used_nontermials_names = [u.get_name() for u in used_nontermials]
        self.productions = filter(lambda p: p.get_left_side().get_name() in used_nontermials_names, self.productions)

    def to_plain_text(self):
        return '\n'.join([prod.get_left_side().get_name()+'->'+''.join([p.get_name() for p in prod.get_right_side()])
                          for prod in self.productions])




