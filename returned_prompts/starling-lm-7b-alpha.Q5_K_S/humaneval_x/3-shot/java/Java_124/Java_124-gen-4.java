        String[] parts = date.split("-");
        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        if (parts.length != 3) {
            return false;
        }
        if (month < 1 || month > 12) {
            return false;
        }
        if (day < 1) {
            return false;
        }
        if (year < 0) {
            return false;
        }

        switch (month) {
            case 2:
                if (year % 4 != 0 || (year % 4 == 0 && day > 29)) {
                    return false;
                }
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                if (day > 30) {
                    return false;
                }
                break;
            default:
                if (day > 31) {
                    return false;
                }
        }

        return true;
    }
}

