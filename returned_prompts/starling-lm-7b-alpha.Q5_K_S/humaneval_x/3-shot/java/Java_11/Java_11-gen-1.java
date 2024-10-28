        char[] result = new char[a.length()];
        for (int i = 0; i < a.length(); i++) {
            result[i] = (char) (a.charAt(i) ^ b.charAt(i));
        }
        return new String(result);
    }
}

