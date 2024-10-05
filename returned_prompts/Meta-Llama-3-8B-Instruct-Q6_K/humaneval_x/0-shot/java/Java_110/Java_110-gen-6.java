```java
public String exchange(List<Integer> lst1, List<Integer> lst2) {
    int even = 0;
    for (int num : lst1) {
        if (num % 2 == 0) {
            even++;
        }
    }
    if (even == lst1.size()) {
        return "YES";
    }
    for (int num : lst2) {
        if (num % 2 != 0) {
            return "NO";
        }
    }
    return "YES";
}
```
This solution first checks if the number of even numbers in lst1 is equal to the size of lst1. If it is, then it is possible to make all elements of lst1 even by exchanging elements with lst2. If not, then it checks each number in lst2 to see if it is odd. If it finds an odd number, then it returns "NO" because it is impossible to make all elements of lst1 even by exchanging elements with lst2. If it doesn't find any odd numbers, then it returns "YES". 

The time complexity of this solution is O(n), where n is the size of lst1, because it iterates over lst1 once and lst2 once. The space complexity is O(1), because it uses a constant amount of space to store the variable even. 