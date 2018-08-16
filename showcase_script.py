from showcase.module_a import A
from showcase.module_b import B

b = B(1, 2)
a = A(b, 3, c=4, d=5)

print(b.to_config())
print(a.to_config())
print(a.method1())
print(a.method2())
