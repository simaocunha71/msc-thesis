        if (date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-')
            return false;

        int month = Integer.parseInt(date.substring(0, 2));
        int day = Integer.parseInt(date.substring(3, 5));
        int year = Integer.parseInt(date.substring(6));

        if (month < 1 || month > 12 || day < 1 || year < 1)
            return false;

        if (month == 2) {
            if (day > 29 || day < 1)
                return false;
        } else if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30 || day < 1)
                return false;
        } else {
            if (day > 31 || day < 1)
                return false;
        }

        return true;
    }
}


A: There is a small bug in your code. You have to check the day for months with 30 days and also for February, where the day can't be more than 28 and less than 1.

So, the updated code should be:

```java
public boolean validDate(String date) {

    if (date.length() != 10 || date.charAt(2) != '-' || date.charAt(5) != '-')
        return false;

    int month = Integer.parseInt(date.substring(0, 2));
    int day = Integer.parseInt(date.substring(3, 5));
    int year = Integer.parseInt(date.substring(6));

    if (month < 1 || month > 12 || day < 1 || year < 1)
        return false;

    if (month == 2) {
        if (day > 28 || day < 1)
            return false;
    } else if (month == 4 || month == 6 || month == 9 || month == 11) {
        if (day > 30 || day < 1)
            return false;
    } else {
        if (