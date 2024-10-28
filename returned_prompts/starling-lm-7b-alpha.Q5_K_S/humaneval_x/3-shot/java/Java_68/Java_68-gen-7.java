        List<Integer> result = new ArrayList<>();
        if (arr.size() == 0) return result;

        int min_even = Integer.MAX_VALUE;
        int index = 0;
        for (int i = 0; i < arr.size(); i++) {
            int node = arr.get(i);
            if (node % 2 == 0 && node < min_even) {
                min_even = node;
                index = i;
            }
        }
        result.add(min_even);
        result.add(index);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.pluck(Arrays.asList(4, 2, 3))); // [2, 1]
        System.out.println(solution.pluck(Arrays.asList(1, 2, 3))); // [2, 1]
        System.out.println(solution.pluck(Arrays.asList())); // []
        System.out.println(solution.pluck(Arrays.asList(5, 0, 3, 0, 4, 2))); // [0, 1]
    }
}
```