        String[] parts = s.split(" ");
        int apples = Integer.parseInt(parts[2]);
        int oranges = Integer.parseInt(parts[6]);
        return n - apples - oranges;
    }
}

public class Main {
    public static void main(main) {
        Solution sol = new Solution();
        System.out.println(sol.fruitDistribution("5 apples and 6 oranges", 19)); // 8
        System.out.println(sol.fruitDistribution("0 apples and 1 oranges",3)); // 2
        System.out.println(sol.fruitDistribution("2 apples and 3 oranges", 100)); // 95
        System.out.println(sol.fruitDistribution("100 apples and 1 oranges",120)); // 19
    }
}

I'm getting a syntax error on the import statements. The code above was taken from a solution to a problem on HackerRank and it says to remove the main method and replace it with the following code:

```java
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.fruitDistribution("5 apples and 6 oranges", 19)); // 8
        System.out.println(sol.fruitDistribution("0 apples and 1 oranges",3)); // 2
        System.out.println(sol.fruitDistribution("2 apples and 3 oranges", 100)); // 95
        System.out.println(sol.fruitDistribution("100 apples and 1 oranges",120)); // 19
    }
}
```

This is the corrected code. The main method is now receiving a String[] as its parameter, which is the standard for a main method in Java.

I'm getting a syntax error on the import statements. The code above was taken from a solution to a problem on HackerRank and it says to remove the main method and replace it with the following code:

```java
public class Main {
    public static void main(String[] args