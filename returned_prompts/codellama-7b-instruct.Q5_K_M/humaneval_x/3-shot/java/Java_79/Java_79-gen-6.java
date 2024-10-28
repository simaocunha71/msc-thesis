        if (decimal == 0) return "db0db";
        StringBuilder result = new StringBuilder("db");
        while (decimal > 0) {
            result.insert(0, (decimal % 2) + "");
            decimal /= 2;
        }
        return result.append("db").toString();
    }
}

