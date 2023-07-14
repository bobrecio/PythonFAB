#Dictionary .setdefault()

computers = {"Google":"Chromebook",
            "Apple":"Macbook",
            "Microsoft":"Surface"
}

def print_computers():
    for item in computers.items():
        print(item)
    print("\n")


print_computers()

#if not exists, it will add
computers.setdefault("Dell","Inspiron")
print_computers()

#if it exists it will not overwrite
computers.setdefault("Dell","XPS")
print_computers()


empty = dict()
print(empty)

with_values = dict(a=1, b=2, c=3)
print(with_values)