        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] bytes = md.digest(text.getBytes());
        return Optional.of(new BigInteger(1, bytes).toString(16).toUpperCase());
    }
}

