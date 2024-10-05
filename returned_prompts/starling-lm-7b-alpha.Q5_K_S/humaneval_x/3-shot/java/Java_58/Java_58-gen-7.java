        List<Integer> result = new ArrayList<>();
        Set<Integer> result_set = new HashSet<>();

        for (int i = 0; i < l1.size(); i++) {
            if (l2.contains(l1.get(i))) {
                result_set.add(l1.get(i));
            }
        }
        result.addAll(result_set);
        Collections.sort(result);
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.common(Arrays.asList(1, 4, 3, 34, 653, 2, 5),
                                           Arrays.asList(5, 7, 1, 5, 9, 653, 121)));
        System.out.println(solution.common(Arrays.asList(5, 3, 2, 8),
                                           Arrays.asList(3, 2)));
    }
}
```