        String result = "db";
        for (int i = 0; i < 32; i++) {
            int bit = (decimal >> i) & 1;
            result += bit;
        }
        result += "db";
        return result;
    }
}

