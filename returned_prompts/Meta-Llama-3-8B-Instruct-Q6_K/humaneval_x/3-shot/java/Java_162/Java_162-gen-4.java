        if (text.isEmpty()) {
            return Optional.empty();
        }

        MessageDigest md = MessageDigest.getInstance("MD5");
        byte[] hashBytes = md.digest(text.getBytes());
        BigInteger no = new BigInteger(1, hashBytes);
        return Optional.of(no.toString(16).toUpperCase());
    }
}

