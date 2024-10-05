    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < message.length(); i++) {
        char c = message.charAt(i);
        if (c >= 'a' && c <= 'z') {
            sb.append((char)(c - 32));
        } else if (c >= 'A' && c <= 'Z') {
            sb.append((char)(c + 32));
        } else {
            sb.append(c);
        }
    }
    String result = sb.toString();
    char[] vowels = result.toLowerCase().toCharArray();
    for (int i = 0; i < vowels.length; i++) {
        if (vowels[i] == 'a') {
            vowels[i] = 'c';
        } else if (vowels[i] == 'e') {
            vowels[i] = 'g';
        } else if (vowels[i] == 'i') {
            vowels[i] = 'k';
        } else if (vowels[i] == 'o') {
            vowels[i] = 'q';
        } else if (vowels[i] == 'u') {
            vowels[i] = 's';
        }
    }
    return String.valueOf(vowels);
    }
}





















































































































































































