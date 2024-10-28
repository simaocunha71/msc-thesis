        if(date == null || date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-'){
            return false;
        }

        String month = date.substring(0, 2);
        String day = date.substring(3, 5);
        String year = date.substring(6);

        if (Integer.parseInt(month) < 1 || Integer.parseInt(month) > 12 || Integer.parseInt(day) < 1 || Integer.parseInt(year) < 1){
            return false;
        }

        if(Integer.parseInt(month) == 2){
            if (Integer.parseInt(day) > 29){
                return false;
            }
        } else if((Integer.parseInt(month) == 4 || Integer.parseInt(month) == 6 || Integer.parseInt(month) == 9 || Integer.parseInt(month) == 11) && Integer.parseInt(day) > 30){
            return false;
        } else if(Integer.parseInt(day) > 31){
            return false;
        }

        return true;
    }
}

This Java function validates a date string based on the provided rules. The function first checks if the date is not empty and has the correct format (mm-dd-yyyy). Then, it checks if the month and year are within the valid range (1-12 for month, 1-∞ for year). After that, it checks if the day is within the valid range for the specific month. If all checks pass, the function returns true, indicating a valid date.

This function doesn't account for leap years, so it assumes all months have 31 days except for February, which has 29 days in a leap year.

You may need to adjust the conditions for February to account for leap years if you need to validate real dates.

Also, note that this function does not handle dates like "02-30-2020" or "02-31-2020" because it assumes that the date string will be in the correct format. If you need to handle these cases, you would need to add additional