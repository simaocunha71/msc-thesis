        String reversed_string = new StringBuilder(string).reverse().toString();
        for (int i = 0; i < string.length(); i++) {
            if (string.substring(i).equals(reversed_string.substring(0,string.length()-i))) {
                return string + reversed_string.substring(0,i);
            }
        }
        return null;
    }
}

