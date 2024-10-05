        String[] parts = date.split("-");
        if (parts.length != 3) return false;
        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        if (parts[0].length() != 2 || parts[1].length() != 2 || parts[2].length() != 4) return false;
        if (month < 1 || month > 12) return false;
        if (day < 1) return false;
        if (year < 0) return false;

        if (month == 2) {
            if (day > 29) return false;
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) return false;
        } else {
            if (day > 31) return false;
        }

        return true;
    }
}

