        if (text.isEmpty()) {
            return Optional.empty();
        } else {
            MessageDigest md = MessageDigest.getInstance("MD5");
            md.update(text.getBytes());
            return Optional.of(new BigInteger(1, md.digest()).toString(16));
        }
    }
}

