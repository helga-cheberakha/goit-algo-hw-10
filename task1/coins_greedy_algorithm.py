def find_coins_greedy(amount: int) -> dict[int, int]:
    """
    Return coins for the amount, starting with
    the largest denomination.
    """
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    result = {}
    for coin in [50, 25, 10, 5, 2, 1]:
        if amount == 0:
            break

        # Take as many coins of this denomination as possible.
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount %= coin

    return result
