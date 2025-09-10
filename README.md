# Laboratorio 2: Continuous Integration

**Universidad del Valle de Guatemala**  
**Facultad de Ingeniería**  
**Departamento de Ciencias de la Computación**  
**Administración y Mantenimiento de Sistemas**

## Autor
- Diego Leiva - 21752  

## mathlib-py

Librería de **matemática básica** implementada en Python como práctica de *GIT, Pruebas Unitarias y CI con GitHub Actions*.

### Funciones incluidas

- `square(n)` → retorna el cuadrado de un número (`int` o `float`).
- `factorial(n)` → retorna el factorial de un número entero no negativo.
- `is_prime(n)` → determina si un número entero es primo.
- `gcd(a, b)` → calcula el máximo común divisor entre dos enteros.
- `lcm(a, b)` → calcula el mínimo común múltiplo entre dos enteros.

### Instalación local

Clonar el repositorio y crear un entorno virtual:

```bash
git clone https://github.com/<tu-usuario>/mathlib-py.git
cd mathlib-py

# Crear y activar entorno virtual (Linux/Mac)
python -m venv .venv
source .venv/bin/activate

# En Windows
python -m venv .venv
.venv\Scripts\activate
```

Instalar el paquete en modo editable con dependencias de desarrollo:

```bash
pip install --upgrade pip setuptools wheel
pip install -e ".[dev]"
```

### Uso de la librería

Ejemplo en consola de Python:

```python
import mathlib

print(mathlib.square(5))      # 25
print(mathlib.factorial(5))   # 120
print(mathlib.is_prime(17))   # True
print(mathlib.gcd(24, 18))    # 6
print(mathlib.lcm(4, 6))      # 12
```