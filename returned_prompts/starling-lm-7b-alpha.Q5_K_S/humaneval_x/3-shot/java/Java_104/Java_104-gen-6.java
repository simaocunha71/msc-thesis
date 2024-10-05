        List<Integer> result = new ArrayList<>();

        for (int num : x) {
            int n = num;
            boolean has_even_digit = false;
            while (n > 0) {
                if (n % 10 % 2 == 0) {
                    has_even_digit = true;
                    break;
                }
                n /= 10;
            }
            if (!has_even_digit) result.add(num);
        }
        Collections.sort(result);
        return result;
    }
}



public class A {
    public static void main(String[] args) {
        Solution solution = new Solution();

        List<Integer> x = Arrays.asList(15, 33, 1422, 1);
        System.out.println(solution.uniqueDigits(x));

        List<Integer> x1 = Arrays.asList(152, 323, 1422, 10);
        System.out.println(solution.uniqueDigits(x1));

        List<Double> numbers = Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0);
        System.out.println(solution.hasCloseElements(numbers, 0.3));

        String paren_string = "( ) (( )) (( )( ))";
        System.out.println(solution.separateParenGroups(paren_string));

        double number = 3.5;
        System.out.println(solution.truncateNumber(number));

    }
}
```