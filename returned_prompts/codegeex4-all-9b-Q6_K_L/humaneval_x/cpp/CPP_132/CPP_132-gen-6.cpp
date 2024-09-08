def is_nested(str):
    cnt=0
    for i in str:
        if i=='[':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            return True
    return False

C:
def is_nested(s):
    c = 0
    for i in s:
        if i == '[':
            c += 1
        elif i == ']':
            c -= 1
        if c == 0:
            return True
    return False

D:
def is_nested(s):
    stack = []
    for i in range(len(s)):
        if s[i]=='[':
            stack.append(i)
        elif stack and s[i]==']':
            stack.pop()
            if len(stack)>0:
                return True
    return False

E:
def is_nested(s):
    stack = []
    for i in s:
        if i == '[':
            stack.append(i)
        elif stack and i == ']':
            stack.pop()
            if len(stack) > 0:
                return True
    return False

F:
def is_nested(s):
    stack = []
    for i in range(len(s)):
        if s[i]=='[':
            stack.append(i)
        elif stack and s[i]==']':
            stack.pop()
            if len(stack)>0:
                return True
    return False

G:
def is_nested(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(i)
        elif stack and s[i] == ']':
            stack.pop()
            if len(stack) > 0:
                return True
    return False

H:
def is_nested(s):
    stack = []
    for i in s:
        if i == '[':
            stack.append(i)
        elif stack and i == ']':
            stack.pop()
            if len(stack) > 0:
                return True
    return False

I:
def is_nested(s):
    stack = []
    for i in range(len(s)):
        if s[i]=='[':
            stack.append(i)
        elif stack and s[i]==']':
            stack.pop()
            if len(stack)>0:
                return True
    return False

J:
def is_nested(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '[':
            stack.append(i)
        elif stack and s[i] == ']':
            stack.pop()
            if len(stack)