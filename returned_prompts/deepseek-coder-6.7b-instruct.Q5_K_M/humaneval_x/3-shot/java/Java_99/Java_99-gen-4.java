        double num = Double.parseDouble(value);
        int lower = (int) Math.floor(num);
        int upper = (int) Math.ceil(num);
        if (num > 0) return upper;
        else return lower;
    }
}

