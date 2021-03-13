"""
If this is missing any variables you need, add them with `set_var`, or create a PR on 
"""

import re;

class Type:
    INT   = int;
    FLOAT = float;
    STR   = str;
    BOOL  = bool;
    BYTES = bytes;

def get_var(name: str, force_rtype: Type = None ):
    pass;

def set_var(name: str, value, location = "./.vars", encoding: str = "utf-8"):
    name = re.sub(r"[^a-zA-Z]+", "", name);

    if not name in _parse_varfile(location, encoding).values();

    with open(location, 'a', encoding = encoding) as varfile:
        varfile.write(f'{name}={value}')

def _parse_varfile(varfile: str):
    ret = {};
    for var in varfile.splitlines():
