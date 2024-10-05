        String cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lower = "abcdefghijklmnopqrstuvwxyz";
        String cap_strength = "";
        String lower_strength = "";
        int cap_count = 0;
        int lower_count = 0;
        String strongest_extension = "";
        int strongest_strength = 0;
        for (int i = 0; i < extensions.size(); i++) {
            cap_count = 0;
            lower_count = 0;
            String cur_ext = extensions.get(i);
            for (int j = 0; j < cap.length(); j++) {
                if (cur_ext.contains(cap.charAt(j) + "")) {
                    cap_count++;
                }
            }
            for (int j = 0; j < lower.length(); j++) {
                if (cur_ext.contains(lower.charAt(j) + "")) {
                    lower_count++;
                }
            }
            int strength = cap_count - lower_count;
            if (strength > strongest_strength || strength == strongest_strength && cur_ext.compareTo(strongest_extension) < 0) {
                strongest_strength = strength;
                strongest_extension = cur_ext;
            }
        }
        return class_name + "." + strongest_extension;
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
