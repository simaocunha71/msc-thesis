        String result = "db";
        while (decimal > 0) {
            result += String.valueOf(decimal % 2);
            decimal /= 2;
        }
        result += "db";
        return result;
    }
}

