    if a == b {
        return nil
    }
    if _, ok := a.(string); ok {
        if _, ok := b.(string); ok {
            if strings.Contains(a.(string), ".") && strings.Contains(b.(string), ".") {
                if strings.Index(a.(string), ".") == 0 {
                    if strings.Index(b.(string), ".") == 0 {
                        if float64(a.(string)[1:]) > float64(b.(string)[1:]) {
                            return a
                        } else {
                            return b
                        }
                    } else if strings.Index(b.(string), ".") == 1 {
                        if float64(a.(string)[1:]) > float64(b.(string)) {
                            return a
                        } else {
                            return b
                        }
                    } else {
                        if float64(a.(string)) > float64(b.(string)[1:]) {
                            return a
                        } else {
                            return b
                        }
                    }
                } else {
                    if strings.Index(b.(string), ".") == 0 {
                        if float64(a.(string)) > float64(b.(string)[1:]) {
                            return a
                        } else {
                            return b
                        }
                    } else if strings.Index(b.(string), ".") == 1 {
                        if float64(a.(string)) > float64(b.(string)) {
                            return a
                        } else {
                            return b
                        }
                    } else {
                        if float64(a.(string)) > float64(b.(string)) {
                            return a
                        } else {
                            return b
                        }
                    }
                }
            } else if strings.Contains(a.(string), ".") {
                if float64(a.(string)) > float64(b.(string)) {
                    return a
                } else {
                    return b
                }
