from string import Template

CLASS_SINGLETON_TEMPLATE = Template('''\
from abc import ABCMeta, abstractmethod


class $class_interface(object):
    __metadata__ = ABCMeta
    @abstractmethod
    def $initialize_method(self):
        pass

    @abstractmethod
    def $method1(self):
        pass

    @abstractmethod
    def $cleanup_method(self):
        pass


class $concrete_product1($class_interface):
    def $initialize_method(self):
        print 'initializing\\n'

    def $method1(self):
        print 'running method 1\\n'

    def $cleanup_method(self):
        print 'clean up method 1\\n'


class $concrete_product2($class_interface):
    def $initialize_method(self):
        print 'initializing\\n'

    def $method1(self):
        print 'running method 2\\n'

    def $cleanup_method(self):
        print 'clean up method 2\\n'


# creator goes here
class $class_creator(object):
    __metaclass = ABCMeta

    def __init__(self):
        self.$attribute_list = []
        self.create_layout()

    @abstractmethod
    def create_layout(self):
        pass

    def add_to_list(self, $attribute):
        self.$attribute_list.append($attribute)

    def get_items_list(self):
        return self.$attribute_list


# Concrete creator 1
class $class_concrete_creator_one($class_creator):
    def create_layout(self):
        self.add_to_list($concrete_product1)
        self.add_to_list($concrete_product2)


# Concrete creator 2
class $class_concrete_creator_two($class_creator):
    def create_layout(self):
        self.add_to_list($concrete_product1)
        self.add_to_list($concrete_product2)


# Usage
if __name__ == '__main__':
    print 'creating and using product 1 \\n'
    product1 = $class_concrete_creator_one()

    print 'creating and using product 2 \\n'
    product2 = $class_concrete_creator_two()


\
''')

output = CLASS_SINGLETON_TEMPLATE.substitute(class_interface='MyInterface',
                                             initialize_method='initialize',
                                             method1='run_method',
                                             cleanup_method='cleanup',
                                             concrete_product1='Product1',
                                             concrete_product2='Product2',
                                             class_creator='Configure',
                                             attribute_list='products',
                                             attribute='product',
                                             class_concrete_creator_one='ConfigurationOne',
                                             class_concrete_creator_two='ConfigurationTwo'
                                             )

with open('auto_factory_method.py', 'wb') as f:
    f.write(output)