        String pattern = "";
        String rotate = "";
        for (int i = 0; i < b.length(); i++) {
            pattern += b.charAt(i);
            rotate += b.charAt((b.length() - 1) - i);
        }
        return (a.contains(pattern) || a.contains(rotate));
    }
}

