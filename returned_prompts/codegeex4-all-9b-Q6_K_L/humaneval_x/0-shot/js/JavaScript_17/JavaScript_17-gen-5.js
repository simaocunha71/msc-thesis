```java
const parseMusic = (music_string) => {
  return music_string.split(" ").map(x => {
    if (x == "o") {return 4;}
    if (x == "o|") {return 2;}
    if (x == ".|") {return 1;}
  });
}
```
