        String[] monthDays = {"31", "29", "31", "30", "31", "30", "31", "31", "30", "31", "30", "31"};
        String[] months = {"01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"};
        if (date == null || date.length() != 10 || !date.matches("\\d\\d-(0[1-9]|1[0-9]|[2-9])-(0[0-9]{2,4}):00")) {
            return false;
        }
        int monthIndex = Integer.parseInt(date.substring(0, 2)) - 1;
        int dayIndex = Integer.parseInt(date.substring(3, 5));
        int yearIndex = Integer.parseInt(date.substring(6, 10));

        if (monthIndex < 0 || monthIndex > 11 || dayIndex < 0 || dayIndex > 31 || yearIndex < 0 || yearIndex > 9999) {
            return false;
        }
        if (monthIndex == 1 && dayIndex > 29) {
            return false;
        }
        if (monthIndex == 2 && dayIndex > 28) {
            return false;
        }
        if (monthIndex == 3 && dayIndex > 31) {
            return false;
        }
        if (monthIndex == 4 && dayIndex > 30) {
            return false;
        }
        if (monthIndex == 5 && dayIndex > 31) {
            return false;
        }
        if (monthIndex == 6 && dayIndex > 30) {
            return false;
        }
        if (monthIndex == 7 && dayIndex > 31) {
            return false;
        }
        if (monthIndex == 8 && dayIndex > 31) {
            return false;
        }
        if (monthIndex