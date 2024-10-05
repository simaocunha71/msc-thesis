        if (date.isEmpty()) return false;

        String[] date_parts = date.split("-");
        if (date_parts.length != 3) return false;

        int month = Integer.parseInt(date_parts[0]);
        int day = Integer.parseInt(date_parts[1]);
        int year = Integer.parseInt(date_parts[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (year < 0) return false;

        if (month == 2) {
            if (day < 1 || day > 29) return false;
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day < 1 || day > 30) return false;
        } else {
            if (day < 1 || day > 31) return false;
        }

        return true;
    }
}

