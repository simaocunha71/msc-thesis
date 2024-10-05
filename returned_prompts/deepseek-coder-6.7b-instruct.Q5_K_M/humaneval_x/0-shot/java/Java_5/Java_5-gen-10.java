        List<Integer> newList = new ArrayList<Integer>();
        if(numbers.size() == 0){
            return newList;
        }
        newList.add(numbers.get(0));
        for(int i = 1; i < numbers.size(); i++){
            newList.add(delimiter);
            newList.add(numbers.get(i));
        }
        return newList;
    }
}

This solution works by creating a new list and adding the first element of the original list to the new list. Then, it adds the delimiter and the next number from the original list to the new list in a loop, continuing until all numbers from the original list have been added. Finally, it returns the new list.

If the original list is empty, the function just returns an empty list.

The time complexity of this solution is O(n), where n is the size of the original list, because it needs to traverse the list once to add each element to the new list. The space complexity is also O(n), because in the worst case (when the delimiter is inserted between every two consecutive elements), the new list will have a size that is three times the size of the original list.

Note: The method Arrays.asList is used here to create the list, but it's not a good practice to use it if you want to add or remove elements from the list. It's better to use a new ArrayList and add elements to it.

The function can be used like this:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<Integer> numbers = new ArrayList<Integer>(Arrays.asList(1, 2, 3));
    int delimiter = 4;
    System.out.println(solution.intersperse(numbers, delimiter));
}
```

This will output:
```
[1, 4, 2, 4, 3]
```

Just replace the numbers and delimiter with your own values to test the function with different inputs.
   */
}

//src/test/java/SolutionTest.java
import org.junit.jupiter.api.