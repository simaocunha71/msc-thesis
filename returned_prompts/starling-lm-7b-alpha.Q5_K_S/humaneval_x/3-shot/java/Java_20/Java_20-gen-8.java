        Collections.sort(numbers);
        double min_distance = Double.MAX_VALUE;
        int closest_index = 0;
        int closest_second_index = 0;
        for (int i = 0; i < numbers.size(); i++) {
            double distance = Math.abs(numbers.get(i) - numbers.get(i + 1));
            if (distance < min_distance) {
                min_distance = distance;
                closest_index = i;
                closest_second_index = i + 1;
            }
        }
        return Arrays.asList(numbers.get(closest_index), numbers.get(closest_second_index));
    }
}

public class TestSolutions {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}
```