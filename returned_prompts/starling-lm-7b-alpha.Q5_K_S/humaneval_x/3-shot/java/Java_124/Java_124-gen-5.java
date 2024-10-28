        String[] parts = date.split("-");
        if (parts.length == 3) {
            int month = Integer.parseInt(parts[0]);
            int day = Integer.parseInt(parts[1]);
            int year = Integer.parseInt(parts[2]);

            if (month >= 1 && month <= 12 && day >= 1 && day <= 31 && (year >= 0 && year <= 9999)) {
                if (month == 2 && day > 29) return false;
                if (month == 4 || month == 6 || month == 9 || month == 11) {
                    if (day > 30) return false;
                } else {
                    if (day > 31) return false;
                }
                return true;
            } else {
                return false;
            }
        } else {
            return false;
        }
    }
}


