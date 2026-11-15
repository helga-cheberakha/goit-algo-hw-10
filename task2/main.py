import random
from scipy.integrate import quad

def f(x):
    """
    Gets the square of x.
    """
    return x ** 2

def monte_carlo_integral(a: float, b: float, samples: int = 100000, seed: int | None = None) -> float:
    """
    Estimate the area under x squared by counting random points.
    """
    if a >= b:
        raise ValueError("The lower bound must be less than the upper bound.")

    # Find the rectangle height using the maximum of x squared
    # on [a, b].
    height = max(f(a), f(b))
    rectangle_area = (b - a) * height

    points_amount = 150000
    rng = random.Random(seed)
    print(f"Загальна кількість точок: {points_amount}")

    # Generate points in the rectangle and
    # get amount of them under the curve.
    inside_count = 0
    for _ in range(points_amount):
        x = rng.uniform(a, b)
        y = rng.uniform(0, height)

        if y <= f(x):
            inside_count += 1

    print(f"Кількість точок під графіком: {inside_count}")

    return (inside_count / points_amount) * rectangle_area

def main() -> None:
    """Compare the result of Monte Carlo method with quad."""
    a, b = 0, 2

    monte_carlo_result = monte_carlo_integral(a, b, seed=42)
    quad_result, quad_error = quad(f, a, b)

    absolute_difference = abs(monte_carlo_result - quad_result)
    relative_difference = absolute_difference / abs(quad_result) * 100

    print(f"Інтеграл за методом Монте-Карло: {monte_carlo_result:.10f}")
    print(f"Інтеграл за допомогою quad: {quad_result:.10f}")
    print(f"Оцінка абсолютної похибки quad: {quad_error}")
    print(f"Абсолютне відхилення від quad: {absolute_difference:.10f}")
    print(f"Відносне відхилення від quad: {relative_difference:.6f}%")


if __name__ == "__main__":
    main()
