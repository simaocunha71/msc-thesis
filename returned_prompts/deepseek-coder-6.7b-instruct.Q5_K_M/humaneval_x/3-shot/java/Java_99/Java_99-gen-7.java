        double num = Double.parseDouble(value);
        if (num < 0) {
            return (int)Math.floor(num - 0.5);
        } else {
            return (int)Math.ceil(num + 0.5);
        }
    }
}

