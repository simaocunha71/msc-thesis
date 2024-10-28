    int len = string.length();
    int i = 0;
    for(i = len; i >= 0; i--) {
        if(isPalindrome(string.substring(0, i))) {
            break;
        }
    }
    if(i == len) {
        return string;
    }
    String suffix = string.substring(i, len);
    String prefix = string.substring(0, i);
    StringBuilder builder = new StringBuilder(suffix);
    return prefix + builder.reverse().toString() + suffix;

B:
    }

C:
}
```

