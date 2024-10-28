        if (date.equals("")) return false;

        String[] date_parts = date.split("-");
        int month = Integer.parseInt(date_parts[0]);
        int day = Integer.parseInt(date_parts[1]);
        int year = Integer.parseInt(date_parts[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (year < 1900 || year > 2020) return false;
        if (month == 2 && day > 29) return false;
        if (month == 4 || month == 6 || month == 9 || month == 11 && day > 30) return false;
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 && day > 31) return false;

        return true;
    }
}

