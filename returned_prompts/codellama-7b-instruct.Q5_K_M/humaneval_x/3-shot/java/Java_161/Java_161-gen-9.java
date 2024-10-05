        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                if (Character.isLowerCase(s.charAt(i))) result.append(Character.toUpperCase(s.charAt(i)));
                else result.append(Character.toLowerCase(s.charAt(i)));
            } else result.append(s.charAt(i));
        }
        return result.toString();
    }
}

