        double num = Double.parseDouble(value);
        int floor = (int)Math.floor(num);
        int ceil = (int)Math.ceil(num);

        if (Math.abs(num - floor) < Math.abs(num - ceil)) {
            return floor;
        } else if (Math.abs(num - floor) > Math.abs(num - ceil)) {
            return ceil;
        } else {
            if (num > 0) {
                return ceil;
            } else {
                return floor;
            }
        }
    }
}

