"""
Credit Card Validator
This script validates credit card numbers using the Luhn algorithm
and identifies the card type.
"""

def get_card_number():
    """Prompt user for card number and clean it."""
    card_number = input("Enter your card number: ")
    # Remove dashes and spaces
    card_number = card_number.replace('-', '').replace(' ', '')
    return card_number

def is_valid_format(card_number):
    """Check if card number consists only of digits and has valid length."""
    if not card_number.isdigit():
        return False
    length = len(card_number)
    return 13 <= length <= 19

def luhn_checksum(card_number):
    """Perform Luhn algorithm validation."""
    # Reverse the card number
    reversed_digits = card_number[::-1]
    total = 0
    for i, digit in enumerate(reversed_digits):
        n = int(digit)
        if i % 2 == 1:  # Every second digit from the right
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0

def get_card_type(card_number):
    """Determine the card type based on the number."""
    length = len(card_number)
    if length == 15 and card_number.startswith(('34', '37')):
        return "American Express"
    elif length == 16 and card_number.startswith('6011'):
        return "Discover"
    elif length in [13, 16] and card_number.startswith('4'):
        return "Visa"
    elif length == 16 and 51 <= int(card_number[:2]) <= 55:
        return "MasterCard"
    else:
        return "Unknown Card Type"

def main():
    """Main function to run the card validator."""
    card_number = get_card_number()

    if not is_valid_format(card_number):
        print("Invalid card number format or length")
        return

    if luhn_checksum(card_number):
        card_type = get_card_type(card_number)
        print(f"Valid card number. Card type: {card_type}")
    else:
        print("Invalid card number")

if __name__ == "__main__":
    main()
