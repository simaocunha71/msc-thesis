```java
public List<String> byLength(List<Integer> arr) {
    List<String> result = new ArrayList<>();
    List<Integer> sortedArr = new ArrayList<>();

    // filter out integers that are not between 1 and 9 inclusive
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            sortedArr.add(num);
        }
    }

    // sort the filtered array
    sortedArr.sort((a, b) -> a - b);

    // reverse the sorted array
    Collections.reverse(sortedArr);

    // replace each digit by its corresponding name
    for (int num : sortedArr) {
        result.add(getName(num));
    }

    return result;
}

// helper method to get the name of a digit
private String getName(int num) {
    switch (num) {
        case 1: return "One";
        case 2: return "Two";
        case 3: return "Three";
        case 4: return "Four";
        case 5: return "Five";
        case 6: return "Six";
        case 7: return "Seven";
        case 8: return "Eight";
        case 9: return "Nine";
        default: return "";
    }
}
```