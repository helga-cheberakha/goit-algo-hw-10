import timeit
from collections.abc import Callable

from coins_greedy_algorithm import find_coins_greedy
from coins_dynamic_programming import find_min_coins


def benchmark(func: Callable, amount: int) -> float:
    """
    Return the best average execution time for one call.
    """
    timings = timeit.repeat(lambda: func(amount), number=10, repeat=5)
    return min(timings) / 10


def main() -> None:
    amount = 113
    print(f"Amount: {amount}")
    print()

    # Print the coins and their total count for each algorithm.
    greedy_algorithm_result = find_coins_greedy(amount)
    print(f"Greedy algorithm: {greedy_algorithm_result}")
    print(f"Total coins: {sum(greedy_algorithm_result.values())}")
    print()

    dynamic_programming_result = find_min_coins(amount)
    print(f"Dynamic programming algorithm: {dynamic_programming_result}")
    print(f"Total coins: {sum(dynamic_programming_result.values())}")
    print()

    # Compare execution time for small and large amounts.
    print(f"| {'Amount': <10} | {'Algorithm': <29} | {'Seconds': <11} |")
    print(f":{'-'*11} | :{'-'*28} | :{'-'*11}")
    for amount in (113, 1000, 10000, 100000):
        greedy_algorithm_seconds = benchmark(find_coins_greedy, amount)
        print(f"| {amount: <10} | {'Greedy algorithm': <30}| {greedy_algorithm_seconds:.9f} |")

        dynamic_programming_seconds = benchmark(find_min_coins, amount)
        print(f"| {amount: <10} | {'Dynamic programming algorithm': <29} | {dynamic_programming_seconds:.9f} |")


if __name__ == "__main__":
    main()
