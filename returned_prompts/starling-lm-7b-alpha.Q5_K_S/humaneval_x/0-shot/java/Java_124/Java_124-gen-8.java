        int[] days = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String[] dateArray = date.split("-");
        if (dateArray.length != 3) {
            return false;
        }
        if (dateArray[0].length() != 2 || dateArray[1].length() != 2 || dateArray[2].length() != 4) {
            return false;
        }
        for (int i = 0; i < 3; i++) {
            if (!dateArray[i].matches("\\d+")) {
                return false;
            }
        }
        int month = Integer.parseInt(dateArray[0]);
        int day = Integer.parseInt(dateArray[1]);
        int year = Integer.parseInt(dateArray[2]);

        if (month < 1 || month > 12) {
            return false;
        }
        if (day < 1 || day > days[month - 1]) {
            return false;
        }
        if (year < 0) {
            return false;
        }
        return true;
    }
}



















































































































































































































