from showcase.module_a import A
from showcase.module_b import B

b = B(1, 2)
a = A(b, 3, c=4, d=5)

print(f'`b` config is: {b.to_config()}')
print(f'`a` config is: {a.to_config()}')

print(f'`a` method1 result is: {a.method1()}')
print(f'`a` method2 result is: {a.method2()}')

print(f'`A` bases are : {A.__bases__}')
print(f'`A` mro is : {A.__mro__}')

print(f'`B` bases are : {B.__bases__}')
print(f'`B` mro is : {B.__mro__}')
