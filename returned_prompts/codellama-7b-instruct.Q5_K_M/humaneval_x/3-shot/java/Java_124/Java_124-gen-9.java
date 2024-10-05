        if (date.isEmpty()) {
            return false;
        }

        String[] date_split = date.split("-");
        if (date_split.length != 3) {
            return false;
        }

        int month = Integer.parseInt(date_split[0]);
        int day = Integer.parseInt(date_split[1]);
        int year = Integer.parseInt(date_split[2]);

        if (month < 1 || month > 12) {
            return false;
        }

        if (day < 1 || day > 31) {
            return false;
        }

        if (month == 2 && day > 29) {
            return false;
        }

        if ((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && day > 31) {
            return false;
        }

        if ((month == 4 || month == 6 || month == 9 || month == 11) && day > 30) {
            return false;
        }

        return true;
    }
}

