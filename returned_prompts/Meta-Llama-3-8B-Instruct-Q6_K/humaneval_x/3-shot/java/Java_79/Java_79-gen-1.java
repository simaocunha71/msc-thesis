        String binary = Integer.toBinaryString(decimal);
        return "db" + String.format("%32s", binary).replace(' ', '0') + "db";
    }
}

