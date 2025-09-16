import re

_re_email = ["^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"]
_re_tel   = ["^\d{7,15}$"]
_re_dni   = ["^\d{7,8}$"]
_re_fecha = ["^\d{4}-\d{2}-\d{2}$"]
_re_hora  = ["^(?:[01]\d|2[0-3]):[0-5]\d$"]

def es_email(s):  return bool(re.match(_re_email[0], s))
def es_tel(s):    return bool(re.match(_re_tel[0], s))
def es_dni(s):    return bool(re.match(_re_dni[0], s))
def es_fecha(s):  return bool(re.match(_re_fecha[0], s))
def es_hora(s):   return bool(re.match(_re_hora[0], s))
