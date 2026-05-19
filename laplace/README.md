# 📱 Simulador de Propagación de Información en Redes Sociales

Aplicación educativa interactiva que simula cómo una publicación, noticia o campaña se difunde en una red social utilizando **la Transformada de Laplace** para resolver el modelo matemático.

## 🎯 Descripción del Proyecto

Este simulador está diseñado como herramienta educativa para una **exposición de matemáticas aplicadas** sobre la Transformada de Laplace. 

**NO es una calculadora de Laplace**, sino un **simulador visual** que permite:

- Modelar dinámicas de propagación de información
- Visualizar ecuaciones diferenciales en acción
- Experimentar con diferentes parámetros
- Entender aplicaciones prácticas del cálculo avanzado

## 📊 Modelo Matemático

### Ecuación Diferencial
```
dN/dt = k(Nmax - N)
```

Donde:
- **N(t)** = Número de personas alcanzadas en el tiempo t
- **N₀** = Alcance inicial
- **Nmax** = Alcance máximo posible
- **k** = Velocidad de propagación (constante)
- **t** = Tiempo

### Solución (usando Transformada de Laplace)
```
N(t) = Nmax - (Nmax - N₀) × e^(-k×t)
```

Esta solución se obtiene aplicando la **Transformada de Laplace** a la ecuación diferencial, resolviéndola en el dominio de la frecuencia, y luego aplicando la Transformada Inversa.

## ✨ Características

- ✅ **Simulación interactiva** con parámetros ajustables
- ✅ **Gráficas en tiempo real** de la propagación
- ✅ **Comparación de escenarios** (lento, medio, rápido)
- ✅ **Interpretación automática** de resultados
- ✅ **Sección educativa completa** sobre Transformada de Laplace
- ✅ **Interfaz limpia y profesional** para presentaciones
- ✅ **Código comentado** fácil de entender
- ✅ **Tabla de datos detallados**
- ✅ **Cálculos analíticos** (tiempo al 50%, velocidad inicial, etc.)

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clone o descargue el proyecto:**
   ```bash
   cd laplace
   ```

2. **Instale las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecute la aplicación:**
   ```bash
   streamlit run app.py
   ```

4. **Abra en su navegador:**
   - Automáticamente se abrirá en `http://localhost:8501`
   - Si no, ingrese manualmente la URL anterior

## 📋 Estructura del Proyecto

```
laplace/
├── app.py              # Aplicación principal en Streamlit
├── requirements.txt    # Dependencias del proyecto
└── README.md          # Este archivo
```

## 🎮 Cómo Usar la Aplicación

### Pestaña 1: Simulador 🎯

1. **Ajuste los parámetros:**
   - **Alcance Inicial (N₀):** Número de personas alcanzadas al principio (ej: 100)
   - **Alcance Máximo (Nmax):** Máximo potencial (ej: 10,000)
   - **Velocidad (k):** Qué tan rápido se propaga (0.01 a 1.0)
   - **Tiempo de Simulación:** Duración en días

2. **Seleccione escenarios para comparar:**
   - ☑️ Propagación Lenta (k=0.05)
   - ☑️ Propagación Media (k=0.15)
   - ☑️ Propagación Rápida (k=0.3)

3. **Haga clic en "🚀 Ejecutar Simulación"**

4. **Analice los resultados:**
   - Gráfica interactiva de N(t) vs tiempo
   - Métricas clave (tiempo al 50%, velocidad inicial, etc.)
   - Interpretación automática
   - Tabla de datos detallados

### Pestaña 2: Teoría Matemática 📚

Explicación completa de:
- El problema real y su contexto
- La ecuación diferencial y su interpretación
- Introducción a la Transformada de Laplace
- Pasos de resolución paso a paso
- La solución final
- Comparación de métodos

### Pestaña 3: Acerca de ℹ️

Información sobre:
- Objetivos del proyecto
- Casos de uso aplicables
- Por qué este modelo
- Stack tecnológico
- Recomendaciones de uso en clase

## 📈 Casos de Uso

El modelo utilizado es aplicable a:

- 📱 **Virales en redes sociales:** Cómo un video o meme se propaga
- 📰 **Difusión de noticias:** Velocidad de propagación de información
- 📢 **Campañas publicitarias:** Alcance de una campaña
- 💻 **Adopción de tecnología:** Cómo se adoptan nuevas tecnologías
- 🦠 **Epidemiología:** Propagación de enfermedades
- 🚀 **Difusión de innovaciones:** Cómo se distribuyen innovaciones

