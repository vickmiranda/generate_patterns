from string import Template
from datetime import date

CLASS_SINGLETON_TEMPLATE = Template('''\
from abc import ABCMeta, abstractmethod
\'''
This script was auto-generated on $date

Few things to adapt and is ready for you to use
\'''

class $class_facade(object):
    def __init__(self):
        sub_one = $class_system_one()
        sub_one.method_one()

    def run(self):
        sub_two = $class_system_two()
        sub_two.method_one()
        sub_two.method_two()

    def cleanup(self):
        sub_three = $class_system_three()
        sub_three.method_one()


# Sub-system1
class $class_system_one(object):
    def __init__(self):
        print 'sub-system one initialization\\n'

    def method_one(self):
        print 'method one sub_system one\\n'


# Sub-system2
class $class_system_two(object):
    def __init__(self):
        print 'sub-system two initialization\\n'

    def method_one(self):
        print 'method one sub_system two\\n'

    def method_two(self):
        print 'method two sub_system two\\n'


# Sub-system3
class $class_system_three(object):
    def __init__(self):
        print 'sub-system three initialization\\n'

    def method_one(self):
        print 'method one sub_system three\\n'


# Usage
if __name__ == '__main__':
    system = $class_facade()
    system.run()
    system.cleanup()

\
''')

output = CLASS_SINGLETON_TEMPLATE.substitute(class_facade='MyFacade',
                                             class_system_one='SubSystemOne',
                                             class_system_two='SubSystemTwo',
                                             class_system_three='SubSystemThree',
                                             date=date.today()
                                             )
with open('auto_facade.py', 'wb') as f:
    f.write(output)