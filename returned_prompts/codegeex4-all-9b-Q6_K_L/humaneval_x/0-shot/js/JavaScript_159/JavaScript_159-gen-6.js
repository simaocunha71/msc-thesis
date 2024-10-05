```
  if (number + need > remaining) {
    return [remaining + number, 0];
  } else {
    return [number + need, remaining - need];
  }
};
```