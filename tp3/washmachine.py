from pyDatalog import pyDatalog


pyDatalog.clear()
pyDatalog.create_terms(
    'dirt, type_dirt, wash_time, high, medium, low, X, Y, Z')

frogs(X) <= croakes(X) & eatFlies(X
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
