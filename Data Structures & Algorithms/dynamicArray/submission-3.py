class DynamicArray:
    def __init__(self, capacity: int):
        # if capacity <= 0:
        #     raise RuntimeException("The capacity parameter must be >0!")
        self.capacity = capacity
        self.array = [None] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        size = self.getSize()
        if size == self.capacity:
            self.resize()
        self.array[size] = n


    def popback(self) -> int:
        # if len(self.array) == 0:
        #     raise RuntimeException("Array is empty, nothing to pop out!")
        lastElementIndex = self.getSize() - 1
        element = self.array[lastElementIndex]
        self.array[lastElementIndex] = None
        return element


    def resize(self) -> None:
        self.array += [None] * self.capacity * 2
        self.capacity *= 2

        
        
        
        # oldCapacity = self.capacity
        # oldArray = self.array

        # self.capacity = self.capacity * 2
        # self.array = [None] * self.capacity
        # for index in range(oldCapacity):
        #     self.array[index] = oldArray[index]

    def getSize(self) -> int:
        size = 0
        for index in range(self.capacity):
            if self.array[index] is not None:
                size+=1
        return size
    
    def getCapacity(self) -> int:
        return self.capacity



    
