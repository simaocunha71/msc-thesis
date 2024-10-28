        String[] parts = date.split("-");
        if (parts.length != 3) return false;

        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;
        if (year < 0 || year > 9999) return false;

        if (month == 2 && day > 29) return false;
        if (month == 2 && day <= 0) return false;

        if (month == 4 || month == 6 || month == 9 || month == 11) {
            if (day > 30) return false;
            if (day <= 0) return false;
        }
        if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12) {
            if (day > 31) return false;
            if (day <= 0) return false;
        }
        return true;
    }
}

public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.0, 3.0), 0.5));
        System.out.println(solution.hasCloseElements(Arrays.asList(1.0, 2.8, 3.0, 4.0, 5.0, 2.0), 0.3));
        System.out.println(solution.separateParenGroups("( ) (( )) (( )( ))"));
        System.out.println(solution.truncateNumber(3.5));
        System.out.println(solution.validDate("03-11-2000"));
        System.out.println(solution.validDate("15-01-2012"));
        System.out