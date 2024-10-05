    int count = 0;
    for (char c : s) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y' && s.back() == 'y') {
            count++;
        }
    }
    return count;
}  // Time Complexity: O(n), where n is the length of the string. Space Complexity: O(1), as we are not using any extra space.