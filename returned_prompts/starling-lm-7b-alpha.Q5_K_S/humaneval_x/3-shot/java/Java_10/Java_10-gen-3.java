        String result = string;
        int i = string.length() - 1;
        while (i >= 0) {
            String suffix = string.substring(i);
            if (isPalindrome(suffix)) {
                result = string.substring(0, i) + result;
                break;
            }
            i--;
        }
        String prefix = string.substring(0, i + 1);
        return result + new StringBuilder(prefix).reverse().toString() + result.substring(0, i + 1);
    }
}

