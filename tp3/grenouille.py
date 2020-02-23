from pyDatalog import pyDatalog

# pyDatalog.load('frogs(X) <= croakes(X) & eatFlies(X)')
# pyDatalog.load('canary(X) <= chirps(X) & sings(X)')
# pyDatalog.load('green(X) <= frogs(X)')
# pyDatalog.load('yellow(X) <= canary(X)')

# pyDatalog.assert_fact('croakes', 'fritz')
# pyDatalog.assert_fact('eatFlies', 'fritz')

# pyDatalog.assert_fact('frogs', 'a')
# pyDatalog.assert_fact('canary', 'b')

# print(pyDatalog.ask('green(X)'))
# print(pyDatalog.ask('yellow(X)'))

# print(pyDatalog.ask('green(a)'))
# print(pyDatalog.ask('green(b)'))

pyDatalog.clear()
pyDatalog.create_terms(
    'frogs, croakes, eatFlies, canary, chirps, sings, green, yellow, X,FROGS')

frogs(X) <= croakes(X) & eatFlies(X)
canary(X) <= chirps(X) & sings(X)
green(X) <= frogs(X)
yellow(X) <= canary(X)

# croakes[fritz]
# eatFlies[fritz]

# frogs[a]
# canary[b]
pyDatalog.assert_fact('croakes', 'fritz')
pyDatalog.assert_fact('eatFlies', 'fritz')

pyDatalog.assert_fact('frogs', 'a')

pyDatalog.assert_fact('chirps', 'b')
pyDatalog.assert_fact('sings', 'b')
pyDatalog.assert_fact('canary', 'c')

print(frogs(FROGS))

# print(pyDatalog.ask('green(X)'))


# print(eatFlies[b])
# print(len(globals()))
