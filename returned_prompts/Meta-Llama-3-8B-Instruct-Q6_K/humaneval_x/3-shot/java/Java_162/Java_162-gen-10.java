        if (text.isEmpty()) return Optional.empty();
        MessageDigest md5 = MessageDigest.getInstance("MD5");
        byte[] bytes = text.getBytes();
        byte[] hashBytes = md5.digest(bytes);
        StringBuilder sb = new StringBuilder();
        for (byte b : hashBytes) {
            sb.append(String.format("%02x", b));
        }
        return Optional.of(sb.toString());
    }
}

