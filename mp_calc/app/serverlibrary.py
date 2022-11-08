

def mergesort(array, byfunc=None):
    if byfunc is None:
        byfunc = lambda x: x
    mergesort_recursive(array, 0, len(array)-1, byfunc)

def mergesort_recursive(array, p, r, byfunc):
    if p < r:
        q = (p+r)//2
    
        
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        merge(array, p, q, r, byfunc)
    pass

def merge(array, p, q, r, byfunc):
    n1  = q-p+1
    n2 = r-q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    
    l = 0
    r = 0
    d = p         
    while (l<n1) and (r<n2):
        if byfunc(left_array[l]) <= byfunc(right_array[r]):
            array[d]=left_array[l]
            l += 1
        else:
            array[d]=right_array[r]
            r += 1
        d += 1
    
    while (l<n1):
        array[d]=left_array[l]
        l += 1
        d += 1
    
    while (r<n2):
        array[d]=right_array[r]
        r += 1
        d += 1
   
    pass


class Stack:
    def __init__(self):
        self.__items = []
        
    def push(self, item):
        self.__items.append(item)
        pass

    def pop(self):
        if self.size > 0:
          return self.__items.pop()
        pass

    def peek(self):
        
        n = len(self.__items)
        return self.__items[n-1]
 
        pass

    @property
    def is_empty(self):
        return len(self.__items) == 0
        pass

    @property
    def size(self):
        return len(self.__items)
        pass


class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





