class IterClass:

    def __init__(self, value: int):
        self.value = value

    def __iter__(self):
        for i in range(self.value):
            yield f'value #{i+1}'

if __name__ == "__main__":

    c = IterClass(11) 
    for x in c:
        print(x)      