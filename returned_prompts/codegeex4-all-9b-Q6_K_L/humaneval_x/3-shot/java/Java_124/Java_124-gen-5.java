        String[] dateParts = date.split("-");
        int month = Integer.parseInt(dateParts[0]);
        int day = Integer.parseInt(dateParts[1]);
        int year = Integer.parseInt(dateParts[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (month == 2) {
            if (day > 29) return false;
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) return false;
        }

        return true;

    }
}

