        List<Integer> sortedArray = new ArrayList<>(array);
        Collections.sort(sortedArray);

        int sum = sortedArray.get(0) + sortedArray.get(sortedArray.size()-1);

        if(sum % 2 == 0){
            Collections.reverse(sortedArray);
        }

        return sortedArray;
    }
}


A: You can do it in one line by using Java 8's Streams API to calculate the sum and sort the array. Here is the code:
public List<Integer> sortArray(List<Integer> array) {
    boolean isReverse = array.stream().mapToInt(i -> i).sum() % 2 == 0;
    return array.stream().sorted().collect(isReverse ? Collectors.toList() : Collectors.toList());
}

In this code, the stream() method is used to convert the List to a Stream. mapToInt(i -> i) method is used to convert each element of the stream to an integer. The sum() method is then used to calculate the sum of all elements in the stream. The result of the sum is used to determine whether the array should be sorted in ascending or descending order. The sorted() method is used to sort the elements in the stream. Finally, the collect() method is used to convert the sorted stream back to a List. The isReverse variable is used to determine whether the collect() method should reverse the order of the elements in the List.

A: Here is a Python solution:

```python
def sort_array(array):
    if not array:
        return []
    else:
        array.sort()
        if sum(array[0:1]+array[-1:]) % 2 == 0:
            array.reverse()
        return array
```

This solution works by first checking if the array is empty and returning an empty array if it is. If the array is not empty, it sorts the array in ascending order. Then it checks if the sum of the first and last elements in the array is even. If it is, it reverses the array. Finally, it returns the sorted array.

It's important to note that Python's sort()