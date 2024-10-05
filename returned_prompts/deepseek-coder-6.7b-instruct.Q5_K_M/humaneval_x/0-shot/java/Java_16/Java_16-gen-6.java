        // Converting all the characters to lowercase to handle case insensitivity
        string = string.toLowerCase();

        // Using a HashSet to automatically remove duplicates and count the unique characters
        Set<Character> uniqueChars = new HashSet<>();

        for (int i = 0; i < string.length(); i++) {
            uniqueChars.add(string.charAt(i));
        }

        return uniqueChars.size();
    }
}

