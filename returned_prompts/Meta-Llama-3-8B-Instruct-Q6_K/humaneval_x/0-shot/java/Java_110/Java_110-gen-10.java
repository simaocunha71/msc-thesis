Here is a simple solution in Java that uses two loops to iterate over the two lists and checks if it is possible to make all elements in lst1 even by exchanging elements with lst2:

```java
public String exchange(List<Integer> lst1, List<Integer> lst2) {
    for (int num : lst1) {
        if (num % 2 != 0) {
            boolean found = false;
            for (int other : lst2) {
                if (other % 2 != 0) {
                    if (!found) {
                        lst2.set(lst2.indexOf(other), num);
                        found = true;
                    } else {
                        return "NO";
                    }
                }
            }
            if (!found) {
                return "NO";
            }
        }
    }
    return "YES";
}
```

This solution iterates over lst1 and for each number that is not even, it tries to find an even number in lst2 to replace it with. If it finds one, it replaces it and continues with the next number. If it cannot find an even number to replace the current number, it returns "NO". If it can make all numbers in lst1 even, it returns "YES". 

This solution assumes that the input lists will be non-empty and will not modify the original lists. It also assumes that there are no duplicate numbers in the lists. 

If you need to handle duplicate numbers or modify the original lists, you will need to modify this solution accordingly. 

This solution has a time complexity of O(n^2), where n is the size of the lists, because it uses two nested loops to iterate over the lists. If the lists are very large, this could be slow. In that case, you might need to use a more efficient algorithm. 

Also, this solution does not check if the lists contain duplicate numbers. If the lists can contain duplicate numbers and you want to handle them correctly, you will need to modify this solution accordingly. 

Finally, this solution assumes that the input lists are not null. If the input lists can be null and you want to handle them correctly, you will need to modify this solution accordingly. 

Here is a version of the solution that checks for null lists and duplicate numbers:

```java
public String exchange(List<Integer> lst1, List<Integer> lst2) {
    if (lst1 == null || lst2 == null) {
        return "NO";
    }
    Set<Integer> set1 = new HashSet<>();
    for (