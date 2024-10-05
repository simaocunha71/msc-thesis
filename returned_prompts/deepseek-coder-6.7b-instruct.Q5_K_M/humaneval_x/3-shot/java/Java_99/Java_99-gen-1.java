        double number = Double.parseDouble(value);
        int intPart = (int) number;
        double decimalPart = number - intPart;

        if (decimalPart < 0.5) return intPart;
        else if (number < 0) return intPart - 1;
        else return intPart + 1;
     }
}

