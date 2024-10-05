        // Corner case handling
        if (number < 0) {
            number = -number;
        }

        // Convert the number to a string
        String str = String.valueOf(number);

        // Split the string into an array of strings
        String[] str_arr = str.split("\\.");

        // Check if the string contains a decimal point
        if (str_arr.length == 1) {
            return 0;
        }

        int decimal_part = Integer.parseInt(str_arr[1]);

        // Round the decimal part to the nearest tenth
        int rounded_decimal_part = Math.round(decimal_part * 10) % 10;

        return Double.parseDouble(str_arr[0] + "." + rounded_decimal_part);
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.truncateNumber(3.6));
        System.out.println(solution.truncateNumber(3.7));
        System.out.println(solution.truncateNumber(3.8));
        System.out.println(solution.truncateNumber(3.9));
        System.out.println(solution.truncateNumber(4.0));
        System.out.println(solution.truncateNumber(4.1));
        System.out.println(solution.truncateNumber(4.2));
        System.out.println(solution.truncateNumber(4.3));
        System.out.println(solution.truncateNumber(4.4));
        System.out.println(solution.truncateNumber(4.5));
        System.out.println(solution.truncateNumber(4.6));
        System.out.println(solution.truncateNumber(4.7));
        System.out.println(solution.truncateNumber(4.8));
        System.out.println(solution.trunc