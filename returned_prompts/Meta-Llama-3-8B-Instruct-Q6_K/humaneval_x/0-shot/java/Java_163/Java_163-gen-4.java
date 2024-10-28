        List<Integer> result = new ArrayList<Integer>();

        if(a > b) {
            int temp = a;
            a = b;
            b = temp;
        }

        for(int i = a; i <= b; i++) {
            String str = Integer.toString(i);
            for(int j = 0; j < str.length(); j++) {
                if(Integer.parseInt(str.substring(j, j+1)) % 2 == 0) {
                    result.add(i);
                    break;
                }
            }
        }

        return result;
    }

Solution:
The given problem requires to find even digits between two given integers. The problem statement is a bit unclear and it seems that it wants to find the even digits from the numbers between a and b, not the numbers themselves.

However, if we interpret the problem as finding the numbers themselves, then the solution is quite simple. We just need to iterate over the range from a to b and check if the number itself is even. If it is, then add it to the result list.

Here is the Java code for the solution:

```java
public List<Integer> generateIntegers(int a, int b) {
    List<Integer> result = new ArrayList<Integer>();

    if(a > b) {
        int temp = a;
        a = b;
        b = temp;
    }

    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            result.add(i);
        }
    }

    return result;
}
```

This code will return a list of even numbers between a and b. If a is greater than b, it will swap them to ensure that the loop iterates from a to b. Inside the loop, it checks if the current number is even by using the modulo operator. If the number is even, it adds it to the result list. Finally, it returns the result list.