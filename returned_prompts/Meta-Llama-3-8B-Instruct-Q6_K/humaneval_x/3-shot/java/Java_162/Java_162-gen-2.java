        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = text.getBytes();
        byte[] hashBytes = md.digest(bytes);
        StringBuilder hashString = new StringBuilder();
        for (byte b : hashBytes) {
            String hex = Integer.toHexString(0xFF & b);
            if (hex.length() == 1) {
                hashString.append('0');
            }
            hashString.append(hex);
        }
        return Optional.of(hashString.toString());
    }
}

