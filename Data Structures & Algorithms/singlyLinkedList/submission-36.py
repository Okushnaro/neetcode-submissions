class LinkedList:
    
    def __init__(self):
        self.llist = []
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1 
        nodeRef = self.head
        nodeCount = 0
        while nodeRef is not None:
            if nodeCount == index:
                return self.llist[nodeRef][0]# value
            nodeRef = self.llist[nodeRef][1]
            nodeCount += 1
        return -1

        

    def insertHead(self, val: int) -> None:
        self.llist.append([val, self.head])
        self.size += 1
        listSz = len(self.llist)
        self.head = listSz -1
        # Inserting the very first node
        if self.size == 1:
            self.tail = self.head 


    def insertTail(self, val: int) -> None:
        self.llist.append([val, None])
        listSz = len(self.llist)
        newRef = listSz - 1
        # # Inserting the very first node
        if self.size == 0:
            self.tail = newRef
            self.head = self.tail
            self.size += 1
            return
            

        self.llist[self.tail][1] = newRef
        self.tail = newRef
        self.size += 1
        

    def remove(self, index: int) -> bool:
        if index >= self.size or index < 0:
            return False
        
        nodeRef = self.head
        nodeCount = 0
        prevRef = []
        while nodeRef is not None:
            prevRef.append(nodeRef)
            nextRef = self.llist[nodeRef][1]
            if nodeCount == index:

                if index == 0:
                    self.head = nextRef
                    if self.size == 1:
                        self.tail = None
                    self.size -= 1
                    return True

                self.llist[prevRef[nodeCount - 1]][1] = nextRef
                if index == self.size - 1:
                    self.tail = prevRef[nodeCount - 1]
                self.size -= 1
                return True
                

            nodeRef = nextRef
            nodeCount += 1
        return False
        

    def getValues(self) -> List[int]:
        retList = []
        nodeRef = self.head
        while nodeRef is not None:
            retList.append(self.llist[nodeRef][0])
            nodeRef = self.llist[nodeRef][1]
            
        return retList