  Here is the Python solution for the given problem statement:

  Problem 1:

  ```python
  def hasCloseElements(numbers, threshold):
      for i in range(len(numbers)):
          for j in range(i+1, len(numbers)):
              if abs(numbers[i] - numbers[j]) < threshold:
                  return True
      return False
  ```

  Problem 2:

  ```python
  def separateParenGroups(paren_string):
      result = []
      current_string = []
      current_depth = 0

      for c in paren_string:
          if c == '(':
              current_depth += 1
              current_string.append(c)
          elif c == ')':
              current_depth -= 1
              current_string.append(c)
              if current_depth == 0:
                  result.append(''.join(current_string))
                  current_string = []
      return result
  ```

  Problem 3:

  ```python
  def truncateNumber(number):
      return number % 1
  ```

  Problem 4:

  ```python
  def fib4(n):
      if n < 2:
          return 0
      elif n == 2:
          return 2
      elif n == 3:
          return 0

      fib = [0, 0, 2, 0] + [0]*(n-3)
      for i in range(4, n+