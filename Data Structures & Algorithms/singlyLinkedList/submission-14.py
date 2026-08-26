class LinkedList:
    
    def __init__(self):
        self.llist = []
        self.head = 0
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        nodeRef = self.head
        nodeIndex = 0
        
        while nodeRef is not None:
            node = self.llist[nodeRef]
            if nodeIndex == index:
                return node[0]
            nodeRef = node[1]
            nodeIndex = nodeIndex + 1
        return -1

    def insertHead(self, val: int) -> None:
        listLen = len(self.llist)
        if self.size == 0:
            self.llist.append([val, None])
            self.head = len(self.llist) - 1
        else:
            self.llist.append([val, self.head])
            self.head = len(self.llist) - 1
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.size == 0:
            self.insertHead(val)
            return
        self.llist.append([val, None])
        new_idx = len(self.llist) - 1
        index = self.head
        lastIndex = self.head
        while index is not None:
            lastIndex = index
            index = self.llist[index][1]
        self.llist[lastIndex][1] = new_idx
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False

        if index == 0:
            self.head = self.llist[self.head][1]
            self.size -= 1
            return True

        nodeRef = self.head
        nodeIndex = 0
        prevIndex = -1
        while nodeRef is not None:
            if nodeIndex == index:
                self.llist[prevIndex][1] = self.llist[nodeRef][1]
                self.size -= 1
                return True
            prevIndex = nodeRef
            nodeRef = self.llist[nodeRef][1]
            nodeIndex += 1
        return False

    def getValues(self) -> List[int]:
        retList = []
        if self.size == 0:
            return retList
        index = self.head
        while index is not None:
            node = self.llist[index]
            retList.append(node[0])
            index = node[1]
        return retList