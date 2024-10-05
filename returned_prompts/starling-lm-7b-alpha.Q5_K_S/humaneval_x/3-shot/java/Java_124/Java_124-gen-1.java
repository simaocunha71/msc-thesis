        if (date.length() != 10) return false;
        if (!date.matches("[0-1]{1}[0-9]{1}-[0-3]{1}[0-9]{1}-[0-9]{4}")) return false;
        String[] tokens = date.split("-");
        int month = Integer.parseInt(tokens[0]);
        int day = Integer.parseInt(tokens[1]);
        int year = Integer.parseInt(tokens[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1) return false;
        if (month == 2 && day > 29) return false;
        if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) return false;
        } else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if (day > 31) return false;
        }
        return true;
    }
}

