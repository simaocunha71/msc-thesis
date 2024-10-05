        if (date.isEmpty()) {
            return false;
        }
        String[] arr = date.split("-");
        if (arr.length != 3) {
            return false;
        }

        int month = Integer.parseInt(arr[0]);
        int day = Integer.parseInt(arr[1]);
        int year = Integer.parseInt(arr[2]);

        if (month < 1 || month > 12) {
            return false;
        }

        if (day < 1 || day > 31) {
            if (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
                return false;
            }
        } else if (day > 30) {
            if (month != 2 && month != 4 && month != 6 && month != 9 && month != 11) {
                return false;
            }
        } else if (month == 2 && day > 29) {
            return false;
        }

        if (year < 0) {
            return false;
        }
        return true;
    }
}










































































































































































































































