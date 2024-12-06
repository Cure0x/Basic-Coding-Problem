# Problem 1
# Gross pay problem

def condition (jam, gross_Pay):
    if jam <= 40:
        gross_Pay += 97000
        return gross_Pay
    elif jam > 40 and jam <= 80:
        gross_Pay += 103000
        return gross_Pay
    elif jam > 80 and jam <= 100:
        gross_Pay += 107500
        return gross_Pay
    else:
        gross_Pay = gross_Pay
        return gross_Pay

def print_Table (jam, gross_Pay, iter):
    if iter == 0:
        print("Gross Pay Table\n")
        print("No.  Jumlah Jam  Gross Pay")
    else:
        print(f"{iter}      {jam}        {gross_Pay}")

jam = 0
gross_Pay = 0
iter = 0

print_Table(jam,gross_Pay,iter)

while jam < 110:
    jam += 5
    iter += 1
    gross_Pay = condition(jam,gross_Pay)
    print_Table(jam,gross_Pay,iter)