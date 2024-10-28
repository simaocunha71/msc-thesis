    List<String> words = new ArrayList<>(Arrays.asList(sentence.split(" ")));
    List<String> primeList = new ArrayList<>();
    for (int i = 2; i < 101; i++) {
        if (isPrime(i)) {
            primeList.add(String.valueOf(i));
        }
    }
    StringBuilder sb = new StringBuilder();
    for (String word : words) {
        if (primeList.contains(String.valueOf(word.length()))) {
            sb.append(word + " ");
        }
    }
    sb.deleteCharAt(sb.length() - 1);
    return sb.toString();
    }

    public boolean isPrime(int number) {
    if (number < 2) return false;
    if (number == 2) return true;
    if (number % 2 == 0) return false;
    for (int i = 3; i * i <= number; i += 2) {
        if (number % i == 0) return false;
    }
    return true;
    }
}



















*/


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

