        if (date.length() == 0) return false;
        if (date.length() != 10) return false;
        if (!Character.isDigit(date.charAt(2)) || !Character.isDigit(date.charAt(5))) return false;
        if (!Character.isDigit(date.charAt(8)) && !Character.isDigit(date.charAt(9))) return false;
        if (date.charAt(4) != '-') return false;

        int month = Integer.parseInt(date.substring(0,2));
        int day = Integer.parseInt(date.substring(3,5));
        int year = Integer.parseInt(date.substring(6,10));

        if (month < 1 || month > 12) return false;
        if (day < 1 || day > (year % 100 != 0 && year % 4 == 0 ? 29 : 31)) return false;
        return true;
    }
}

