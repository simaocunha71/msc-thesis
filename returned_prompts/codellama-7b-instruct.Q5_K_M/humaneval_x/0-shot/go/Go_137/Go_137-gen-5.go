    switch at := a.(type) {
        case int:
            switch bt := b.(type) {
                case int:
                    if at > bt {
                        return at
                    }
                    if at < bt {
                        return bt
                    }
                    return nil
                case float64:
                    return bt
                case string:
                    return bt
            }
        case float64:
            switch bt := b.(type) {
                case int:
                    return at
                case float64:
                    if at > bt {
                        return at
                    }
                    if at < bt {
                        return bt
                    }
                    return nil
                case string:
                    return bt
            }
        case string:
            switch bt := b.(type) {
                case int:
                    return bt
                case float64:
                    return bt
                case string:
                    if at > bt {
                        return at
                    }
                    if at < bt {
                        return bt
                    }
                    return nil
            }
    }

    return nil
}


