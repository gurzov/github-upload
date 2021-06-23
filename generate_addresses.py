
bcolors = {
    "HEADER" : '\033[95m',
    "OKBLUE" : '\033[94m',
    "OKGREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m',
}

def _(text, color):
    return f"{bcolors[color]}{text}{bcolors['ENDC']}"

from typing import NamedTuple, List, Union

class Range(NamedTuple):
    min : Union[int, str]
    max : Union[int, str]


import re

default_params = {
    "retailer_value": "10",
    "store_value": "01",
    "zone_range": "D",
    "aisle_range": "1-1",
    "bay_range": "1-1",
    "shelf_range": "01-1",
    "position_range": "A-T",
}


def collect_params():
    params = {}
    params["R"] = input("Retailer code (leave empty to set default value `{}`) :".format(default_params["retailer_value"]))
    if not params["R"]:  params["R"] = default_params["retailer_value"]
    params["R"] = int(params["R"])
    print("Reatailer code = ", params["R"])

    params["D"] = input("Store ID (leave empty to set default value `{}`) :".format(default_params["store_value"]))
    if not params["D"]:  params["D"] = default_params["store_value"]
    params["D"] = int(params["D"])
    print("Store ID = ", params["D"])

    params["Z"] = input("Area (leave empty to set default value `{}`) format=``:".format(default_params["zone_range"]))
    if not params["Z"]:  params["Z"] = default_params["zone_range"]
    print("Area code = ", params["Z"])

    params["A"] = input("Aisle (leave empty to set default value `{}`) format=`01-99`:".format(default_params["aisle_range"]))
    if not params["A"]:  params["A"] = default_params["aisle_range"]
    params["A"] = Range(*map(int,re.findall("(\d+)-(\d+)", params["A"])[0]))
    print("Aisle range = from {} to {}".format(params["A"].min, params["A"].max))

    params["B"] = input("Bay (leave empty to set default value `{}`) format=`001-999`:".format(default_params["bay_range"]))
    if not params["B"]:  params["B"] = default_params["bay_range"]
    params["B"] = Range(*map(int,re.findall("(\d+)-(\d+)", params["B"])[0]))
    print("Bay range = from {} to {}".format(params["B"].min, params["B"].max))

    params["S"] = input("Aisle (leave empty to set default value `{}`) format=`01-99`:".format(default_params["shelf_range"]))
    if not params["S"]:  params["S"] = default_params["shelf_range"]
    params["S"] = Range(*map(int,re.findall("(\d+)-(\d+)", params["S"])[0]))
    print("Shelf range = from {} to {}".format(params["S"].min, params["S"].max))

    params["P"] = input("Aisle (leave empty to set default value `{}`) format=`A-T`:".format(default_params["position_range"]))
    if not params["P"]:  params["P"] = default_params["position_range"]
    params["P"] = Range(*map(lambda x:x.upper(),re.findall("(\w)-(\w)", params["P"])[0]))
    print("Position range = from {} to {}".format(params["P"].min, params["P"].max))

    return params

from pprint import pprint

def main():
    params = collect_params()
    R = params["R"]
    D = params["D"]
    Z = params["Z"]
    import string
    alphbt = string.ascii_uppercase
    filename = "tom_addresses_zone_" + Z + ".csv"
    with open(filename, "w") as target_file:
        for A in range(params["A"].min, params["A"].max + 1):
            for B in range(params["B"].min, params["B"].max + 1):
                for S in range(params["S"].min, params["S"].max + 1):
                    for P in alphbt[alphbt.find(params["P"].min):alphbt.find(params["P"].max) + 1]:
                        R, D, A, S = map(lambda x:str(x).rjust(2,"0"),(R, D, A, S))
                        B = str(B).rjust(3, "0")
                        out = f"{R},{D},{Z},{A},{B},{S},{P}"
                        target_file.write(out + "\n")
        print("Successfully created file `{}`".format(filename))

if __name__ == "__main__":
    main()