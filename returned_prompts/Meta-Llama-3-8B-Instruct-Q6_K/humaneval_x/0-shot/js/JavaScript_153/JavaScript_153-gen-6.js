```javascript
function strongestExtension(class_name, extensions) {
    let max_strength = -Infinity;
    let strongest_extension = '';
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
        if (strength > max_strength) {
            max_strength = strength;
            strongest_extension = extension;
        }
    }
    return class_name + '.' + strongest_extension;
}
```