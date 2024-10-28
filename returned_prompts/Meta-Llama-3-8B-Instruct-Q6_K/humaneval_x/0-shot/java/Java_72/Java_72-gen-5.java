Here is a Java function that implements the described behavior:

```java
public boolean willItFly(List<Integer> q, int w) {
    List<Integer> qList = new ArrayList<Integer>(q); // convert to list
    Collections.reverse(qList); // reverse the list
    if (!q.equals(new ArrayList<Integer>(qList))) { // check if the list is palindromic
        return false;
    }
    int sum = 0;
    for (int i : q) {
        sum += i;
    }
    return sum <= w;
}
```

This function first converts the input list to a list, reverses it, and checks if the original list is equal to the reversed list. If they are not equal, it means the list is not palindromic, so the function returns false.

Then, it calculates the sum of the elements in the list and checks if it is less than or equal to the maximum possible weight w. If it is, the function returns true; otherwise, it returns false. 

Note that this function assumes that the input list does not contain null elements. If the list can contain null elements, the function should be modified to handle this case. 