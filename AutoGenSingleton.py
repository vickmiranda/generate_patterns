from string import Template

CLASS_SINGLETON_TEMPLATE = Template('''\
class $class_name(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not $class_name._instance:
            $class_name._instance = super(
                $class_name, cls).__new__(cls, *args, **kwargs)
        return $class_name._instance

    def __init__(self):
        self.$attributes = []

\
''')

output = CLASS_SINGLETON_TEMPLATE.substitute(class_name='MySingleton',
                                             attributes='my_list',
                                             properties=None)
with open('auto_singleton.py', 'wb') as f:
    f.write(output)
