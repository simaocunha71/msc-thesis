        String result = "db";
        String binary = Integer.toBinaryString(decimal);
        result += binary.length() < 16 ? "0".repeat(16 - binary.length()) : "";
        result += binary + "db";
        return result;
    }
}

