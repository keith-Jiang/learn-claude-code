def greet(name: str) -> str:
    """
    Return a greeting message for the given name.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message in the format "Hello, {name}!"
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Example usage
    print(greet("World"))
    print(greet("Python Developer"))