## 💡 Ejemplos de Simulación

### Ejemplo 1: Video Viral
```
N₀ = 100 (personas iniciales)
Nmax = 1,000,000 (potencial máximo)
k = 0.2 (se propaga muy rápido)
t = 30 días

Resultado: En 30 días alcanza casi la totalidad del potencial
```

### Ejemplo 2: Noticia en Comunidad Local
```
N₀ = 50 (personas iniciales)
Nmax = 10,000 (comunidad local)
k = 0.05 (propagación lenta)
t = 60 días

Resultado: Crecimiento más gradual, similar a como se propagan chismes
```

### Ejemplo 3: Campaña de Marketing
```
N₀ = 1,000 (contactos iniciales)
Nmax = 100,000 (mercado objetivo)
k = 0.1 (propagación media)
t = 45 días

Resultado: Saturación moderada después del período analizado
```

## 🔬 Fundamentos Matemáticos (Resumen)

### ¿Por qué Transformada de Laplace?

La Transformada de Laplace es una herramienta que:

1. **Convierte** ecuaciones diferenciales en ecuaciones algebraicas
2. **Simplifica** la resolución de sistemas dinámicos
3. **Proporciona** soluciones analíticas exactas

### Proceso de Resolución

```
Ecuación diferencial
    ↓ Aplicar Transformada de Laplace
Ecuación algebraica (más fácil)
    ↓ Resolver algebraicamente
Solución en dominio de frecuencia
    ↓ Aplicar Transformada Inversa
Solución en dominio del tiempo: N(t) = Nmax - (Nmax - N₀)e^(-kt)
```

## 🎓 Uso en Presentación

**Estructura sugerida para la exposición:**

1. **Introducción (5 min):**
   - Mostrar un video viral como motivación
   - Formular la pregunta: "¿Cómo modelar esto matemáticamente?"

2. **Teoría (15 min):**
   - Explicar la ecuación diferencial
   - Introducir la Transformada de Laplace
   - Derivar la solución paso a paso

3. **Demostración (15 min):**
   - Usar el simulador en vivo
   - Cambiar parámetros y mostrar efectos
   - Dejar que la audiencia haga predicciones

4. **Análisis (10 min):**
   - Discutir otros casos de uso
   - Analizar limitaciones del modelo
   - Comparar con datos reales (si es posible)

## 🛠️ Tecnología Utilizada

- **Python 3.8+:** Lenguaje de programación principal
- **Streamlit:** Framework para aplicaciones web interactivas (sin necesidad de HTML/CSS)
- **NumPy:** Cálculos numéricos y manejo de arrays
- **Matplotlib:** Visualización de gráficas
- **Pandas:** Manipulación de datos en tablas

### ¿Por qué Streamlit?

- ✅ **Desarrollo rápido:** Sin HTML/CSS/JavaScript
- ✅ **Interactivo:** Widgets intuitivos
- ✅ **Profesional:** Interfaz moderna
- ✅ **Educativo:** Fácil de entender para principiantes
- ✅ **Desplegable:** Puede alojarse en la nube fácilmente

## 📚 Para Aprender Más

### Conceptos Relacionados
- Ecuaciones Diferenciales Ordinarias (EDO)
- Transformada de Laplace e Inversa
- Análisis de sistemas dinámicos
- Modelado matemático
- Métodos numéricos

### Recursos Recomendados
- Libros de Cálculo Avanzado y Ecuaciones Diferenciales
- Cursos online de MIT OpenCourseWare
- Documentación oficial de NumPy y Matplotlib

## 📝 Notas Adicionales

- La solución utiliza la fórmula analítica exacta, no aproximaciones numéricas
- Los gráficos se generan con 500 puntos para suavidad visual
- El modelo asume que k es constante (en realidad podría variar con factores externos)
- Para mejor precisión en casos reales, considere datos históricos reales

## 🐛 Resolución de Problemas

### "Module 'streamlit' not found"
```bash
pip install streamlit
```

### "Permission denied" al instalar paquetes
```bash
pip install --user -r requirements.txt
```

### El puerto 8501 ya está en uso
```bash
streamlit run app.py --server.port 8502
```

## 📄 Licencia

Este proyecto es de código abierto y está disponible para uso educativo.

## 👨‍💼 Autor

Proyecto educativo desarrollado para exposición de Matemáticas Aplicadas.

---

**¡Disfrute explorando la Transformada de Laplace con este simulador interactivo!** 🚀
