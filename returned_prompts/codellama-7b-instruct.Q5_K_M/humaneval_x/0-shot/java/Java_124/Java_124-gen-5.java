import java.util.*;
import java.lang.*;

class Solution {
    public boolean validDate(String date) {
        String[] arr = date.split("-");
        int month = Integer.parseInt(arr[0]);
        int day = Integer.parseInt(arr[1]);
        int year = Integer.parseInt(arr[2]);
        if(month < 1 || month > 12 || day < 1 || day > 31 || year < 0)
            return false;
        if(month == 4 || month == 6 || month == 9 || month == 11)
            if(day < 1 || day > 30)
                return false;
        if(month == 2)
            if(day < 1 || day > 28)
                return false;
        if(month == 2 && year % 4 == 0)
            if(day > 29)
                return false;
        return true;
    }
}
