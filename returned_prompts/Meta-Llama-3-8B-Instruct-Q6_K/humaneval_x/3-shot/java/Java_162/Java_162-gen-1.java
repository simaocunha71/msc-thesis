        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        return Optional.of(new BigInteger(1, hashBytes).toString(16));
    }
}

