        String result = "db";
        int current = decimal;
        int bit_index = 0;
        while (current > 0) {
            result += current % 2;
            current /= 2;
            bit_index += 1;
        }
        result += "db";
        return result.substring(0, bit_index + 2);
    }
}

