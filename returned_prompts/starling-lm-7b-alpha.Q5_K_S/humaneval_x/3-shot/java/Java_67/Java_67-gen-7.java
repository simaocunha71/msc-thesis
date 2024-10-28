        String[] parts = s.split(" ");
        return n - Integer.parseInt(parts[0].replace("apples", "")) - Integer.parseInt(parts[1].replace("oranges", ""));
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.fruitDistribution("5 apples and 6 oranges", 19));
        System.out.println(solution.fruitDistribution("0 apples and 1 oranges",3));
        System.out.println(solution.fruitDistribution("2 apples and 3 oranges", 100));
        System.out.println(solution.fruitDistribution("100 apples and 1 oranges",120));
    }
}
```