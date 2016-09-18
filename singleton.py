class MySingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not MySingleton._instance:
            MySingleton._instance = super(
                MySingleton, cls).__new__(cls, *args, **kwargs)
        return MySingleton._instance

    def __init__(self):
        self.my_list = []



