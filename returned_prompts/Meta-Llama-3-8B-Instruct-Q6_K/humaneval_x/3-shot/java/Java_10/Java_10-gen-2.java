        String reversed = new StringBuilder(string).reverse().toString();
        for (int i = 0; i < reversed.length(); i++) {
            if (isPalindrome(string + reversed.substring(i))) {
                return string + reversed.substring(i);
            }
        }
        return string + reversed;
    }
}

