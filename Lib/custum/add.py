import numpy

class add:
    __x = None
    __y = None
    __sum = None

    NUM_IN = 2
    NUM_PAR = 0
    NUM_OUT = 1

    IN_LABEL = ["x","y"]
    OUT_LABEL = ["Sum"]
    
    def set_input(self,data):
        self.__x = data[0]
        self.__y = data[1]
    
    def get_output(self):
        return self.__sum
    
    def take_sum(self):
        self.__sum = self.__x + self.__y

    def process(self):
        self.take_sum()

# test script
# a = add()
# a.set_input([1,2])
# a.process()
# a.NUM_IN = 10
# r = a.get_output()
# print(r)
# print(a.IN_LABEL[0])