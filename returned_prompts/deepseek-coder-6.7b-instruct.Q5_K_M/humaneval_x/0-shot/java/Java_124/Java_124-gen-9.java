        if(date.isEmpty()) return false;
        if(date.length() != 10) return false;
        if(date.charAt(2) != '-' || date.charAt(5) != '-') return false;
        String month = date.substring(0, 2);
        String day = date.substring(3, 5);
        String year = date.substring(6);
        if(Integer.parseInt(month) < 1 || Integer.parseInt(month) > 12) return false;
        if(Integer.parseInt(day) < 1 || Integer.parseInt(day) > 31) return false;
        if(Integer.parseInt(year) < 1) return false;
        switch(Integer.parseInt(month)){
            case 4: case 6: case 9: case 11:
                if(Integer.parseInt(day) > 30) return false;
                break;
            case 2:
                if(Integer.parseInt(day) > 29) return false;
                break;
        }
        return true;
    }


}


This solution is based on the given problem, first the function will check if the date string is not empty and has the correct length and format. Then it will check if the month is between 1 and 12. It will also check if the day is between 1 and 31 for all months, except for April, June, September and November which have 30 days, and February which has 29 days.


Note: This solution does not check for leap years, it assumes all input dates are in the Gregorian calendar. If you want to check for leap years, the solution would need to be modified.


This solution will work for all dates in the valid range of the Gregorian calendar. For dates in the range of the Julian calendar, the solution would need to be modified.


The solution does not check if the date is a valid date in the Gregorian calendar, it only checks if the date is formatted correctly and if the numbers are within the valid range.


This solution assumes that the input date string is always in the format: mm-dd-yyyy. If the input date string