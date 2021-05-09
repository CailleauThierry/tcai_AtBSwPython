# AUTOGENERATED! DO NOT EDIT! File to edit: 10_Python_Regular_Expresssions.ipynb (unless otherwise specified).

__all__ = ['isPhoneNumber']

# Cell
def isPhoneNumber(text):
    if len(text) != 12:
        return False # not phone number size
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no are code
    if text[3] != '-':
        return False # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no second position 3 digits
    if text[7] != '-':
        return False # missing dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # no third position 4 digits
    return True

print(isPhoneNumber('415-555-1234'))


