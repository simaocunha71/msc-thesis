        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < nums.size(); i++) {
            result.add(nums.get(i));
        }
        Collections.sort(result, (x, y) -> {
            int sum_x = sumOfDigits(x);
            int sum_y = sumOfDigits(y);
            if (sum_x == sum_y) return Integer.compare(x, y);
            return Integer.compare(sum_x, sum_y);
        });
        return result;
    }

    private int sumOfDigits(int number) {
        int result = 0;
        while (number != 0) {
            result += number % 10;
            number /= 10;
        }
        return result;
    }
}


public class Practice {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}

```