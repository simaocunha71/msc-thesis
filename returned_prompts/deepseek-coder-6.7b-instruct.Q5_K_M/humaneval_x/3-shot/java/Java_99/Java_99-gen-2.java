        double num = Double.parseDouble(value);
        int intNum = (int) Math.floor(num);
        return (num >= 0) ? intNum : intNum - 1;
     }
}

