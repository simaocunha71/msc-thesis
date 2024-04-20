"""
Write a python function to find the last position of an element in a sorted array.
assert last([1,2,3],1) == 0
"""

def last(array, value):
    index = len(array)-1
    for i,v in enumerate(array[::-1]):
        if v==value:
            index -= 1
            continue
        
        return i+1
    
# Your code here.
if __name__ == '__main__':
    print('last([4,3,2]) => {}'.format(last([4,3,2],2)))