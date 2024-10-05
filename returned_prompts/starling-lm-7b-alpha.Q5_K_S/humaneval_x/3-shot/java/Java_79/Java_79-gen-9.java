        String result = "db";
        while (decimal > 0) {
            int remainder = decimal % 2;
            result += remainder;
            decimal = decimal / 2;
        }
        result += "db";
        return result;
    }
}

