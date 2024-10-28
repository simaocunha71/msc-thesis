        String binary = "";
        if (decimal == 0) {
            return "db0db";
        }
        while (decimal > 0) {
            int remainder = decimal % 2;
            binary = remainder + binary;
            decimal /= 2;
        }
        return "db" + binary + "db";
    }
}

