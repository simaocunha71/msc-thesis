Here is the solution for the problem:

```javascript
const strongestExtension = (class_name, extensions) => {
    let strongest = null;
    let maxStrength = -Infinity;

    for (let extension of extensions) {
        let cap = 0;
        let sm = 0;

        for (let char of extension) {
            if (char.toUpperCase() === char) {
                cap++;
            } else {
                sm++;
            }
        }

        let strength = cap - sm;
        if (strength > maxStrength) {
            strongest = extension;
            maxStrength = strength;
        }
    }

    return class_name + '.' + strongest;
};
```



In this function, we iterate over each extension in the list. For each extension, we calculate its strength by counting the number of uppercase letters and lowercase letters. We then compare this strength with our current maximum strength. If the new strength is greater, we update our strongest extension and maximum strength. Finally, we return the class name followed by the strongest extension. If there are multiple extensions with the same maximum strength, we will return the first one we encounter.