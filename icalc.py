import pegpy

peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value
parser = pegpy.generate(peg)

t = parser('1+2')
print(repr(t))

t = parser('1@2')
print(repr(t))


