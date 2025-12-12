# Proyecto de Electropermeabilización - TID2025-2

Este proyecto contiene una implementación completa y autocontenida para ejecutar simulaciones de electropermeabilización celular usando la formulación MTF (Multiple Traces Formulation) con acoplamiento temporal.

## Estructura del Proyecto

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

##  Inicio Rápido (3 Pasos)

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

##  Referencias

**Modelo y Formulación:**
> Cell Electropermeabilization Modeling via Multiple Traces Formulation and Time Semi-Implicit Coupling
> arXiv:2403.19371
> https://arxiv.org/abs/2403.19371

**Modelo de Corrientes (Kavian et al.):**
> Classical electropermeabilization modeling at the cell scale
> Journal of Mathematical Biology, 68(1-2), 235-265, 2014


**Proyecto:** TID2025-2
**Actualizado:** 2025-12-12
