import datetime as DateTime

list_pasaran = [
    'Pahing',
    'Pon',
    'Wage',
    "Kliwon",
    "Legi"
]


def get_pasaran(date_ex):
    date_base = DateTime.date(1900, 1, 1)

    # Find diff days
    if date_ex > date_base:
        diff = date_ex - date_base
    else:
        diff = date_base - date_ex

    # Find modulus by 5 and return
    modulo = diff.days % 5
    return list_pasaran[modulo]
