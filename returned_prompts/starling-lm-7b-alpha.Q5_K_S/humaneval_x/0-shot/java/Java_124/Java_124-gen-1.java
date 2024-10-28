        if(date.length() == 0) {
            return false;
        }

        String[] dateparts = date.split("-");
        if(dateparts.length != 3) {
            return false;
        }

        int month = Integer.parseInt(dateparts[0]);
        int day = Integer.parseInt(dateparts[1]);
        int year = Integer.parseInt(dateparts[2]);

        if(month == 0 || month == 13) {
            return false;
        }
        if(day == 0 || day > 31) {
            return false;
        }
        if(month == 2 && day > 29) {
            return false;
        }
        if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if(day < 1 || day > 31) {
                return false;
            }
        }
        if(month == 4 || month == 6 || month == 9 || month == 11) {
            if(day < 1 || day > 30) {
                return false;
            }
        }
        if(year < 0) {
            return false;
        }
        if(month < 0 || month > 12) {
            return false;
        }
        return true;
    }
}





































































































































































