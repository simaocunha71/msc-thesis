        // Base case for when the string is less than 3 characters
        if (s.length() < 3) return false;

        // Loop through the string
        for (int i = 0; i < s.length()-2; i++) {
            // Check if the 3 consecutive characters are distinct
            if (s.charAt(i) == s.charAt(i+1) || s.charAt(i+1) == s.charAt(i+2) || s.charAt(i) == s.charAt(i+2)) {
                return false;
            }
        }
        // If we have made it through the entire string without finding any non-distinct 3 character sequences, return true
        return true;
    }
}

