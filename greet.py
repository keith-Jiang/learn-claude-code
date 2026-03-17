def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"


def greet_formal(name, title=""):
    """Return a formal greeting message.
    
    Args:
        name (str): The name of the person to greet
        title (str): Optional title (e.g., "Mr.", "Ms.", "Dr.")
    
    Returns:
        str: A formal greeting message
    """
    if title:
        return f"Good day, {title} {name}!"
    else:
        return f"Good day, {name}!"


def greet_casual(name):
    """Return a casual greeting message.
    
    Args:
        name (str): The name of the person to greet
    
    Returns:
        str: A casual greeting message
    """
    return f"Hey {name}! How's it going?"


def farewell(name):
    """Return a farewell message.
    
    Args:
        name (str): The name of the person to say goodbye to
    
    Returns:
        str: A farewell message
    """
    return f"Goodbye, {name}! Have a great day!"


def greet_multiple(names):
    """Greet multiple people at once.
    
    Args:
        names (list): List of names to greet
    
    Returns:
        str: A greeting message for all names
    """
    if not names:
        return "Hello everyone!"
    
    if len(names) == 1:
        return greet(names[0])
    
    name_list = ", ".join(names[:-1])
    return f"Hello {name_list}, and {names[-1]}!"


if __name__ == "__main__":
    # Test the greeting functions when run directly
    print("Testing greet module:")
    print("-" * 40)
    
    # Test basic greet function
    print("1. Basic greeting:")
    print(greet("Alice"))
    print()
    
    # Test formal greeting
    print("2. Formal greeting:")
    print(greet_formal("Smith", "Mr."))
    print(greet_formal("Johnson"))
    print()
    
    # Test casual greeting
    print("3. Casual greeting:")
    print(greet_casual("Bob"))
    print()
    
    # Test farewell
    print("4. Farewell:")
    print(farewell("Charlie"))
    print()
    
    # Test multiple greetings
    print("5. Multiple greetings:")
    print(greet_multiple([]))
    print(greet_multiple(["David"]))
    print(greet_multiple(["Emma", "Frank"]))
    print(greet_multiple(["Grace", "Henry", "Ivy"]))