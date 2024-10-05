        if (date.isEmpty()) return false;
        String[] split_date = date.split("-");
        if (split_date.length != 3) return false;
        int month = Integer.parseInt(split_date[0]);
        int day = Integer.parseInt(split_date[1]);
        int year = Integer.parseInt(split_date[2]);
        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (year < 0 || year > 9999) return false;
        if (day > 30 && (month == 4 || month == 6 || month == 9 || month == 11)) return false;
        if (day > 29 && month == 2) return false;
        return true;
    }
}

