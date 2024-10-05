        if (date.isEmpty()) {
            return false;
        }

        String[] parts = date.split("-");
        if (parts.length != 3) {
            return false;
        }

        int month, day, year;

        try {
            month = Integer.parseInt(parts[0]);
            day = Integer.parseInt(parts[1]);
            year = Integer.parseInt(parts[2]);
        } catch (NumberFormatException e) {
            return false;
        }

        if (month < 1 || month > 12) {
            return false;
        }

        if (day < 1) {
            return false;
        }

        if (month == 2) {
            if (day > 29) {
                return false;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        } else {
            if (day > 31) {
                return false;
            }
        }

        return true;
    }
}

// You can test your code here
class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.validDate("03-11-2000")); // true
        System.out.println(solution.validDate("15-01-2012")); // false
        System.out.println(solution.validDate("04-0-2040")); // false
        System.out.println(solution.validDate("06-04-2020")); // true
        System.out.println(solution.validDate("06/04/2020")); // false
    }
}
```

This program first checks if the date is not empty and if it follows the correct format. Then it checks if the month and year are within the valid range and if the day is within the valid range for the specific month. If all checks pass, the function returns true, otherwise it returns false.

Here'