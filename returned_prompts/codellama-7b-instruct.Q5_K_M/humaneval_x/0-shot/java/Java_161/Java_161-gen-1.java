        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                if (Character.isUpperCase(s.charAt(i))) {
                    s.setCharAt(i, Character.toLowerCase(s.charAt(i)));
                } else {
                    s.setCharAt(i, Character.toUpperCase(s.charAt(i)));
                }
            }
        }
        return s;
    }
}

B:
public String solve(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                if (Character.isUpperCase(s.charAt(i))) {
                    result.append(Character.toLowerCase(s.charAt(i)));
                } else {
                    result.append(Character.toUpperCase(s.charAt(i)));
                }
            } else {
                result.append(s.charAt(i));
            }
        }
        return result.toString();
    }

C:
public String solve(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                result.append(Character.isUpperCase(s.charAt(i)) ?
                        Character.toLowerCase(s.charAt(i)) :
                        Character.toUpperCase(s.charAt(i)));
            } else {
                result.append(s.charAt(i));
            }
        }
        return result.toString();
    }

D:
public String solve(String s) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (Character.isLetter(s.charAt(i))) {
                result.append(Character.toUpperCase(s.charAt(i)) == s.charAt(