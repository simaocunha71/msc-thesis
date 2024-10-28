        double number = Double.parseDouble(value);
        int floor_val = (int)Math.floor(number);
        int ceil_val = (int)Math.ceil(number);

        if (Math.abs(number - floor_val) < Math.abs(number - ceil_val)) {
            return floor_val;
        } else if (Math.abs(number - floor_val) > Math.abs(number - ceil_val)) {
            return ceil_val;
        } else {
            return (number < 0) ? ceil_val : floor_val;
        }
     }
}

