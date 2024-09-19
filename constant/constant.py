# user input validation regex
NAME_VALIDATION_REGEX = r"^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
PHONE_NUMBER_VALIDATION_REGEX = r"^\d{10}$"
EMAIL_VALIDATION_REGEX = r"^(\w+)\d+@(?:gmail|ymail)\.(?:com|in)$"
DOB_VALIDATION_REGEX = r"^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$"
PASSWORD_VALIDATION_REGEX = r"^(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$"
NUMBER_REGEX = r"^-?\d+(\.\d+)?$"


GENDER_CATEGORY = ["male", "female", "others"]
LOGGER_LEVEL_DEBUG = 10
INVALID_DATE_FORMATE = "Invalid date format. Please enter the date in 'YYYY-MM-DD' format."
INVALID_NAME_FORMATE = ("Invalid name format. The name contains First name and last name. "
                        "Last name must not be initial.")
INVALID_PHONE_NUMBER = "Invalid phone number format. Please enter a valid phone number."
INVALID_EMAIL = "Invalid email format. Please enter a valid email address."
INVALID_GENDER = "Invalid gender. Please enter Male, Female, or Others."
INVALID_DOB = "Invalid date of birth format. Please enter in DD/MM/YYYY format."
INVALID_PASSWORD = "Invalid password. Please ensure it's 8 characters long and contains special characters (!@#$)."
INVALID_CONFIRMATION = "Invalid input. Please enter 'yes' or 'no'."

