    eaten = number
    remaining_carrots = remaining - (need - eaten)
    return [eaten + need - remaining_carrots, remaining_carrots] if remaining_carrots >= 0 else [eaten + remaining, 0]  # if remaining_carrots < 0, it means we ate all remaining carrots, so we return eaten + remaining, 0


