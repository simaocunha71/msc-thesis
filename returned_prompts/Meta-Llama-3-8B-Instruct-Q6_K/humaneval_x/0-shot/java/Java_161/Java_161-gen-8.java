        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(Character.toUpperCase(c));
                }
            } else {
                sb.append(c);
            }
        }
        return sb.reverse().toString();
    }
}
S:
    public String solve(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    sb.append(Character.toLowerCase(c));
                } else {
                    sb.append(Character.toUpperCase(c));
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }S:
    public String solve(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            if (Character.isLetter(c)) {
                if (Character.isUpperCase(c)) {
                    sb.append((char)(c + 32));
                } else {
                    sb.append((char)(c - 32));
                }
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }
    Here, the problem is asking for the solution to be implemented using the Java programming language. The task is to create a function called "solve" that takes a string "s" as an input and returns a new string with the following rules:
    1. If the character is a letter, reverse its case from lower to upper or vice versa.
    2. If the string contains no letters, reverse the string.
    The examples provided in the problem statement are:
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    Here is the solution implemented in Java:
    In the solution, we use a StringBuilder to construct the resulting string. We iterate over the input string from the end to the start. If the character is a letter, we reverse its case using the Character.toLowerCase() and Character.toUpperCase() methods. If the character is not a letter, we append it to the StringBuilder as