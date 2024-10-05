        if (date.length() != 10) {
            return false;
        }
        if (date.charAt(2) != '-' || date.charAt(5) != '-') {
            return false;
        }
        String month = date.substring(0, 2);
        String day = date.substring(3, 5);
        String year = date.substring(6);
        if (!month.matches("[0-9]{2}") || !day.matches("[0-9]{2}") || !year.matches("[0-9]{4}")) {
            return false;
        }
        int m = Integer.parseInt(month);
        int d = Integer.parseInt(day);
        int y = Integer.parseInt(year);
        if (m < 1 || m > 12) {
            return false;
        }
        if (d < 1 || d > 31) {
            return false;
        }
        if (m == 2) {
            if (y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)) {
                if (d > 29) {
                    return false;
                }
            } else {
                if (d > 28) {
                    return false;
                }
            }
        } else if (m == 4 || m == 6 || m == 9 || m == 11) {
            if (d > 30) {
                return false;
            }
        }
        return true;
    }
}

