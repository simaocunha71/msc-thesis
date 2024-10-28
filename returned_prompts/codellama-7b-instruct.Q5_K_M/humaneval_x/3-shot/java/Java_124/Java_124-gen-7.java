        if (date.isEmpty() || date.length() != 10) return false;
        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));
        int year = Integer.parseInt(date.substring(6, 10));
        if (month < 1 || month > 12) return false;
        if (day < 1) return false;
        if (month == 2) {
            if (day > 29) return false;
        } else if (month % 2 != 0) {
            if (day > 30) return false;
        } else if (day > 31) return false;
        return true;
    }
}

