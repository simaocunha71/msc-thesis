    can_eat = min(need, remaining)
    total_eaten = number + can_eat
    left_over = remaining - can_eat
    return [total_eaten, left_over]


