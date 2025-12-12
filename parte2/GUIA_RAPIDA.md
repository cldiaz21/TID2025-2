# 🚀 Guía Rápida de Inicio - TID2025-2

## ⚡ En 5 Minutos

### 1. Instalar (1 min)
```bash
pip install numpy scipy matplotlib pyshtools jupyter
```

### 2. Verificar (30 seg)
```bash
python verify_setup.py
```
Espera ver: `✓✓✓ TODO CORRECTO ✓✓✓`

### 3. Abrir Notebook (30 seg)
```bash
jupyter notebook e2.mtf_time_coupled_Kavian.ipynb
```

### 4. Ejecutar en Orden (3 min)

| Paso | Celdas | Qué hace | Tiempo |
|------|--------|----------|--------|
| 1 | **3** | Setup inicial | 1 seg |
| 2 | **11-27** | Configurar parámetros | 5 seg |
| 3 | **31** | Definir excitaciones | 10 seg |
| 4 | **39-50** | Configurar corrientes | 5 seg |
| 5 | **55** | ⭐ **SIMULAR** | 2-5 min |
| 6 | **68, 72** | Ver resultados | 10 seg |

## 🎯 Parámetros Importantes

### Para Comenzar (Usa estos valores por defecto)

```python
# Celda 11: Geometría
radius = 10.0

# Celda 13: Conductividades
sigma_e = 15.0
sigma_i = 1.5

# Celda 18: Resolución espacial
big_l = 17  # ⚠️ Si es lento, usa 10

# Celda 22: Resolución temporal
number_steps = 2**13  # ⚠️ Si es lento, usa 2**10

# Celda 31: Tipo de excitación
phi_choice = "linear_z"  # ✅ Recomendado
```

## 🔄 Flujo Básico

```
┌─────────────────────────────────────────────────┐
│  1. Instalar dependencias                       │
│     pip install numpy scipy matplotlib ...      │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  2. Verificar setup                             │
│     python verify_setup.py                      │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  3. Abrir notebook en Jupyter                   │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  4. Ejecutar celdas 3, 11-27                    │
│     (Configuración de parámetros)               │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  5. Ejecutar celda 31                           │
│     (Seleccionar excitación φₑ)                 │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  6. Ejecutar celdas 39-50                       │
│     (Configurar corrientes Kavian)              │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  7. Ejecutar celda 55                           │
│     ⭐ SIMULACIÓN (tarda 2-5 min)                │
└─────────────────┬───────────────────────────────┘
                  │
┌─────────────────▼───────────────────────────────┐
│  8. Ver resultados (celdas 68, 72, 75)          │
└─────────────────────────────────────────────────┘
```

## 📊 Qué Esperar

### Después de Celda 31
```
Módulos locales importados correctamente
Configurando excitaciones para: radius=1.0, cte=5.0

1. Creando phi_cte (constante en espacio y tiempo)...
2. Creando phi_point (fuente puntual)...
3. Creando phi_linear_z (lineal en z, recomendado para Kavian)...

✓ Usando excitación: 'linear_z'

Configuración de excitación completada.
```

### Después de Celda 55 (Simulación)
```
[La simulación correrá... espera 2-5 minutos]
```

Luego tendrás disponible:
- Variable `solutions`: Array con todas las soluciones
- Dimensión: `(number_steps+1, 6*num)` ej. `(8193, 1944)`

### Después de Celdas de Visualización

**Celda 68:** Gráfico de evolución temporal
**Celda 72:** Superficie 3D del potencial
**Celda 75:** Corte plano en x=0

## 🎨 Modificaciones Comunes

### Cambiar Tipo de Excitación

En **Celda 31**, modifica:
```python
phi_choice = "point"  # En lugar de "linear_z"
```

Luego ejecuta nuevamente celdas 55+ (no necesitas reejecutar 3-27).

### Simulación Más Rápida (para pruebas)

En **Celda 18 y 22**:
```python
big_l = 10           # En lugar de 17
number_steps = 2**10 # En lugar de 2**13
```

⚠️ Menor precisión, pero **10x más rápido**.

### Simulación Más Precisa

En **Celda 18 y 22**:
```python
big_l = 20
number_steps = 2**14
```

⚠️ Mayor precisión, pero **mucho más lento** (puede tardar horas).

## 🆘 Problemas Frecuentes

### ❌ `ModuleNotFoundError: No module named 'scipy'`
**Solución:**
```bash
pip install scipy
```

### ❌ `NameError: name 'big_l' is not defined`
**Causa:** Saltaste celdas
**Solución:** Ejecuta celdas 11-27 primero

### ❌ `NameError: name 'sigmas' is not defined`
**Causa:** No ejecutaste celda 13
**Solución:** Ejecuta celda 13 que define conductividades

### ⚠️ Notebook muy lento
**Solución:** Reduce resolución
```python
big_l = 10
number_steps = 2**10
```

### ⚠️ Kernel muerto / Out of Memory
**Causa:** Demasiada memoria usada
**Solución:**
1. Restart kernel
2. Reduce `big_l` y `number_steps`
3. Cierra otros programas

## 📁 Archivos Importantes

| Archivo | Descripción | ¿Modificar? |
|---------|-------------|-------------|
| `e2.mtf_time_coupled_Kavian.ipynb` | Notebook principal | ✅ Sí (parámetros en celdas) |
| `verify_setup.py` | Verificación | ❌ No |
| `README.md` | Documentación completa | 📖 Leer |
| `GUIA_RAPIDA.md` | Esta guía | 📖 Leer |
| `biosspheres/` | Módulos locales | ⚠️ Solo si sabes qué haces |

## ✅ Checklist Primera Ejecución

```
[ ] 1. Python instalado (versión 3.7+)
[ ] 2. Dependencias instaladas (numpy, scipy, matplotlib, pyshtools, jupyter)
[ ] 3. verify_setup.py ejecutado y muestra "TODO CORRECTO"
[ ] 4. Notebook abierto en Jupyter
[ ] 5. Celdas ejecutadas en orden: 3 → 11-27 → 31 → 39-50 → 55
[ ] 6. Simulación completada (variable solutions existe)
[ ] 7. Gráficos visualizados (celdas 68, 72, 75)
```

## 🎓 Próximos Pasos

Una vez que hayas ejecutado la simulación básica:

1. **Experimenta con parámetros** (celdas 11-27, 39)
2. **Prueba diferentes excitaciones** (celda 31)
3. **Modifica visualizaciones** (celdas 68+)
4. **Guarda tus resultados**: `np.save("mis_resultados.npy", solutions)`
5. **Lee el README.md completo** para opciones avanzadas

## 💡 Tip Final

**Primera vez:** Ejecuta TODO con valores por defecto para verificar que funciona.

**Segunda vez:** Experimenta cambiando UN parámetro a la vez.

**Tercera vez:** Combina modificaciones y guarda resultados.

---

¿Dudas? Revisa el [README.md](README.md) completo o ejecuta `python verify_setup.py` para diagnóstico.
