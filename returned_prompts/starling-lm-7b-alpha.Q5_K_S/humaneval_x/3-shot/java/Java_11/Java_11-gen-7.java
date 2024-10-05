        StringBuilder result = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            char c = (char) ((a.charAt(i) - '0') ^ (b.charAt(i) - '0') + '0');
            result.append(c);
        }
        return result.toString();
    }
}

