        if(date.isEmpty()) return false;
        String[] splitDate = date.split("-");
        if(splitDate.length != 3) return false;
        int month, day, year;
        try{
            month = Integer.parseInt(splitDate[0]);
            day = Integer.parseInt(splitDate[1]);
            year = Integer.parseInt(splitDate[2]);
        }
        catch(NumberFormatException e){
            return false;
        }
        if(month < 1 || month > 12) return false;
        if(day < 1 || day > 31) return false;
        if(month == 4 || month == 6 || month == 9 || month == 11) {
            if(day > 30) return false;
        }
        else if(month == 2) {
            if(day > 29) return false;
        }
        return true;
    }
}

