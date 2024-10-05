        double num = Double.parseDouble(value);
        return (int)Math.floor(num) == (int)Math.ceil(num) ? (int)Math.round(num) : (int)Math.floor(num);
     }
}

