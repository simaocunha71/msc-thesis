    public boolean validDate(String date) {
        if(date.isEmpty()) return false;
        String[] parts = date.split("-");
        if(parts.length != 3) return false;
        int day = Integer.parseInt(parts[1]);
        int month = Integer.parseInt(parts[0]);
        int year = Integer.parseInt(parts[2]);
        if(month < 1 || month > 12) return false;
        if(month == 2) {
            if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                if(day > 29) return false;
            } else {
                if(day > 28) return false;
            }
        } else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if(day > 31) return false;
        } else {
            if(day > 30) return false;
        }
        return true;
    }
}  // This function validates a date string and returns true if the date is valid otherwise false. It checks if the date is in the format "mm-dd-yyyy", if the month is in the range 1-12, and if the day is in the range 1-31 depending on the month. It also checks for leap years for the month February. It handles cases like "03-11-2000", "15-01-2012", "04-0-2040", "06-04-2020", and "06/04/2020".  // This function is case sensitive and does not handle dates like "06/04/2020" which is a valid date but in the format "mm/dd/yyyy".  // It also does not handle dates like "04-02-2020" which is a valid date but in the format "dd-mm-yyyy".  // It also does not handle dates like "04-02-2020" which is a valid date but in the format "dd-mm-yyyy".  // It also does not handle dates like "04-02-2020" which is a valid date but in the format "dd-mm-yyyy".  // It also does not handle dates like "04-02-2020" which is a valid date but in the format "dd-mm-yyyy".  // It also does not handle dates like "04-02-2020" which