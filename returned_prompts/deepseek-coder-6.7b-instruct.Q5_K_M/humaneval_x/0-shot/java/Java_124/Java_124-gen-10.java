        if (date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-')
            return false;

        String month = date.substring(0, 2);
        String day = date.substring(3, 5);
        String year = date.substring(6);

        if (Integer.parseInt(month) < 1 || Integer.parseInt(month) > 12)
            return false;

        if (Integer.parseInt(day) < 1)
            return false;

        if (Integer.parseInt(month) == 2) {
            if (Integer.parseInt(day) > 29)
                return false;
        }

        else if (Integer.parseInt(month) == 4 || Integer.parseInt(month) == 6 || Integer.parseInt(month) == 9 || Integer.parseInt(month) == 11) {
            if (Integer.parseInt(day) > 30)
                return false;
        }

        else {
            if (Integer.parseInt(day) > 31)
                return false;
        }

        return true;
    }
}

This program checks for the rules specified in the problem. It first checks if the length of the date string is 10 and if the correct format is used (mm-dd-yyyy). Then it separates the month, day and year from the date string. It checks if the month is between 1 and 12. It then checks if the day is between 1 and 31 for months 1,3,5,7,8,10,12 and between 1 and 30 for months 4,6,9,11. For month 2, it checks if the day is between 1 and 29. If all these conditions are satisfied, the method returns true, indicating a valid date. Otherwise, it returns false.































































