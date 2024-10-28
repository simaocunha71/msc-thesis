
    }
}

// Encoding a message
// Swaps case of all letters
// Replaces all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet.
// Assume only letters.

public String encode(String message) {
    StringBuilder sb = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isAlphabetic(c)) {
            c = Character.toLowerCase(c);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c += 2;
            } else {
                c ^= 'a' ^ 'A';
                c += Character.isUpperCase(c) ? -'A' : -'a';
            }
        }
        sb.append(c);
    }
    return sb.toString();
}

// Encoding a message
// Swaps case of all letters
// Replaces all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet.
// Assume only letters.

public String encode(String message) {
    StringBuilder sb = new StringBuilder();
    for (char c : message.toCharArray()) {
        if (Character.isAlphabetic(c)) {
            c = Character.toLowerCase(c);
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c += 2;
            } else {
                c ^= 'a' ^ 'A';
                c += Character.isUpperCase(c) ? -'A' : -'a';
            }
        }
        sb.append(c);
    }
    return sb.toString();
}

// Encoding a message
// Swaps case of all letters
// Replaces all vowels with the letter that appears 2 places ahead of that vowel in the english alphabet.
// Assume only letters.

public String encode(String message) {
    StringBuilder sb = new StringBuilder();
    for (