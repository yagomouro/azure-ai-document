def mask_card_number(number):
    if not number:
        return None
    n = len(number)
    if n <= 4:
        return number
    return "*"*(n-4)+number[-4:]

def format_date_display(exp):
    if not exp:
        return None
    parts = exp.split("/")
    if len(parts) != 2:
        return exp
    mm, yy = parts[0], parts[1][-2:]
    return f"{mm}/{yy}"
