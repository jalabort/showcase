from hudl_terrarium import create_factory
from showcase.module_a import A
from showcase.module_b import B


create_a = create_factory([A], A)
create_b = create_factory([B], B)
