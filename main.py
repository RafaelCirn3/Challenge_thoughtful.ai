def sort(width, height, length, mass):
    """
    Sort packages into stacks based on volume, dimensions, and mass.
    
    Parameters:
    - width, height, length: dimensions in cm
    - mass: mass in kg
    
    Returns:
    - str: "STANDARD", "SPECIAL", or "REJECTED"
    """
    
    # Calculate the volume of the package
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150
    
    # Determine if package is heavy
    is_heavy = mass >= 20
    
    # Determine the stack using a ternary operator
    return "REJECTED" if is_bulky and is_heavy else ("SPECIAL" if is_bulky or is_heavy else "STANDARD")


# Example test cases
if __name__ == "__main__":
    print(sort(100, 100, 100, 10))  # STANDARD
    print(sort(200, 50, 50, 10))    # SPECIAL (bulky)
    print(sort(100, 100, 100, 25))  # SPECIAL (heavy)
    print(sort(200, 200, 200, 30))  # REJECTED (both)
