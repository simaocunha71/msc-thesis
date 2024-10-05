        StringBuilder result = new StringBuilder("db");
        while (decimal > 0) {
            result.append(decimal % 2);
            decimal = decimal >> 1;
        }
        result.append("db");
        return result.toString();
    }
}

