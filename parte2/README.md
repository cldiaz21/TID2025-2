# Proyecto de Electropermeabilización - TID2025-2

Este proyecto contiene una implementación completa y autocontenida para ejecutar simulaciones de electropermeabilización celular usando la formulación MTF (Multiple Traces Formulation) con acoplamiento temporal.

## 📁 Estructura del Proyecto

```
TID2025-2/
├── e2.mtf_time_coupled_Kavian.ipynb    # Notebook principal
├── verify_setup.py                      # Script de verificación
├── README.md                            # Esta guía
└── biosspheres/                         # Módulos locales (TODO EN ESTA CARPETA)
    ├── utils/
    │   ├── auxindexes.py               # Índices auxiliares
    │   └── validation/
    │       └── inputs.py               # Validación de entradas
    ├── quadratures/
    │   └── sphere.py                   # Cuadraturas esféricas
    ├── formulations/
    │   ├── massmatrices.py             # Matrices de masa
    │   └── mtf/
    │       ├── mtf.py                  # Formulación MTF
    │       ├── righthands.py           # Lados derechos MTF
    │       └── timecouplings/
    │           ├── solvertemplates.py  # Solvers temporales
    │           ├── righthands.py       # Lados derechos acoplados
    │           └── linearoperators.py  # Operadores lineales
    ├── miscella/
    │   └── forcouplings/
    │       ├── currents.py             # Corrientes acopladas
    │       └── oderesolutions.py       # Resolución de ODEs
    ├── laplace/
    │   └── drawing.py                  # Visualización
    └── helmholtz/
        └── selfinteractions.py         # Autointeracciones
```

## 🚀 Inicio Rápido (3 Pasos)

### Paso 1: Instalar Dependencias

```bash
pip install numpy scipy matplotlib pyshtools jupyter
```

### Paso 2: Verificar Instalación

```bash
python verify_setup.py
```

Deberías ver: `✓✓✓ TODO CORRECTO ✓✓✓`

### Paso 3: Ejecutar el Notebook

```bash
jupyter notebook e2.mtf_time_coupled_Kavian.ipynb
```

Luego ejecuta las celdas en este orden:
1. Celdas **3-27**: Parámetros
2. Celda **31**: Excitaciones
3. Celdas **39-50**: Corrientes
4. Celda **55**: ⭐ **Simular**
5. Celdas **68+**: Visualizar

## 📓 Guía de Uso del Notebook

### Configuración Básica (Celdas 11-27)

Los parámetros más importantes son:

```python
# Geometría (Celda 11)
radius = 10.0  # Radio de la esfera [μm]

# Conductividades (Celda 13)
sigma_e = 15.0  # Extracelular [μS/μm]
sigma_i = 1.5   # Intracelular [μS/μm]

# Discretización (Celdas 18, 20)
big_l = 17      # Grado máximo de armónicos esféricos
big_l_c = 60    # Grado para cuadraturas

# Tiempo (Celda 22)
final_time = 10.0
number_steps = 2**13  # 8192 pasos
```

### Seleccionar Excitación (Celda 31)

Cambia la variable `phi_choice`:

```python
phi_choice = "linear_z"  # Opciones: "cte", "point", "linear_z"
```

- **"linear_z"**: ⭐ Recomendado para modelo de Kavian
- **"cte"**: Constante (para pruebas)
- **"point"**: Fuente puntual

### Ejecutar Simulación (Celda 55)

Esta es la celda principal que resuelve el problema:

```python
solutions = solve.mtf_time_coupling_one_sphere(...)
```

**Nota:** La simulación puede tardar varios minutos dependiendo de `number_steps` y `big_l`.

## 🎯 Resultados

La variable `solutions` tiene dimensión `(number_steps+1, 6*num)` donde `num = (big_l+1)²`.

Contiene (por columnas):
- Columnas `0:num`: Traza Dirichlet exterior
- Columnas `num:2*num`: Traza Neumann exterior
- Columnas `2*num:3*num`: Traza Dirichlet interior
- Columnas `3*num:4*num`: Traza Neumann interior
- Columnas `4*num:5*num`: **Potencial transmembrana (v)**
- Columnas `5*num:6*num`: Variable de recuperación (z)

