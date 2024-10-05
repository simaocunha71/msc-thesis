        MessageDigest digest = MessageDigest.getInstance("MD5");
        digest.update(text.getBytes());
        byte[] md5 = digest.digest();
        StringBuilder sb = new StringBuilder();
        for (byte b : md5) {
            sb.append(String.format("%02x", b));
        }
        return Optional.of(sb.toString());
    }


    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.stringToMd5("Hello world").get());
    }
}



















```
```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```

```