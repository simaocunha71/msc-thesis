        if (date.isEmpty() || date.split("-").length != 3) {
            return false;
        }

        int month = Integer.parseInt(date.split("-")[0]);
        int day = Integer.parseInt(date.split("-")[1]);
        int year = Integer.parseInt(date.split("-")[2]);

        if (month < 1 || month > 12) {
            return false;
        }

        if (day < 1 || day > 31) {
            return false;
        }

        if (month == 2) {
            if (day > 28) {
                return false;
            }
        }

        if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) {
                return false;
            }
        }

        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if (day > 31) {
                return false;
            }
        }

        if (year < 0) {
            return false;
        }

        return true;
    }
}

