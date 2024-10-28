        if(date == null || date.isEmpty()) {
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

        if (day < 1 || day > 31) {
            return false;
        }

        if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        } else if (month == 2) {
            if (day > 29) {
                return false;
            }
        }

        return true;
    }
}

In this code, we first check if the date is empty or null. If it is, we return false. Then we split the date into its components by "-". If the split does not yield exactly 3 parts, we return false as this is not a valid format.

We then try to parse the month, day, and year into integers. If this fails, we return false.

Next, we check if the month is within the valid range (1-12). If it is not, we return false.

We then check if the day is within the valid range (1-31). If it is not, we return false.

If the month is 4, 6, 9, or 11, we check if the day is less than or equal to 30. If it is not, we return false.

If the month is 2, we check if the day is less than or equal to 29. If it is not, we return false.

If all these checks pass, we return true, indicating that the date is valid.

This code assumes that all input dates are in the Gregorian calendar.


