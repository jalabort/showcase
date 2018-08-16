class A:
    r"""
    A docstrings
    """
    def __init__(self, a, b, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def method1(self):
        return 1

    def method2(self):
        return self.a.to_config()
