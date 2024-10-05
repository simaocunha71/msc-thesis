
    // Checking the type of a and b
    if (typeof a === "string") {
        // If a is a string, replace the ',' with '.' and convert to float
        a = parseFloat(a.replace(",", "."));
    }
    if (typeof b === "string") {
        // If b is a string, replace the ',' with '.' and convert to float
        b = parseFloat(b.replace(",", "."));
    }

    // Comparing a and b
    if (a > b) {
        return a;
    } else if (b > a) {
        return b;
    } else {
        return null;
    }
}
console.log(compareOne(1, 2.5))  // 2.5
console.log(compareOne(1, "2,3"))  // "2.3"
console.log(compareOne("5,1", "6"))  // "6"
console.log(compareOne("1", 1))  // null
```

## 4. Extract the domain name from a URL

