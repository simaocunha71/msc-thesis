        if (text.isEmpty()) {
            return Optional.empty();
        }
        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        BigInteger hash = new BigInteger(1, hashBytes);
        return Optional.of(String.format("%032x", hash));
    }
}

