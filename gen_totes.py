# IMPORTANT!!
# use only as `gen_totes.py <target/storage> <starting num> <how many>`

import  sys

_, tote_type, start, count = sys.argv

def modulo10(barcode: str):
    return (10 - (sum(int(digit) if i % 2 else int(digit) * 3 for i, digit in enumerate(barcode)) % 10))%10

def provide_target_tote(tote_body):
    return f"{tote_body}{modulo10(str(tote_body))}"
    # return str(tote_body) + str(modulo10(str(tote_body)))


def provide_storage_tote(tote_body):
    return f'{tote_body}0{modulo10(str(tote_body) + "0")}'

gen_method = {"target": provide_target_tote,
              "storage": provide_storage_tote}.get(tote_type)


start = int(start)
count = int(count)
with open(tote_type + ".csv", "w") as out:
    for tote in range(start, start+count):
        #out.write(gen_method(tote) + "\n")
        out.write(gen_method(tote) + "\n")
    print("Success.")
