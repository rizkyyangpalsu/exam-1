import datetime

list_month = [
    {
        "key": "Jan",
        "value": "Januari"
    }, {
        "key": "Feb",
        "value": "Februari"
    }, {
        "key": "Mar",
        "value": "Maret"
    }, {
        "key": "Apr",
        "value": "April"
    }, {
        "key": "May",
        "value": "Mei"
    }, {
        "key": "Jun",
        "value": "Juni"
    }, {
        "key": "Jul",
        "value": "Juli"
    }, {
        "key": "Aug",
        "value": "Agustus"
    }, {
        "key": "Sep",
        "value": "September"
    }, {
        "key": "Oct",
        "value": "Oktober"
    }, {
        "key": "Nov",
        "value": "November"
    }, {
        "key": "Dec",
        "value": "Desember"
    }
]
list_day = [
    {
        "key": "Sun",
        "value": "Minggu"
    }, {
        "key": "Mon",
        "value": "Senin"
    }, {
        "key": "Tue",
        "value": "Selasa"
    }, {
        "key": "Wed",
        "value": "Rabu"
    }, {
        "key": "Thu",
        "value": "Kamis"
    }, {
        "key": "Fri",
        "value": "Jumat"
    }, {
        "key": "Sat",
        "value": "Sabtu"
    }
]


def get_day_name_id(day):
    name_day = None

    for x in list_day:
        if day == x.get("key"):
            name_day = x.get("value")
            break
    else:
        name_day = "Kiamat"

    return name_day


def get_month_name_id(month: str) -> str:
    name_month = None

    for x in list_month:
        if month == x.get("key"):
            name_month = x.get("value")
            break
    else:
        name_month = "Kiamat"

    return name_month


def get_age(birthdate):
    today = datetime.datetime.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
