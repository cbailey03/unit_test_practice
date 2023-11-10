"""Contains functions to format a persons name."""
def get_formatted_name(first, last, middle=''):
    """Takes a first and last name, and formats
    the name to be proper
    
    Args:
        first: String, users first name
        middle: String, users middle name
        last: String, users last name
        
    Return:
        full_name: String, concatenated first, middle, and last.
    """
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()