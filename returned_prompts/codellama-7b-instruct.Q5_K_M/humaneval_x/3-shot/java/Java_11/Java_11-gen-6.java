        char[] result = new char[a.length()];

        for (int i = 0; i < a.length(); i++) {
            result[i] = (a.charAt(i) == b.charAt(i)) ? '0' : '1';
        }

        return new String(result);
    }
}

