        // Write your solution here
        text = text.toLowerCase();
        String reversed = new StringBuilder(text).reverse().toString();
        return text.equals(reversed);
    }
}

