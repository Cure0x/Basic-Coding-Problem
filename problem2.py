import numpy as np
import math

def degree_Converter (sudut):
    rad = (np.pi/180)*sudut
    return rad

def deret_Mclaurin(iter,x):
    cos = ((-1)**iter) * (x**(2*iter)) / math.factorial(2*iter)
    return cos

def calculate_Error(aprox_Value, true_Value):
    error = ((aprox_Value-true_Value)/true_Value) * 100
    error = abs(round(error,3))
    return error

sudut = int(input(f"\nBesar sudut (derajat) = "))

sudut_Rad = degree_Converter(sudut)
true_Value = np.cos(sudut_Rad)

iter = 0
aprox_Value = deret_Mclaurin(iter,sudut_Rad)
error_Value = calculate_Error(true_Value, aprox_Value)

print(f"true Value cos ({sudut} derajat) = {true_Value}")

print (f"\n Jumlah Suku        AV Cosinus      ER Cosinus")
print(f"{iter}                 {aprox_Value:.6f}          {error_Value:.3f} %")

while error_Value >= 1:
    iter += 1
    aprox_Value += deret_Mclaurin(iter,sudut_Rad)
    error_Value = calculate_Error(true_Value, aprox_Value)
    print(f"{iter}                 {aprox_Value:.6f}          {error_Value:.3f} %")