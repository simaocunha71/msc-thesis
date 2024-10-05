        StringBuilder sb = new StringBuilder();

        for (int i = 0; i <= n; i++) {
            sb.append(i);
            if (i < n) {
                sb.append(" ");
            }
        }

        return sb.toString();
    }
}

The solution above is a simple implementation of a for loop that iterates from 0 to n inclusive, appending each number to a StringBuilder object along with a space if the number is not the last one. The final output of the StringBuilder object is then returned as a string.
This solution has a time complexity of O(n), where n is the input number.


'''

def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    "0"
    >>> string_sequence(5)
    "0 1 2 3 4 5"
    """
    return ' '.join(str(i) for i in range(n+1))

'''
This Python solution uses a generator expression to create a string that is joined by spaces from numbers from 0 to n inclusive. This solution also has a time complexity of O(n).
'''


def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    "0"
    >>> string_sequence(5)
    "0 1 2 3 4 5"
    """
    return ' '.join(str(i) for i in range(n+1))

'''
This Python solution uses a generator expression to create a string that is joined by spaces from numbers from 0 to n inclusive. This solution also has a time complexity of O(n).
'''


def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    "0"
    >>> string_sequence(5)
    "0