        String[] parts = date.split("-");
        if (parts.length != 3) return false;
        if (parts[0].length() != 2 || parts[1].length() != 2 || parts[2].length() != 4) return false;
        for (String part : parts) {
            if (!part.matches("[0-9]+")) return false;
        }
        int month = Integer.parseInt(parts[0]);
        int day = Integer.parseInt(parts[1]);
        int year = Integer.parseInt(parts[2]);
        int[] daysInMonth = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (month < 1 || month > 12 || day < 1 || day > daysInMonth[month - 1]) return false;
        return true;
    }
}

