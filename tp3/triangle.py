from pyDatalog import pyDatalog
# pyDatalog.load('triangle(X) <= cotes(X) == F')
# pyDatalog.load('equilateral(X) <= triangle(X) & cotes_egaux(X) == F')
# pyDatalog.load('isocele(X) <= triangle(X) & cotes_egaux(X) == D')
# pyDatalog.load('rectangle(X) <= triangle(X) & angle_droit(X)')
# pyDatalog.load('quelconque(X) <= triangle(X)')


# pyDatalog.assert_fact('cotes(3)', 'a')
pyDatalog.clear()
pyDatalog.create_terms(
    'triangle, quelconque, rectangle, isocele, rectangle, angle_droit, equilateral, cotes, cotes_egaux, X,Y')

triangle(X) <= cotes(X, Y) & (Y == 3)
equilateral(X) <= (triangle(X) & cotes_egaux(X, Y) & (Y == 3))
isocele(X) <= (triangle(X) & cotes_egaux(X, Y) & (Y == 2))
rectangle(X) <= (triangle(X) & angle_droit(X))
quelconque(X) <= triangle(X)

+cotes('triangle_Rectangle', 3)
+triangle('triangle_Rectangle')
+angle_droit('triangle_Rectangle')


+triangle('triangle_isocele')
+cotes_egaux('triangle_isocele', 2)

+triangle('triangle_equilaterale')
+cotes_egaux('triangle_equilaterale', 3)


print('Triangle {}'.format(pyDatalog.ask('triangle(X)')))
print('Triangle quelconque {}'.format(pyDatalog.ask('quelconque(X)')))
print('Triangle rectangle{}'.format(pyDatalog.ask('rectangle(X)')))
print('Triangle isocele{}'.format(pyDatalog.ask('isocele(X)')))
print('Triangle equilateral{}'.format(pyDatalog.ask('equilateral(X)')))

# print(pyDatalog.ask('triangle(triangle_Rectangle)'))
# print(pyDatalog.ask('quelconque(triangle_Rectangle)'))
# print(pyDatalog.ask('rectangle("triangle_Rectangle")'))
# print(pyDatalog.ask('isocele("triangle_Rectangle")'))
# print(pyDatalog.ask('equilateral("triangle_Rectangle")'))
