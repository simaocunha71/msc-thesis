        if (date.length() != 10) return false;
        if (date.charAt(2) != '-' || date.charAt(5) != '-') return false;
        int month = Integer.valueOf(date.substring(0, 2));
        int day = Integer.valueOf(date.substring(3, 5));
        int year = Integer.valueOf(date.substring(6, 10));
        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (year < 1000 || year > 9999) return false;
        if (month == 2) {
            if (day > 29) return false;
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) return false;
        }
        return true;
    }
}

