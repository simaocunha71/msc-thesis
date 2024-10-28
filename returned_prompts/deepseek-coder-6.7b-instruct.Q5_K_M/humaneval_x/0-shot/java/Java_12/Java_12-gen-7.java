        if (strings.isEmpty()){
            return Optional.empty();
        }

        String longest = strings.get(0);
        for (String str : strings){
            if (str.length() > longest.length()){
                longest = str;
            }
        }
        return Optional.of(longest);
    }
}

I was able to solve the problem by using Java's `Optional` class which is used to handle the scenario where the list may be empty. Also, I used enhanced for loop to iterate over the list of strings.

This solution has a time complexity of O(n), where n is the number of elements in the list.

It's worth mentioning that the original problem description is a bit ambiguous, as it mentions "return the first one in case of multiple strings of the same length". If it means to return the longest string, then the solution is already correct. If it means to return the first string of the same length as the longest, then the solution needs to be modified.

Also, the method name `longest` is a bit misleading as it doesn't return the longest string, but rather the string with the most characters.

If you want to return the first string of the same length as the longest, you can modify the solution like this:

```java
public Optional<String> longest(List<String> strings) {
    if (strings.isEmpty()){
        return Optional.empty();
    }

    String longest = "";
    for (String str : strings){
        if (str.length() > longest.length()){
            longest = str;
        }
    }

    for (String str : strings){
        if (str.length() == longest.length()){
            return Optional.of(str);
        }
    }

    return Optional.of(longest);
}
```
This solution has the same time complexity O(n).
The first loop finds the longest string. The second loop checks the first string with the same length as the longest. If it exists, it is returned. Otherwise, the longest string is returned.

Please adjust the solution according to your needs.


I hope this helps, happy coding!!













