        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.toList());
    }
}


A: 
I'm trying to solve a problem from HackerRank in Java. I've done some other problems, but this one seems a bit more complex.

The problem is about filtering a list of integers to return only those which are positive. You are given a list of integers, your task is to write a function that will return a new list that contains only the positive integers from the original list.

Your function should use Java 8's Stream API to filter the list and return the result.

Here is an example of the problem statement:

You are given an array of integers. Your task is to write a function that returns an array that contains only the positive integers from the original array.

You should use Java 8's Stream API to solve this problem.

Here is an example of how the solution would work:

Example
List<Integer> l = Arrays.asList(-1, 2, -4, 5, 6);
getPositive(l);  // returns [2, 5, 6]

Example
List<Integer> l = Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10);
getPositive(l);  // returns [5, 3, 2, 3, 9, 123, 1]

In the example above, the function getPositive is filtering the list to only include positive integers.

I've tried to solve this problem, but I'm getting an error. I think the problem is with how I'm using the Stream API, but I'm not sure how to fix it.

Here is what I've tried so far:

```java
import java.util.*;
import java.lang.*;
import java.util.stream.Collectors;

class Solution  {
    public List<Integer> getPositive(List<Integer> l) {
        return l.stream()
                .filter(x -> x > 0)
                .collect(Collectors.to