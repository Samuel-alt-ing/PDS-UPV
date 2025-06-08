import sys
from src.Actividad_1 import continuous_sine, discrete_sine, continuous_exponential, discrete_exponential, continuous_triangular, discrete_triangular, continuous_square, discrete_square
from src.Actividad_2 import understanding_freq
from src.Actividad_3 import sine_both
from src.Actividad_4 import analizar_dac



def main(options):
    if options[1] == "act_1":
        continuous_sine()
        discrete_sine()
        continuous_exponential()
        discrete_exponential()
        continuous_triangular()
        discrete_triangular()
        continuous_square()
        discrete_square()
    elif options[1] == "act_2":
        if len(args) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")
    
    elif options[1] == "act_3":
        if len(options) > 4:
            amp = float(options[2])
            freq = float(options[3])
            phi = float(options[4])
            sine_both(amp, freq, phi)
        else:
            print("Por favor indica: amplitud, frecuencia y fase")
            print("Ejemplo: python main.py act_3 1 2 0.785")

    elif options[1] == "act_4":
        if len(options) > 2:
            bits = int(options[2])
            analizar_dac(bits)
        else:
            print("Por favor indica el número de bits")
            print("Ejemplo: python main.py act_4 8")

    else:
        print("Opción no válida. Usa: act_1, act_2, act_3 o act_4")




if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example ( run activity 1 ) : python main.py act_1")
        print("Example ( run activity 2 ) : python main.py act_2 1")
        print("Example ( run activity 3 ): python main.py act_3 1 2 0.785")
        print("Example ( run activity 4 ): python main.py act_4 8")