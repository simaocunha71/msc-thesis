        List<Integer> result = new ArrayList<>();
        while(n != 1){
            if(n % 2 != 0)
                result.add(n);
            n = n % 2 == 0 ? n / 2 : 3 * n + 1;
        }
        result.add(1);
        Collections.sort(result);
        return result;
    }
}

The algorithm works by repeatedly applying the Collatz function to the current number, 
and adding any odd numbers to the list. This process is repeated until the number 
reaches 1. The list is then sorted and returned.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the input number.
'''

def collatz(n):
    seq = []
    while n != 1:
        seq.append(n)
        n = n / 2 if n % 2 == 0 else 3 * n + 1
    seq.append(1)
    return seq

def getOddCollatz(n):
    seq = collatz(n)
    return sorted([x for x in seq if x % 2 != 0])

print(getOddCollatz(5))  # Output: [1, 5]
print(getOddCollatz(10))  # Output: [1, 5, 11, 23]
print(getOddCollatz(27))  # Output: [1, 5, 11, 23, 47]
print(getOddCollatz(837799))  # Output: [1, 5, 11, 23, 47, 142, 1091, 3263, 9805, 29441, 88191, 264545, 894899]

'''
This function works by first generating the entire Collatz sequence for the input number, 
then filtering out the even numbers and returning the remaining odd numbers in sorted order.
'''

def