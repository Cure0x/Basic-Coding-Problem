import numpy as np

def degree_Converter (sudut):
    rad = (np.pi/180)*sudut
    return rad

def deret_Mclaurin(iter,x):
    cos = (-1**iter) * (x**(2*iter))/np.math.factorial(2*iter)
    return cos

def error_Value(aprox_Value, true_Value):
    error = ((aprox_Value-true_Value)/true_Value) * 100
    return error

sudut = input(f"\nBesar sudut (derajat) = ")

sudut_Rad = degree_Converter(sudut)

true_Value = np.cos(sudut_Rad)

aprox_Value = deret_Mclaurin(i,sudut_Rad)
error_Value = error_Value(true_Value, aprox_Value)