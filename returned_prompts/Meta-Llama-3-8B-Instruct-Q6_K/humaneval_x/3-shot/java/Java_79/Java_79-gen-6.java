        String binary = Integer.toBinaryString(decimal);
        return "db" + new StringBuilder(binary).reverse().toString() + "db";
    }
} 