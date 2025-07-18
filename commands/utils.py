def validate_amount(input_str):
    """
    Validates that the input string can be converted to a float.
    
    Args:
        input_str (str): The input string from user.

    Returns:
        float: The converted float amount.

    Raises:
        ValueError: If input is not a valid number.
    """
    try:
        return float(input_str)
    except ValueError:
        raise ValueError("Amount must be a number")
