The problem is that you are trying to solve this problem by using brute force. The better solution would be to use the mathematical property of cube roots. A number is a cube if and only if the number is equal to the cube of some integer number.

So you can just check if the cube of the cube root of the number is equal to the number. You can use Math.cbrt() function to get the cube root of the number. 

Here is the optimized code:

```java
public boolean iscube(int a) {
    int root = (int) Math.round(Math.cbrt(a));
    return a == root * root * root;
}
```

This code first calculates the cube root of the number and rounds it to the nearest integer. It then checks if the cube of this root equals the original number. If it does, it means the number is a cube and the function returns true. Otherwise, it returns false. This solution is much more efficient than the original one.

Also, this solution works for both positive and negative numbers.

This solution has a time complexity of O(1) which is the best possible time complexity for this problem.
*/

