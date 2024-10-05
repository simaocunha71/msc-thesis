    string result = "";
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (c >= 'a' && c <= 'z') {
            c = (c - 'a' + 2 * 2) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            c = (c - 'A' + 2 * 2) % 26 + 'A';
        }
        result += c;
    }
    return result;
}  // This code is not tested and may have bugs, but it should give you the idea of how to solve the problem. The idea is to shift the letters down by 2 * 2 = 4 places. We do this by subtracting the ASCII value of 'a' or 'A' (depending on whether the letter is lowercase or uppercase) and then adding 4, and taking the modulus with 26 to ensure we wrap around the alphabet. We then add the ASCII value back to get the encrypted character.  // This code is not tested and may have bugs, but it should give you the idea of how to solve the problem. The idea is to shift the letters down by 2 * 2 = 4 places. We do this by subtracting the ASCII value of 'a' or 'A' (depending on whether the letter is lowercase or uppercase) and then adding 4, and taking the modulus with 26 to ensure we wrap around the alphabet. We then add the ASCII value back to get the encrypted character.  // This code is not tested and may have bugs, but it should give you the idea of how to solve the problem. The idea is to shift the letters down by 2 * 2 = 4 places. We do this by subtracting the ASCII value of 'a' or 'A' (depending on whether the letter is lowercase or uppercase) and then adding 4, and taking the modulus with 26 to ensure we wrap around the alphabet. We then add the ASCII value back to get the encrypted character.  // This code is not tested and may have bugs, but it should give you the idea of how to solve the problem. The idea is to shift the letters down by 2 * 2 = 4 places. We do this by subtracting the ASCII value of 'a' or 'A' (depending on whether the letter is lowercase