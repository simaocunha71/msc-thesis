        if (date.isEmpty() || date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-')
            return false;

        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));
        int year = Integer.parseInt(date.substring(6));

        if (month < 1 || month > 12 || day < 1 || year < 1)
            return false;

        if (month == 4 || month == 6 || month == 9 || month == 11)
            return day <= 30;
        if (month == 2) {
            if (day > 29 || year % 4 != 0)
                return false;
            if (year % 100 == 0 && year % 400 != 0)
                return false;
            return true;
        }
        return day <= 31;
    }
}

