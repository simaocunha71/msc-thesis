You have the right idea, but it seems like the problem might be missing a bit of context. The code you posted is actually correct and will return the largest even number in the range [x, y]. However, the problem statement mentions "biggest even integer", which implies that the range should only include even numbers.

If you want to return the largest even number in the range [x, y], you should change the condition in your for loop to check if i is even:

```java
for(int i = x; i <= y; i++) {
    if(i > maxNum && i % 2 == 0) {
        maxNum = i;
    }
}
```

This will make sure that the largest number returned is always even. If there are no even numbers in the range, the function will return -1 as expected.

If you meant to check for the largest odd number, you should change the condition to check if i is odd:

```java
for(int i = x; i <= y; i++) {
    if(i > maxNum && i % 2 != 0) {
        maxNum = i;
    }
}
```

Please clarify the problem statement if this is not what you intended.


