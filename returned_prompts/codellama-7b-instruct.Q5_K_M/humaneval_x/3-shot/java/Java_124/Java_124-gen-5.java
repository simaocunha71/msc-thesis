        if (date.isEmpty() || date.length() != 10) return false;

        String[] parts = date.split("-");

        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > 31) return false;

        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                if (day < 1 || day > 31) return false;
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                if (day < 1 || day > 30) return false;
                break;
            case 2:
                if (day < 1 || day > 29) return false;
                break;
            default:
                return false;
        }

        return true;
    }
}

