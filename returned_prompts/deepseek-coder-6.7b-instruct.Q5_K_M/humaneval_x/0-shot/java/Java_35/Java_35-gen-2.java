        int max = l.get(0);
        for (int i = 1; i < l.size(); i++) {
            if (l.get(i) > max) {
                max = l.get(i);
            }
        }
        return max;
    }
}

This solution works by setting the first element of the list as the maximum initially. It then iterates through the rest of the list, comparing each element with the current maximum. If a larger element is found, it replaces the maximum. When the loop finishes, the maximum value has been found and is returned.

It's worth mentioning that if the list is empty, the method will crash because it will try to get the first element of an empty list. You may want to add a check at the start of the method to see if the list is empty and return a suitable value in this case.

The time complexity of this solution is O(n), where n is the size of the list. This is because it iterates through the list once. The space complexity is O(1), because it only uses a single integer to store the maximum value.

This solution assumes that the list contains at least one element.
*/

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.maxElement(Arrays.asList(1, 2, 3))); // 3
        System.out.println(solution.maxElement(Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10))); // 123
    }
}
```

### 2.3. 二叉树的层序遍历

```java
