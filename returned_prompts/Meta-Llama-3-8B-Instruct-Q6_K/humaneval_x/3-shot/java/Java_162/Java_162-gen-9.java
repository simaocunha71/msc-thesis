        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md5 = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md5.digest(text.getBytes());
        return Optional.of(new BigInteger(1, hashBytes).toString(16));
    }
}

