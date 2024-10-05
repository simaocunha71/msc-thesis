    // Nous allons utiliser une expression régulière pour trouver toutes les phrases.
    // L'expression cherche un mot alphanumérique (a-z, A-Z, 0-9, _),
    // suivi d'un point, d'une question ou d'un élément d'exclamation.
    re := regexp.MustCompile(`\b[a-zA-Z0-9_]+[.?!]`)

B:
    // Nous allons trouver toutes les phrases dans la chaîne.
    sentences := re.FindAllString(S, -1)

C:
    // Nous allons compter le nombre de phrases qui commencent par "I".
    count := 0
    for _, sentence := range sentences {
        if sentence[0] == 'I' {
            count++
        }
    }

D:
    // Nous allons retourner le compte.
    return count
}

```

## Test Cases

```go
package main

import (
    "fmt"
    "testing"
)

func TestIsBored(t *testing.T) {
    cases := []struct {
        in  