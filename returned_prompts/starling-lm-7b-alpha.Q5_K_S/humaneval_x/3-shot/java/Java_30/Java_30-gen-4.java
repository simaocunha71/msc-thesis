        return l.stream().filter(i -> i > 0).collect(Collectors.toList());
    }
}



public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Integer> l = Arrays.asList(5, 3, -5, 2, -3, 3, 9, 0, 123, 1);
        System.out.println(solution.getPositive(l));
    }
}
```