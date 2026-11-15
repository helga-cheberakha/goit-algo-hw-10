def find_min_coins(amount: int) -> dict[int, int]:
    """
    Use dynamic programming to find the minimum count of coins
    for each amount, then reconstruct the selected combination.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    # Store the fewest coins needed for each amount.
    # Use amount + 1 as an initial value larger than
    # any valid count, start from 0.
    min_counts = [amount + 1] * (amount + 1)
    min_counts[0] = 0
    # Store the last coin selected for each amount.
    # Use 0 as an initial value.
    last_coins = [0] * (amount + 1)

    for current_amount in range(1, amount + 1):
        for coin in [50, 25, 10, 5, 2, 1]:
            if coin > current_amount:
                continue

            count = min_counts[current_amount - coin] + 1
            # Save the new combination if it uses less amount of coins.
            if count < min_counts[current_amount]:
                min_counts[current_amount] = count
                last_coins[current_amount] = coin

    result = {}
    while amount > 0:
        # Get the last coin selected for the current amount.
        # Increase its count in the result if it is already
        # there, or set its count to 1 if this is the first
        # time it is used.
        coin = last_coins[amount]
        result[coin] = result.get(coin, 0) + 1

        # Reduce the amount by the coin value to find the next
        # coin for the remaining amount.
        amount -= coin

    return result
