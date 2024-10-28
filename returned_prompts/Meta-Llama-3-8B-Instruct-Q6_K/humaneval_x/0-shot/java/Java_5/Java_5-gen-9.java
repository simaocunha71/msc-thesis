Explanation:
The problem is asking to insert a number 'delimeter' between every two consecutive elements of input list `numbers`. 

The solution uses a for loop to iterate over the input list `numbers`. For each element, it adds the element to the result list `result`. If it's not the last element in the list, it also adds the delimiter to the result list. This way, the delimiter is inserted between every two consecutive elements.

Here is an example of how to use this method:
```
List<Integer> numbers = Arrays.asList(1, 2, 3);
int delimiter = 4;
List<Integer> result = new Solution().intersperse(numbers, delimiter);
System.out.println(result); // Output: [1, 4, 2, 4, 3]
```
In this example, the input list `numbers` is `[1, 2, 3]` and the delimiter is `4`. The output list `result` is `[1, 4, 2, 4, 3]`, which is the input list with the delimiter inserted between every two consecutive elements.