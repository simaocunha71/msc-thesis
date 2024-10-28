        if (date.isEmpty())
            return false;
        if (date.length() != 10)
            return false;
        if (date.charAt(2) != '-' || date.charAt(5) != '-')
            return false;

        String month = date.substring(0, 2);
        String day = date.substring(3, 5);
        String year = date.substring(6);

        int m, d, y;
        try {
            m = Integer.parseInt(month);
            d = Integer.parseInt(day);
            y = Integer.parseInt(year);
        } catch (NumberFormatException e) {
            return false;
        }

        if (m < 1 || m > 12)
            return false;
        if (d < 1 || d > 31)
            return false;

        if (m == 2) {
            if (d > 29)
                return false;
        } else if (m == 4 || m == 6 || m == 9 || m == 11) {
            if (d > 30)
                return false;
        }

        return true;
    }
}
```

This code is a simple solution to the problem. It first checks if the date is empty or if it has the correct length and format. It then splits the date into its components (month, day, and year) and tries to parse them as integers. If any of these conversions fail, the function returns false. Finally, it checks if the month is within the valid range (1-12), if the day is within the valid range (1-31), and if the day is valid for the given month and year.

Please note that this code does not check for leap years, so it will incorrectly validate dates like February 29 in non-leap years. If you need to check for leap years, you will need to add an additional check for February 29.

Also, this code assumes that the day and month are always two digits. If this is not the case, you will need to add additional checks to handle single-digit days and months.

This code also does not validate the year. It assumes that the