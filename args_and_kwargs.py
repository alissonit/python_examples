
class UseArgs:

    def __init__(self, myname, *args):
        self.myname = myname
        self.args = args
    
    @property
    def my_cars(self):
        print(f'Myname: {self.myname}')
        for i in self.args:
            print(f'Car: {i}')

class UseKwargs:

    def __init__(self, myname, **kwargs):
        self.myname = myname
        self.kwargs = kwargs
    
    @property
    def mycars(self):
        print(f'Myname: {self.myname}')
        for i in self.kwargs:
            print(f'Car k: {self.kwargs[i]}')

if __name__ == "__main__":
    
    us = UseArgs('Alisson', 'Gol', 'FordKa', 'FIT', 'March')
    us.my_cars

    kus = UseKwargs('Alisson', carro1='Gol', carro2='FordKa', carro3='FIT', carro4='March') 
    kus.mycars