### Guardar Resultados

```python
np.save("mi_simulacion.npy", solutions)
```

## ⚙️ Personalización

### Modificar Parámetros de Kavian (Celda 39)

```python
s_l = 1.9*10**(-6)   # Conductancia de fuga
s_ir = 2.5*10**2     # Conductancia irreversible
tau_ep = 1.0         # Tiempo de electroporación [μs]
tau_res = 10.**3     # Tiempo de restitución [μs]
k_ep = 40.0          # Pendiente [V⁻¹]
v_rev = 1.5          # Potencial de reversión [V]
```

### Crear Excitación Personalizada (Celda 31)

```python
use_custom = True

def mi_funcion_tiempo(t):
    return 1.0 if 2.0 <= t <= 7.0 else 0.0

custom_phi = tcrighthands.phi_part_of_b_separable_in_space_time(
    space_phi_linear_z, mi_funcion_tiempo
)
```

## 🔧 Solución de Problemas

### Error: "No module named 'scipy'"
```bash
pip install scipy numpy matplotlib pyshtools
```

### Error: Variables no definidas (NameError)
**Causa:** Celdas ejecutadas fuera de orden
**Solución:** Ejecuta desde el inicio en orden: 3→11-27→31→39-50→55

### Simulación muy lenta
**Solución:** Reduce resolución para pruebas:
```python
big_l = 10           # En lugar de 17
number_steps = 2**10 # En lugar de 2**13
```

### Error de memoria
**Solución:** Igual que arriba, reduce `big_l` y `number_steps`

## 📊 Análisis SVD (Opcional - Celda 32)

La celda 32 ejecuta múltiples simulaciones y análisis SVD:
- Compara las 3 excitaciones (cte, point, linear_z)
- Calcula descomposición en valores singulares
- Guarda resultados en `results_svd/`
- Genera gráficos de valores singulares y energía

**Nota:** Esto puede tardar mucho tiempo (ejecuta 3 simulaciones completas).

## 🛠️ Características del Proyecto

✅ **Autocontenido:** Todos los módulos necesarios están en `biosspheres/`
✅ **Sin instalación externa:** No requiere biblioteca biosspheres completa
✅ **Rutas relativas:** Todo funciona dentro de la misma carpeta
✅ **Verificación automática:** Script `verify_setup.py` para diagnóstico
✅ **Bien documentado:** Comentarios en español en el notebook

## 📚 Referencias

**Modelo y Formulación:**
> Cell Electropermeabilization Modeling via Multiple Traces Formulation and Time Semi-Implicit Coupling
> arXiv:2403.19371
> https://arxiv.org/abs/2403.19371

**Modelo de Corrientes (Kavian et al.):**
> Classical electropermeabilization modeling at the cell scale
> Journal of Mathematical Biology, 68(1-2), 235-265, 2014

## 📋 Checklist Pre-Ejecución

- [ ] Python 3.7+ instalado
- [ ] Dependencias instaladas: `pip install numpy scipy matplotlib pyshtools jupyter`
- [ ] `verify_setup.py` muestra "TODO CORRECTO"
- [ ] Notebook abierto en Jupyter

## 💡 Consejos

**Para principiantes:**
- Usa los parámetros por defecto primero
- Ejecuta las celdas en orden secuencial
- Espera a que cada celda termine antes de continuar

**Para expertos:**
- Modifica parámetros en celdas 11-27 y 39
- Crea excitaciones personalizadas en celda 31
- Usa celda 32 para análisis comparativo con SVD

**Optimización:**
- Simulación rápida: `big_l=10`, `number_steps=2**10` (~1-2 min)
- Producción: `big_l=17`, `number_steps=2**13` (~10-20 min)
- Alta precisión: `big_l=20`, `number_steps=2**14` (~1-2 horas)

---

**Proyecto:** TID2025-2
**Actualizado:** 2025-12-12
**Contacto:** [Tu información aquí]
