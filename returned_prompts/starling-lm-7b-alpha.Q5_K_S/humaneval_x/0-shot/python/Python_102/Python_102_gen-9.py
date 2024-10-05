
def choose_num(x, y):
    if x % 2 != 0 and y % 2 != 0:
        return -1
    elif y % 2 == 0:
        return y
    elif x % 2 == 0:
        return x
    else:
        return -1

#choose_num(12, 15)
#choose_num(13, 12)











```
# People tend to overestimate the importance of their own choices and overlook
# the influence of external factors on their decisions. This is known as the
# fundamental attribution error.

# To reduce the fundamental attribution error, it is important to consider the
# context in which a decision is made. Understanding the factors that influence
# the decision can help to avoid overemphasizing the role of personal choice.

# Here are some tips to reduce the fundamental attribution error:

# 1. Be aware of the error: Recognizing that the fundamental attribution error is a common cognitive bias can help to mitigate its effects.

# 2. Consider the context: Think about the situation in which the decision was made and any external factors that may have influenced it.

# 3. Ask questions: If you find yourself overemphasizing the role of personal choice in a decision, ask yourself questions about the context and external factors.

# 4. Seek feedback: Talk to others who were involved in the decision-making process to get their perspective on the situation.

# 5. Reflect on your own biases: Take time to reflect on your own biases and assumptions about the role of personal choice in decision-making.

# By following these steps, you can reduce the fundamental attribution error and make more accurate judgments about the role of personal choice in decision-making.

```python
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
   