        if (date.isEmpty()) return false;
        if (!date.contains("-")) return false;

        String[] parts = date.split("-");
        if (parts.length != 3) return false;

        int month, day, year;
        try {
            month = Integer.parseInt(parts[0]);
            day = Integer.parseInt(parts[1]);
            year = Integer.parseInt(parts[2]);
        } catch (NumberFormatException e) {
            return false;
        }

        if (month < 1 || month > 12) return false;

        if (day < 1) return false;

        switch (month) {
            case 4: case 6: case 9: case 11:
                if (day > 30) return false;
                break;
            case 2:
                if (day > 29) return false;
                break;
            default:
                if (day > 31) return false;
        }

        return true;
     }
}

