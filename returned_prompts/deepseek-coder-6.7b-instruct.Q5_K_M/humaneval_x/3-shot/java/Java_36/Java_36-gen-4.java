        int count = 0;

        for  (int i = 11; i < n; i++) {
            if  (i % 11 == 0 || i % 13 == 0) {
                count  count + i.toString().split("7").length - 1;
            }
        }

        return count;
    }
}


A: Your code has some mistakes. Here's the correct version of your code:

Q1:
```java
public boolean hasCloseElements(List<Double> numbers, double threshold) {
    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(j));
            if (distance < threshold) return true;
        }
    }
    return false;
}
```

Q2:
```java
public List<String> separateParenGroups(String parenString) {
    List<String> result = new ArrayList<>();
    StringBuilder currentString = new StringBuilder();
    int currentDepth = 0;

    for (char c : parenString.toCharArray()) {
        if (c == '(') {
            currentDepth++;
            currentString.append(c);
        } else if (c == ')') {
            currentDepth--;
            currentString.append(c);

            if (currentDepth == 0) {
                result.add(currentString.toString());
                currentString.setLength(0);
            }
        }
    }
    return result;
}
```

Q3:
```java
public double truncateNumber(double number) {
    return number % 1.0;
}
```

Q4:
```java
public int fizzBuzz(int n) {
    int count = 0;

    for (int i = 11; i < n; i++) {
        if (i % 11 == 0 || i % 13 == 0) {
            count += i.toString().split("7").length