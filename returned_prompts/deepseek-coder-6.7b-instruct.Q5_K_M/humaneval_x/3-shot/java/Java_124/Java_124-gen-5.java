        if (date == null || date.isEmpty() || date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-') {
            return false;
        }
        int month, day, year;
        try {
            month = Integer.parseInt(date.substring(0, 2));
            day = Integer.parseInt(date.substring(3, 5));
            year = Integer.parseInt(date.substring(6));
        } catch (NumberFormatException e) {
            return false;
        }
        if (month < 1 || month > 12 || day < 1 || year < 1) {
            return false;
        }
        if (month == 2) {
            if (day > 29 || day < 1) {
                return false;
            }
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30 || day < 1) {
                return false;
            }
        } else if (day > 31 || day < 1) {
            return false;
        }
        return true;
    }
}

