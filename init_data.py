name = ''
phone = 0

def phone_number(x1, x2):
    global name
    global phone
    name = x1
    phone = x2

def get_data():
    global name
    global phone
    return name, phone