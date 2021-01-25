#written by MIDN Sean Moriarty

class MyClass:
    
    def __init__(self, listofnums):
        self.listofnums = listofnums

    def odds(self):
        i = 0
        oddnums = []
        for num in self.listofnums:
            if i % 2 != 0:
                oddnums.append(num)
            i += 1
        return oddnums

    def oddsPlusC(self, c):
        i = 0
        oddnums = []
        for num in self.listofnums:
            if i % 2 != 0:
                oddnums.append(num+c)
            i += 1
        return oddnums
