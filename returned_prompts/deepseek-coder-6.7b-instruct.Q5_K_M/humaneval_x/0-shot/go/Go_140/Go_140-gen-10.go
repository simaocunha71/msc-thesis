
	r := strings.Replace(text, " ", "_", -1)

	for strings.Contains(r, "__") {
		r = strings.Replace(r, "__", "-", -1)
	}

	return r
}

// Testing
func main() {
	fmt.Println(FixSpaces("Example"))
	fmt.Println(FixSpaces("Example 1"))
	fmt.Println(FixSpaces(" Example 2"))
	fmt.Println(FixSpaces(" Example  3"))
}

```


## Swift

```swift
import Foundation

func fixSpaces(text: String) -> String {
    let replacedByUnderscores = text.replacingOccurrences(of: " ", with: "_", options: .global)
    var result = replacedByUnderscores
    
    while true {
        let range = replacedByUnderscores.rangeOfString("__")
        
        if range.location == NSNotFound {
            break
        }
        
        result = result.replacingOccurrences(of: "__", with: "-", options: .global)
    }
    
    return result
}

// Testing
print(fixSpaces(text: "Example"))
print(fixSpaces(text: "Example 1"))
print(fixSpaces(text: " Example 2"))
print(fixSpaces(text: " Example  3"))
```

## Javascript

```javascript
function fixSpaces(text) {
    let replacedByUnderscores = text.replace(/ /g, "_");
    let result = replacedByUnderscores;
    
    while (true) {
        const range = replacedByUnderscores.search(/__/g);
        
        if (range === -1) {
            break;
        }
        
        result = result.replace(/__/g, "-");
    }
    
    return result;
}

// Testing
console.log(fixSpaces("Example"));
console.log(fixSpaces("Example 1"));
console.log(