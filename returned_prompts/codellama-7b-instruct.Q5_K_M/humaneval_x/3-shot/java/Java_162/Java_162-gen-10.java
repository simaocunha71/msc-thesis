        if (text.length() == 0) {
            return Optional.empty();
        }

        MessageDigest md = MessageDigest.getInstance("MD5");
        md.update(text.getBytes());
        byte[] digest = md.digest();
        return Optional.of(new BigInteger(1, digest).toString(16));
    }
}

