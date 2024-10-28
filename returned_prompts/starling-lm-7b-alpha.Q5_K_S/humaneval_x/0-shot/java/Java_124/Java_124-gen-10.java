        if(date.isEmpty()){
            return false;
        }
        String[] dateArr = date.split("-");
        if(dateArr.length != 3){
            return false;
        }
        int month = Integer.parseInt(dateArr[0]);
        int day = Integer.parseInt(dateArr[1]);
        int year = Integer.parseInt(dateArr[2]);
        if(month < 1 || month > 12){
            return false;
        }
        if(day < 1 || day > 31 && month != 2 && month != 4 && month != 6 && month != 9 && month != 11){
            return false;
        }
        if(month == 2 && day > 29){
            return false;
        }
        if(month == 2 && day < 1){
            return false;
        }
        if(month == 4 || month == 6 || month == 9 || month == 11 && day > 30){
            return false;
        }
        if(year < 1){
            return false;
        }
        return true;
    }
}














































































































































































































































