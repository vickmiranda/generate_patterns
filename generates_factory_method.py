from string import Template
from datetime import date

CLASS_FACTORY_TEMPLATE = Template('''\
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
        print 'initializing $concrete_product1'

    def $method1(self):
        print 'running method for $concrete_product1'

    def $cleanup_method(self):
        print 'clean up method for $concrete_product1'


class $concrete_product2($class_interface):
    def $initialize_method(self):
        print 'initializing $concrete_product2'

    def $method1(self):
        print 'running method for $concrete_product2'

    def $cleanup_method(self):
        print 'clean up for $concrete_product2'


class $concrete_product3($class_interface):
    def $initialize_method(self):
        print 'initializing $concrete_product3'

    def $method1(self):
        print 'running method for $concrete_product3'

    def $cleanup_method(self):
        print 'clean up for $concrete_product3'


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

    def initialize_all(self):
        for i in self.instruments:
            i().$initialize_method()

    def run_all(self):
        for i in self.instruments:
            i().$method1()

    def cleanup_all(self):
        for i in self.instruments:
            i().$cleanup_method()


# Concrete creator 1
class $class_concrete_creator_one($class_creator):
    def create_layout(self):
        self.add_to_list($concrete_product1)
        self.add_to_list($concrete_product2)
        self.add_to_list($concrete_product3)


# Concrete creator 2
class $class_concrete_creator_two($class_creator):
    def create_layout(self):
        self.add_to_list($concrete_product1)
        self.add_to_list($concrete_product2)


# Usage
if __name__ == '__main__':
    print 'creating and using product 1'
    product1 = $class_concrete_creator_one()
    product1.initialize_all()
    product1.run_all()
    product1.cleanup_all()

''')

output = CLASS_FACTORY_TEMPLATE.substitute(class_interface='MyInterface',
                                             initialize_method='setup',
                                             method1='run',
                                             cleanup_method='cleanup',
                                             concrete_product1='DMM',
                                             concrete_product2='Scope',
                                             concrete_product3='PowerSupply',
                                             class_creator='Configure',
                                             attribute_list='instruments',
                                             attribute='instrument',
                                             class_concrete_creator_one='Station1',
                                             class_concrete_creator_two='Station2',
                                             date=date.today()
                                             )

with open('auto_factory_method.py', 'wb') as f:
    f.write(output)
