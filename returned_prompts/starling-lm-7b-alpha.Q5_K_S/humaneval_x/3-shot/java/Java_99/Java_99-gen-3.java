        int integer_part = Integer.parseInt(value.substring(0, value.length() - 1));
        int decimal_part = Integer.parseInt(value.substring(value.length() - 1));
        if (decimal_part == 0) {
            return integer_part;
        } else if (decimal_part < 0) {
            return integer_part - 1;
        } else {
            return integer_part + 1;
        }
    }
}






public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        // solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5);
        // solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3);
        // solution.separateParenGroups("( ) (( )) (( )( ))");
        // solution.truncateNumber(3.5);
        // solution.countUpper("10");
        // solution.countUpper("15.3");
        // solution.countUpper("14.5");
        // solution.countUpper("-14.5");
    }
}
```