

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
  # copy the other definitions
  # from the previous parts
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr = string
    pass

  @property
  def expression(self):
    return self.expr
    pass

  @expression.setter
  def expression(self, new_expr):
    if self._is_valid_string(new_expr):
      self.expr = new_expr
    else:
      self.expr = ""

    pass

  def _is_valid_string(self, input_string):
    if isinstance(input_string, str):
      for char in input_string:
        if char not in self.valid_char:
          return False
      return True
    pass
  def insert_space(self):
    new_expr = ""
    for char in self.expr:
      if char in "+-*/()":
        new_expr += " " + char + " "
      else:
        new_expr += char
    self.expr = new_expr
    return self.expression
    pass
  def process_operator(self, operand_stack, operator_stack):
    if operator_stack.is_empty:
      return
    else:
      operator = operator_stack.pop()
      if operator == "(":
        return
      else:
        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        result = self._eval(operand1, operator, operand2)
        operand_stack.push(int(result))
    pass

  def _eval(self, operand1, operator, operand2):
    if operator == "+":
      return operand1 + operand2
    elif operator == "-":
      return operand1 - operand2
    elif operator == "*":
      return operand1 * operand2
    elif operator == "/":
      return operand1 / operand2
    pass

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    self.insert_space()
    expr_list = self.expr.split()
    for token in expr_list:
      if token.isdigit():
        operand_stack.push(int(token))
      elif token in "+-":
        while not operator_stack.is_empty and operator_stack.peek() not in "()":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token in "*/":
        while not operator_stack.is_empty and operator_stack.peek() in "*/":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(token)
      elif token == "(":
        operator_stack.push(token)
      elif token == ")":
        while not operator_stack.is_empty and operator_stack.peek() != "(":
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()
    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.peek()
    pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





