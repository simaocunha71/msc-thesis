        List<Integer> result = new ArrayList<Integer>();
        for(int i = 0; i < numbers.size(); i++){
            result.add(numbers.get(i));
            if(i < numbers.size()-1){
                result.add(delimiter);
            }
        }
        return result;
    }
}

*/

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.intersperse(Arrays.asList(1, 2, 3), 4));  //[1, 4, 2, 4, 3]
        System.out.println(solution.intersperse(Collections.emptyList(), 4)); //[]
    }
}

The solution first creates an empty list to store the result. Then it iterates through the input list, adding each number to the result list and the delimiter to the result list if it is not the last number in the list. Finally, it returns the result list.

Time complexity is O(n) as we iterate through the list once. Space complexity is also O(n) as we create a new list to store the result.

In the main method, we create an instance of the Solution class and call the intersperse method with a list of numbers and a delimiter. The result is printed to the console.

It's also important to note that the intersperse method doesn't modify the original list. It creates a new list to store the result.

The intersperse method works with any list of integers and any delimiter integer.

Also, the method will return an empty list if the input list is empty.

This solution is written in Java.

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```
