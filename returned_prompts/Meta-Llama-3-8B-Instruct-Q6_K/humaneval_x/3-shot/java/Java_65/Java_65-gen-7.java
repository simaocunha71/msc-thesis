        String str = String.valueOf(x);
        String result = str.substring(shift % str.length()) + str.substring(0, shift % str.length());
        return result;
    }
}

