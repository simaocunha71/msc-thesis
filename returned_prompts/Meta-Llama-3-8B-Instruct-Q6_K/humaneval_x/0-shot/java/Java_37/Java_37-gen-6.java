```java
public List<Integer> sortEven(List<Integer> l) {
    List<Integer> result = new ArrayList<Integer>(l);
    Collections.sort(result.subList(1, result.size()));
    return result;
}
```
Explanation:
The problem asks to create a new list that is identical to the input list at odd indices, while the even indices have the same values as the even indices of the input list, but sorted. 

The solution uses the `subList` method of the `ArrayList` class, which returns a new list that contains the elements between the specified start and end indices. The `sort` method of the `Collections` class is used to sort the even indices of the list.

Note that the `subList` method takes the start and end indices as parameters, where the start index is inclusive and the end index is exclusive. In this case, we want to sort the even indices, so we start from the second element (index 1) and go up to the last element of the list. The `Collections.sort` method sorts the entire sublist in ascending order. 

Finally, the `result` list is returned, which contains the original elements at odd indices and the sorted elements at even indices. 