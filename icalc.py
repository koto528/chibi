import pegpy

peg = pegpy.grammar('''
Expression = Product (^{ '+' Product #Add })*
Product = Value (^{ '*' Product #Add })*
Value = { [0-9]+ #Int}
''')
parser = pegpy.generate(peg)

t = parser('1+2')
print(repr(t))

t = parser('1@2')
print(repr(t))


