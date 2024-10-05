let result = "";

for (let i = 0; i < a.length; i++) {
  result += a[i] ^ b[i];
}

return result;
}

console.log(stringXor("010", "110"));

// Expected Output: "100"

```

You can test the code by copy-pasting