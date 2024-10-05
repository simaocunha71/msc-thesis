        // Split date into month, day, and year
        String[] splitDate = date.split("-");

        // Check if date is in correct format
        if(splitDate.length != 3) {
            return false;
        }

        // Check if all parts of the date are not empty
        for(String part : splitDate) {
            if(part.isEmpty()) {
                return false;
            }
        }

        // Convert parts of date to integers
        int month = Integer.parseInt(splitDate[0]);
        int day = Integer.parseInt(splitDate[1]);
        int year = Integer.parseInt(splitDate[2]);

        // Check if month is valid
        if(month < 1 || month > 12) {
            return false;
        }

        // Check if day and month are valid
        if((month == 4 || month == 6 || month == 9 || month == 11) && (day < 1 || day > 30)) {
            return false;
        } else if((month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) && (day < 1 || day > 31)) {
            return false;
        } else if(month == 2 && (day < 1 || day > 29)) {
            return false;
        }

        // Check if year is valid
        if(year < 1 || year > 9999) {
            return false;
        }

        // If all checks pass, return true
        return true;
    }
}

*/

public class Main
{
    public static void main(String[] args)
    {
        Solution sol = new Solution();
        System.out.println(sol.validDate("03-11-2000")); // true
        System.out.println(sol.validDate("15-01-2012")); // false
        System.out.println(sol.validDate("04-0-2040")); // false
        System.out.println(sol.validDate("06-04-2020")); // true
       