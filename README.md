# TID2025-2

Proyecto de Electropermeabilización Celular usando Formulación MTF (Multiple Traces Formulation)

## Estructura del Repositorio

```
TID2025-2-repo/
├── parte1/          # Primera parte del proyecto
└── parte2/          # Segunda parte del proyecto (implementación completa)
    ├── biosspheres/                        # Módulos locales organizados
    ├── e2.mtf_time_coupled_Kavian.ipynb   # Notebook principal
    ├── verify_setup.py                     # Script de verificación
    ├── README.md                           # Documentación completa
    ├── GUIA_RAPIDA.md                      # Guía de inicio rápido
    └── PROYECTO_COMPLETADO.md              # Resumen del proyecto
```

## Inicio Rápido

### Parte 2: Implementación Completa

```bash
cd parte2
pip install numpy scipy matplotlib pyshtools jupyter
python verify_setup.py
jupyter notebook e2.mtf_time_coupled_Kavian.ipynb
```

## Descripción

Este proyecto implementa simulaciones de electropermeabilización celular basadas en el modelo de Kavian et al. utilizando la formulación de trazas múltiples (MTF) con acoplamiento temporal.

### Características Principales

- Autocontenido: Todos los módulos necesarios incluidos
- Documentación completa en español
- Script de verificación automática
- Tres tipos de excitación: constante, fuente puntual, lineal-z
- Visualización 2D y 3D de resultados
- Análisis SVD opcional

## Referencias

**Modelo y Formulación:**
> Cell Electropermeabilization Modeling via Multiple Traces Formulation and Time Semi-Implicit Coupling
> arXiv:2403.19371
> https://arxiv.org/abs/2403.19371

**Modelo de Corrientes:**
> Kavian, O., Leguèbe, M., Poignard, C., & Weynans, L. (2014).
> "Classical electropermeabilization modeling at the cell scale"
> Journal of Mathematical Biology, 68(1-2), 235-265.

##  Autores
Isidora Gajardo Weason
Claudio Díaz Consuegra
Proyecto TID2025-2

