        if (date.length() == 0) return false;
        if (date.matches("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")) {
            int month = Integer.parseInt(date.substring(0, 2));
            int day = Integer.parseInt(date.substring(3, 5));
            int year = Integer.parseInt(date.substring(6, 10));
            if (month == 2 && day > 28) return false;
            if (month == 4 || month == 6 || month == 9 || month == 11 && day > 30) return false;
            if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12 && day > 31) return false;
            if (day < 1 || day > 31) return false;
            if (year < 1900 || year > 2020) return false;
            return true;
        }
        return false;
    }
}

