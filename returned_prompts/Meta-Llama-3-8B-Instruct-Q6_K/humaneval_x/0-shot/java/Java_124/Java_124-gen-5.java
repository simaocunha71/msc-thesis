Here is a Java function that validates a given date string according to the rules provided:

```java
public boolean validDate(String date) {
    if(date.isEmpty()) {
        return false;
    }
    String[] parts = date.split("-");
    if(parts.length != 3) {
        return false;
    }
    int month = Integer.parseInt(parts[0]);
    int day = Integer.parseInt(parts[1]);
    int year = Integer.parseInt(parts[2]);
    
    if(month < 1 || month > 12) {
        return false;
    }
    if(month == 2) {
        if(day < 1 || day > 29) {
            return false;
        }
    } else if(month == 4 || month == 6 || month == 9 || month == 11) {
        if(day < 1 || day > 30) {
            return false;
        }
    } else {
        if(day < 1 || day > 31) {
            return false;
        }
    }
    return true;
}
```

This function splits the date string into three parts: month, day, and year. It then checks each part against the rules provided. If any of the parts fail to meet the rules, the function returns false. If all the parts meet the rules, the function returns true. 

Note that this function does not check if the year is valid (i.e., it does not check if the year is within a certain range or if it is a leap year). It only checks the month and day. If you need to check the year as well, you will need to add additional code to do so. 

Also, this function assumes that the date string is in the format "mm-dd-yyyy". If the date string is in a different format, you will need to modify the function accordingly. For example, if the date string is in the format "dd-mm-yyyy", you will need to swap the month and day parts before parsing them as integers. 

Finally, this function does not handle exceptions that may occur when parsing the date string. For example, if the date string is "abc-def-1234", the function will throw a NumberFormatException when it tries to parse the month and day parts as integers. To handle such exceptions, you can wrap the code that parses the date string in a try-catch block. 

Here is how you can modify the function to handle exceptions:

```java
public boolean validDate(String date) {
    try {
        if