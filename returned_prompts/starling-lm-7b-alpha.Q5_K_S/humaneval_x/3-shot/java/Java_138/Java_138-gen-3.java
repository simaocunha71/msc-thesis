        if (n % 2 == 1) return false;
        for (int i = 2; i < n; i += 2) {
            if (n - i == i && n - i >= 0) {
                return true;
            }
        }
        return false;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        List<Double> numbers = Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0, 2.0);
        System.out.println(solution.hasCloseElements(numbers, 0.3));
    }
}

```