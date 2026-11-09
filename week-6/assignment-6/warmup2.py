def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

fahrenheit = celsius_to_fahrenheit(0)
print(f"0°C = {fahrenheit:.1f}°F")

fahrenheit = celsius_to_fahrenheit(100)
print(f"100°C = {fahrenheit:.1f}°F")


celsius = fahrenheit_to_celsius(72)
print(f"72°F = {celsius:.1f}°C")