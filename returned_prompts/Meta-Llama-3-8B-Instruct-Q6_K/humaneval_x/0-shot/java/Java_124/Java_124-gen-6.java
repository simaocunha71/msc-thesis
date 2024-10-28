    public boolean validDate(String date) {
        if(date.length()!=10) return false;
        String[] parts = date.split("-");
        if(parts.length!=3) return false;
        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);
        if(month<1 || month>12) return false;
        if((month==4 || month==6 || month==9 || month==11) && day>30) return false;
        if((month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) && day>31) return false;
        if(month==2) {
            if(year%4==0) {
                if(day>29) return false;
            } else {
                if(day>28) return false;
            }
        }
        return true;
    }  // false for invalid date, true for valid date.  // valid for invalid date, true for valid date.

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.validDate("03-11-2000"));  // true
        System.out.println(solution.validDate("15-01-2012"));  // false
        System.out.println(solution.validDate("04-0-2040"));  // false
        System.out.println(solution.validDate("06-04-2020"));  // true
        System.out.println(solution.validDate("06/04/2020"));  // false
    }  // false for invalid date, true for valid date.  // valid for invalid date, true for valid date.