        String reversed = new StringBuilder(string).reverse().toString();
        for (int i = 0; i < reversed.length(); i++) {
            String prefix = string.substring(0, string.length() - i);
            String postfix = reversed.substring(i);
            if (isPalindrome(postfix + prefix)) {
                return postfix + prefix;
            }
        }
        return string + reversed;
    }
}

