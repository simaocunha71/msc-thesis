        String result = "db";

        for (int i = 0; i < 8; i++) {
            result += (decimal % 2);
            decimal /= 2;
        }
        result += "db";
        return result;
    }
}


