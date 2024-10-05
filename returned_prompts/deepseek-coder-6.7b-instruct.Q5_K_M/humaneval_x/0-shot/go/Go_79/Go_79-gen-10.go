	binary := ""

	
	if decimal == 0 {
		return "db0db"
	}

B:
	for decimal > 0 {
		remainder := decimal % 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
		decimal = decimal / 2
	}

C:
	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}

```



## PicoLisp

```PicoLisp
(de DecimalToBinary
   (n)
   (let (bin "")
      (while (> n 0)
         (setq bin (cons (rem n 2) bin))
         (div n 2) )
      (str "db" (str/in " " bin) "db") ) )
```


## Perl

```perl
sub DecimalToBinary {
    my $decimal = shift;
    return "db0db" if $decimal == 0;
    my $binary = "";
    while ($decimal > 0) {
        $binary = ($decimal % 2).$binary;
        $decimal = int($decimal / 2);
    }
    return "db$binary db";
}

print DecimalToBinary(15), "\n";
print DecimalToBinary(32), "\n";
```


## Perl 6

```perl6
sub DecimalToBinary ($decimal) {
    return 'db0db' if $decimal == 0;
    my $binary = '';
    loop {
        last if $decimal < 1;
        $binary ~= ($decimal % 2).$binary;
        $decimal /= 2;
    }
    return 'db' ~ $binary ~ 'db';
}

say DecimalToBinary(15);
say DecimalToBinary(32);
```


## Swift

```swift
import Foundation

func DecimalToBinary(decimal: Int) ->