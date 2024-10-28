        String[] split = date.split("-");
        int days = Integer.parseInt(split[1]);
        int month = Integer.parseInt(split[0]);
        int year = Integer.parseInt(split[2]);

        if (date.isEmpty() || days < 1 || days > 31 || month < 1 || month > 12 || year < 0) return false;
        else if (month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12)
            return days >= 1 && days <= 31;
        else if (month == 4 || month == 6 || month == 9 || month == 11)
            return days >= 1 && days <= 30;
        else if (month == 2)
            return days >= 1 && days <= 29;
        else
            return true;

    }
}

