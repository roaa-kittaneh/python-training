def bmi_calculator(height: float, weight: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    height: meters
    weight: kilograms
    """

    # Reject bool explicitly
    if isinstance(height, bool) or isinstance(weight, bool):
        raise TypeError("Boolean values are not allowed")

    if not isinstance(height, (int, float)):
        raise TypeError("Height must be a number")

    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")

    if height <= 0:
        raise ValueError("Height must be greater than zero")

    if weight <= 0:
        raise ValueError("Weight must be greater than zero")

    bmi = weight / (height**2)
    return round(bmi, 2)
