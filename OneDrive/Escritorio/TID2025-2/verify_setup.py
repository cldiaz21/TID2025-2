"""
Script de verificación completo para el proyecto TID2025-2
Verifica que todos los módulos y estructura de carpetas están correctos
"""

import sys
import os
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Agregar directorio actual al path
current_dir = Path(__file__).parent.absolute()
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

print("="*70)
print("VERIFICACIÓN DEL PROYECTO TID2025-2")
print("="*70)

# 1. Verificar estructura de carpetas
print("\n[1] Verificando estructura de carpetas...")
required_dirs = [
    "biosspheres",
    "biosspheres/utils",
    "biosspheres/utils/validation",
    "biosspheres/quadratures",
    "biosspheres/formulations",
    "biosspheres/formulations/mtf",
    "biosspheres/formulations/mtf/timecouplings",
    "biosspheres/miscella",
    "biosspheres/miscella/forcouplings",
    "biosspheres/laplace",
    "biosspheres/helmholtz",
]

all_dirs_ok = True
for dir_path in required_dirs:
    full_path = current_dir / dir_path
    if full_path.exists():
        print(f"  [OK] {dir_path}")
    else:
        print(f"  [ERROR] {dir_path} NO ENCONTRADO")
        all_dirs_ok = False

if all_dirs_ok:
    print("\n  ✓ Estructura de carpetas correcta")
else:
    print("\n  ✗ Faltan algunas carpetas")
    sys.exit(1)

# 2. Verificar archivos clave
print("\n[2] Verificando archivos clave...")
required_files = [
    "biosspheres/utils/auxindexes.py",
    "biosspheres/utils/validation/inputs.py",
    "biosspheres/quadratures/sphere.py",
    "biosspheres/formulations/mtf/mtf.py",
    "biosspheres/formulations/mtf/righthands.py",
    "biosspheres/formulations/mtf/timecouplings/solvertemplates.py",
    "biosspheres/formulations/mtf/timecouplings/righthands.py",
    "biosspheres/formulations/mtf/timecouplings/linearoperators.py",
    "biosspheres/formulations/massmatrices.py",
    "biosspheres/miscella/forcouplings/currents.py",
    "biosspheres/miscella/forcouplings/oderesolutions.py",
    "biosspheres/laplace/drawing.py",
    "e2.mtf_time_coupled_Kavian.ipynb",
]

all_files_ok = True
for file_path in required_files:
    full_path = current_dir / file_path
    if full_path.exists():
        print(f"  [OK] {file_path}")
    else:
        print(f"  [ERROR] {file_path} NO ENCONTRADO")
        all_files_ok = False

if all_files_ok:
    print("\n  ✓ Todos los archivos necesarios están presentes")
else:
    print("\n  ✗ Faltan algunos archivos")
    sys.exit(1)

# 3. Verificar importaciones
print("\n[3] Verificando importaciones de módulos...")

import_tests = [
    ("import numpy as np", "NumPy"),
    ("import matplotlib.pyplot as plt", "Matplotlib"),
    ("import scipy", "SciPy"),
    ("import pyshtools", "pyshtools"),
    ("import biosspheres.utils.auxindexes", "biosspheres.utils.auxindexes"),
    ("import biosspheres.utils.validation.inputs", "biosspheres.utils.validation.inputs"),
    ("import biosspheres.quadratures.sphere", "biosspheres.quadratures.sphere"),
    ("import biosspheres.formulations.mtf.mtf", "biosspheres.formulations.mtf.mtf"),
    ("import biosspheres.formulations.mtf.righthands", "biosspheres.formulations.mtf.righthands"),
    ("import biosspheres.formulations.mtf.timecouplings.solvertemplates", "biosspheres.formulations.mtf.timecouplings.solvertemplates"),
    ("import biosspheres.formulations.mtf.timecouplings.righthands", "biosspheres.formulations.mtf.timecouplings.righthands"),
    ("import biosspheres.formulations.massmatrices", "biosspheres.formulations.massmatrices"),
    ("import biosspheres.miscella.forcouplings.currents", "biosspheres.miscella.forcouplings.currents"),
    ("import biosspheres.miscella.forcouplings.oderesolutions", "biosspheres.miscella.forcouplings.oderesolutions"),
    ("import biosspheres.laplace.drawing", "biosspheres.laplace.drawing"),
]

all_imports_ok = True
for import_stmt, module_name in import_tests:
    try:
        exec(import_stmt)
        print(f"  [OK] {module_name}")
    except ImportError as e:
        print(f"  [ERROR] {module_name}: {e}")
        all_imports_ok = False
    except Exception as e:
        print(f"  [WARN] {module_name}: {e}")

if all_imports_ok:
    print("\n  ✓ Todas las importaciones funcionan")
else:
    print("\n  ✗ Algunas importaciones fallaron")
    print("\n  NOTA: Si faltan paquetes externos (numpy, scipy, pyshtools), instálalos con:")
    print("        pip install numpy scipy matplotlib pyshtools")

# 4. Test funcional básico
print("\n[4] Test funcional de módulos clave...")

try:
    import numpy as np
    import biosspheres.formulations.mtf.timecouplings.righthands as tcrighthands

    # Test básico
    space_b = np.array([1.0, 2.0, 3.0])

    def simple_time_function(t):
        return 2.0

    phi_func = tcrighthands.phi_part_of_b_separable_in_space_time(
        space_b, simple_time_function
    )
    result = phi_func(1.0)

    expected = space_b * 2.0
    if np.allclose(result, expected):
        print(f"  [OK] Función básica funciona correctamente")
        print(f"       Entrada: {space_b}, Tiempo: 1.0")
        print(f"       Resultado: {result}")
    else:
        print(f"  [ERROR] Resultado inesperado")
        all_imports_ok = False
except Exception as e:
    print(f"  [ERROR] Test funcional falló: {e}")
    all_imports_ok = False

# Resumen final
print("\n" + "="*70)
print("RESUMEN DE LA VERIFICACIÓN")
print("="*70)

if all_dirs_ok and all_files_ok and all_imports_ok:
    print("\n✓✓✓ TODO CORRECTO ✓✓✓")
    print("\nEl proyecto está configurado correctamente.")
    print("Puedes ejecutar el notebook: e2.mtf_time_coupled_Kavian.ipynb")
    print("\nOrden de ejecución en el notebook:")
    print("  1. Celda 3: Setup inicial e imports")
    print("  2. Celdas 11-27: Parámetros del problema")
    print("  3. Celda 31: Configuración de excitaciones (φₑ)")
    print("  4. Celdas 39-50: Parámetros de corrientes y ODEs")
    print("  5. Celda 53-55: Configuración de threads y resolución")
    print("  6. Celdas 68+: Visualización de resultados")
else:
    print("\n✗✗✗ HAY PROBLEMAS ✗✗✗")
    print("\nRevisa los errores anteriores y corrígelos antes de continuar.")

print("\n" + "="*70)
