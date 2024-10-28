        String result = "db";
        result += String.format("%32s", Integer.toBinaryString(decimal)).replace(' ', '0');
        result += "db";
        return result;
    }
}


