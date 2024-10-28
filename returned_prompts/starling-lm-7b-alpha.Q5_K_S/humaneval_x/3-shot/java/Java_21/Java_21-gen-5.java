        double min = Collections.min(numbers);
        double max = Collections.max(numbers);

        List<Double> result = new ArrayList<>();
        for (double number : numbers) {
            result.add((number - min) / (max - min));
        }
        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.rescaleToUnit(Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0)));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
    }
}
```