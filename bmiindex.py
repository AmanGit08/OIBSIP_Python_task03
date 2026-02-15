def get_valid_input(prompt, min_val, max_val):
    """
    Helper function to ensure user input is a valid number within a specific range.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_bmi(weight, height):
    """Calculates BMI using the formula: weight(kg) / height(m)^2"""
    return weight / (height ** 2)

def get_category(bmi):
    """Classifies BMI into standard health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("--- Welcome to the Python BMI Calculator ---")
    
    # Prompting for weight in kg (reasonable range 10kg to 500kg)
    weight = get_valid_input("Enter your weight in kilograms (kg): ", 10.0, 500.0)
    
    # Prompting for height in meters (reasonable range 0.5m to 3.0m)
    height = get_valid_input("Enter your height in meters (m): ", 0.5, 3.0)
    
    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)
    
    print("\n" + "="*30)
    print(f"Your BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("="*30)

if __name__ == "__main__":
    main()