        if (text.length() == 0) {
            return Optional.empty();
        } else {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(text.getBytes());
            byte[] digest = md.digest();
            return Optional.of(String.format("%032x", new BigInteger(1, digest)));
        }
    }
}

