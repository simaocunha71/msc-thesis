        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String encrypted = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int position = alphabet.indexOf(c);
            int newPosition = (position + 2) % 26;
            encrypted += alphabet.charAt(newPosition);
        }
        return encrypted;
    }
}

*/


