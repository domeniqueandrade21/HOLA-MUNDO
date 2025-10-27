def pedir_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (0-100): "))
            if 0 <= nota <= 100:
                return nota
            else:
                print("La nota debe estar entre 0 y 100. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingresa un número (ej. 85 o 78.5).")

def calculadora_notas():
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = pedir_nota(1)
    nota2 = pedir_nota(2)
    nota3 = pedir_nota(3)

    promedio = (nota1 + nota2 + nota3) / 3
    print(f"\nEstudiante: {nombre}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Promedio: {promedio:.2f}")  # .2f muestra 2 decimales

if __name__ == "__main__":
    calculadora_notas()
    