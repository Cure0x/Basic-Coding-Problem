# Problem 1
# Gross pay problem

jam = 0
gross_Pay = 0

while jam <= 110:
    jam += 5
    if jam <= 40:
        gross_Pay += 97000
    elif jam > 40 and jam <= 80:
        gross_Pay += 103000
    elif jam > 80 and jam <= 100:
        gross_Pay += 107500
    else:
        gross_Pay = gross_Pay
    print (f"Grosspay {jam} Jam = {gross_Pay}")