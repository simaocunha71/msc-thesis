        if (text.length() == 0)
            return Optional.empty();
        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] bytes = md.digest();
        BigInteger bi = new BigInteger(1, bytes);
        String hash = String.format("%32s", bi.toString(16));
        return Optional.of(hash);
    }
}

