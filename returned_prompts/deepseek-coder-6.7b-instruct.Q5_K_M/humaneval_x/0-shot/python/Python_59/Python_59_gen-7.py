
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

if __name__ == "__main__":
    import doctest
    doctest.testmod()


```


## Rust

```rust
fn largest_prime_factor(n: u64) -> u64 {
    let mut n = n;
    let mut i = 2;
    while i * i <= n {
        if n % i == 0 {
            n /= i;
        } else {
            i += 1;
        }
    }
    n
}

fn main() {
    assert_eq_eq(largest_prime_factor(13195), 29);
    assert_eq_eq(largest_prime_factor(2048), 2);
}
```


## Swift

```swift
func largest_prime_factor(n: Int) -> Int {
    var n = n
    var i = 2
    while i * i <= n {
        if n % i == 0 {
            n /= i
        } else {
            i += 1
        }
    }
    return n
}

print(largest_prime_factor(n: 13195)) // prints 29
print(largest_prime_factor(n: 2048)) // prints 2
```


## XSLT

```xslt
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template name="largest_prime_factor">
  <xsl:param name="n"/>
  <xsl:choose>
    <xsl:when test="$n mod 2 = 0">
      <xsl:value-of select="2"/>
    </xsl:when>
    <xsl:otherwise>
      <xsl:call-template name="largest_prime_factor">
