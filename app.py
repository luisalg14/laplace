"""
Simulador de Propagación de Información en Redes Sociales
usando la Transformada de Laplace

Este software educativo simula cómo una publicación, noticia o campaña
se difunde en una red social con el tiempo, basado en un modelo matemático
de ecuaciones diferenciales resuelto con la Transformada de Laplace.
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import math

# Configuración de la página
st.set_page_config(
    page_title="Simulador de Propagación en Redes Sociales",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuración de estilo
rcParams['font.size'] = 10
rcParams['figure.figsize'] = (10, 6)

# Título y descripción
st.title("📱 Simulador de Propagación de Información en Redes Sociales")
st.markdown("### Usando la Transformada de Laplace para modelar dinámicas de propagación")

# Crear tabs principales
tab_acerca, tab_teoria, tab_simulador = st.tabs(["ℹ️ Acerca de", "📚 Teoría Matemática", "🎯 Simulador"])

# ============================================================================
# TAB 1: SIMULADOR
# ============================================================================
with tab_simulador:
    st.header("Herramienta Interactiva de Simulación")
    
    # Dividir en dos columnas
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("⚙️ Parámetros de Simulación")
        
        # Entrada de parámetros
        N0 = st.number_input(
            "Alcance inicial: N₀ (personas que ven la publicación al inicio)",
            min_value=1,
            max_value=10000,
            value=100,
            step=100,
            help="Número inicial de personas alcanzadas por la publicación"
        )
        
        Nmax = st.number_input(
            "Alcance máximo: Nmax (total máximo de personas que podrían verla)",
            min_value=N0 + 1,
            max_value=100000,
            value=10000,
            step=1000,
            help="Máximo número de personas que podrían ser alcanzadas"
        )
        
        k = st.slider(
            "Velocidad de propagación: k (qué tan rápido se comparte)",
            min_value=0.01,
            max_value=1.0,
            value=0.1,
            step=0.01,
            help="Parámetro que controla qué tan rápido se propaga (mayor = más rápido)"
        )
        
        t_max = st.number_input(
            "Tiempo de Simulación (días)",
            min_value=1,
            max_value=365,
            value=30,
            step=1,
            help="Duración total de la simulación en días"
        )
        
        # Botón para simular
        simular = st.button("🚀 Ejecutar Simulación", use_container_width=True)
    
    with col2:
        st.subheader("📊 Comparación de Escenarios")
        
        st.markdown("""
        **Compare cómo diferentes velocidades de propagación afectan el alcance:**
        """)
        
        # Escenarios predefinidos
        escenario_lento = st.checkbox("🐢 Propagación Lenta (k=0.05)", value=True)
        escenario_medio = st.checkbox("🚗 Propagación Media (k=0.15)", value=True)
        escenario_rapido = st.checkbox("🚀 Propagación Rápida (k=0.3)", value=True)
        
        st.markdown("""
        ---
        **Nota:** Estos escenarios usan los mismos valores de N₀ y Nmax,
        pero con diferentes velocidades de propagación.
        """)
    
    # Si se presiona simular, ejecutar cálculos
    if simular:
        # Función para calcular N(t)
        def calcular_alcance(N0, Nmax, k, t):
            """
            Calcula el alcance en tiempo t usando la solución de la ecuación diferencial
            
            Ecuación diferencial: dN/dt = k(Nmax - N)
            Solución: N(t) = Nmax - (Nmax - N0) * e^(-k*t)
            
            Args:
                N0: Alcance inicial
                Nmax: Alcance máximo
                k: Velocidad de propagación
                t: Tiempo (puede ser escalar o array)
            
            Returns:
                Alcance en tiempo t
            """
            return Nmax - (Nmax - N0) * np.exp(-k * t)
        
        # Crear array de tiempo
        tiempo = np.linspace(0, t_max, 500)
        
        # Calcular alcance para escenario principal
        alcance_principal = calcular_alcance(N0, Nmax, k, tiempo)
        
        # Crear figura de la gráfica principal
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Gráfica del escenario principal
        ax.plot(tiempo, alcance_principal, 'b-', linewidth=3, label=f'Simulación (k={k})')
        ax.fill_between(tiempo, N0, alcance_principal, alpha=0.2, color='blue')
        
        # Línea horizontal del alcance máximo
        ax.axhline(y=Nmax, color='red', linestyle='--', linewidth=2, alpha=0.7, label=f'Alcance Máximo (Nmax={Nmax})')
        
        # Línea horizontal del alcance inicial
        ax.axhline(y=N0, color='green', linestyle='--', linewidth=2, alpha=0.7, label=f'Alcance Inicial (N₀={N0})')
        
        # Agregar escenarios de comparación
        if escenario_lento:
            alcance_lento = calcular_alcance(N0, Nmax, 0.05, tiempo)
            ax.plot(tiempo, alcance_lento, ':', linewidth=2, color='orange', label='Propagación Lenta (k=0.05)', alpha=0.8)
        
        if escenario_medio:
            alcance_medio = calcular_alcance(N0, Nmax, 0.15, tiempo)
            ax.plot(tiempo, alcance_medio, ':', linewidth=2, color='purple', label='Propagación Media (k=0.15)', alpha=0.8)
        
        if escenario_rapido:
            alcance_rapido = calcular_alcance(N0, Nmax, 0.3, tiempo)
            ax.plot(tiempo, alcance_rapido, ':', linewidth=2, color='red', label='Propagación Rápida (k=0.3)', alpha=0.8)
        
        # Configurar etiquetas y leyenda
        ax.set_xlabel('Tiempo (días)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Alcance - Número de Personas (N)', fontsize=12, fontweight='bold')
        ax.set_title('Propagación de Información en Red Social\nAplicando la Transformada de Laplace', 
                    fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3, linestyle='--')
        ax.legend(loc='right', fontsize=10, framealpha=0.95)
        ax.set_xlim(0, t_max)
        
        # Mostrar gráfica
        st.pyplot(fig)
        plt.close(fig)
        
        # ====================================================================
        # CÁLCULOS Y ANÁLISIS
        # ====================================================================
        st.divider()
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Calcular alcance al 50%
            # Nmax - (Nmax - N0) * e^(-k*t) = (N0 + Nmax) / 2
            # (Nmax - N0) * e^(-k*t) = (Nmax - N0) / 2
            # e^(-k*t) = 0.5
            # -k*t = ln(0.5)
            # t = -ln(0.5) / k
            t_50 = -np.log(0.5) / k
            alcance_50 = calcular_alcance(N0, Nmax, k, t_50)
            
            st.metric(
                "Tiempo al 50% de Alcance",
                f"{t_50:.2f} días",
                help="Tiempo necesario para alcanzar el punto medio entre N₀ y Nmax"
            )
        
        with col2:
            # Alcance final (teórico, muy cercano a Nmax)
            alcance_final = calcular_alcance(N0, Nmax, k, t_max)
            porcentaje_final = (alcance_final / Nmax) * 100
            
            st.metric(
                "Alcance al Final de la Simulación",
                f"{alcance_final:,.0f}",
                f"{porcentaje_final:.1f}% de Nmax"
            )
        
        with col3:
            # Velocidad inicial de propagación (dN/dt en t=0)
            # dN/dt = k(Nmax - N), en t=0: dN/dt = k(Nmax - N0)
            velocidad_inicial = k * (Nmax - N0)
            
            st.metric(
                "Velocidad Inicial de Propagación",
                f"{velocidad_inicial:,.0f} personas/día",
                help="Tasa de crecimiento al inicio de la publicación"
            )
        
        # ====================================================================
        # INTERPRETACIÓN DE RESULTADOS
        # ====================================================================
        st.subheader("📈 Interpretación de Resultados")
        
        interpretacion = f"""
        ### Análisis de la Simulación:
        
        **Parámetros utilizados:**
        - Alcance Inicial (N₀): {N0:,} personas
        - Alcance Máximo (Nmax): {Nmax:,} personas
        - Velocidad de Propagación (k): {k}
        - Tiempo de Simulación: {t_max} días
        
        **Hallazgos principales:**
        
        1. **Crecimiento Exponencial Amortiguado:**
           La publicación comienza con {N0:,} personas alcanzadas y se propaga de manera exponencial, 
           pero a un ritmo decreciente conforme se acerca al límite de {Nmax:,} personas.
        
        2. **Punto Crítico (50%):**
           La publicación alcanza el {50}% de su potencial máximo en aproximadamente **{t_50:.1f} días**.
           En este punto, ha llegado a **{alcance_50:,.0f} personas**.
        
        3. **Velocidad Inicial:**
           En el primer momento, la información se propaga a una velocidad de **{velocidad_inicial:,.0f} personas por día**.
           Esta velocidad disminuye con el tiempo conforme hay menos personas nuevas para alcanzar.
        
        4. **Saturación del Mercado:**
           Después de {t_max} días, la campaña ha alcanzado a **{alcance_final:,.0f} personas**, 
           que representa el **{porcentaje_final:.1f}%** del potencial máximo.
        
        5. **Implicaciones Prácticas:**
           - Si k es mayor: La información se propaga más rápido, alcanzando a más personas en menos tiempo.
           - Si k es menor: La propagación es más lenta y gradual.
           - El límite natural es siempre Nmax (no todas las personas en el universo ven la publicación).
        """
        
        st.markdown(interpretacion)
        
        # ====================================================================
        # TABLA DE DATOS
        # ====================================================================
        st.subheader("📋 Tabla de Datos Detallados")
        
        # Crear tabla con puntos clave
        puntos_clave = np.array([0, t_max/4, t_max/2, 3*t_max/4, t_max])
        datos_tabla = []
        
        for t in puntos_clave:
            N = calcular_alcance(N0, Nmax, k, t)
            porcentaje = (N / Nmax) * 100
            datos_tabla.append({
                'Tiempo (días)': f'{t:.1f}',
                'Alcance N(t)': f'{N:,.0f}',
                '% de Nmax': f'{porcentaje:.1f}%'
            })
        
        import pandas as pd
        df = pd.DataFrame(datos_tabla)
        st.dataframe(df, use_container_width=True, hide_index=True)

# ============================================================================
# TAB 2: TEORÍA MATEMÁTICA
# ============================================================================
with tab_teoria:
    st.header("📚 Fundamentos Matemáticos")
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("1️⃣ El Problema Real")
        st.markdown("""
        #### ¿Cómo se propaga una publicación en las redes sociales?
        
        Cuando alguien publica algo importante (noticia, campaña, anuncio), 
        queremos saber:
        
        - **¿Cuántas personas la verán?**
        - **¿A qué velocidad se propaga?**
        - **¿Cuánto tiempo tarda en alcanzar el máximo?**
        
        La respuesta NO es lineal. Al principio crece rápido, pero después 
        el crecimiento se ralentiza.
        
        **Analogía:** Es como una epidemia que se propaga, pero eventualmente 
        se satura porque casi todos ya lo vieron.
        """)
    
    with col2:
        st.subheader("2️⃣ La Ecuación Diferencial")
        st.markdown("""
        #### Modelo Matemático
        
        Expresamos la propagación como una **ecuación diferencial**:
        
        $$\\frac{dN}{dt} = k(N_{max} - N)$$
        
        **¿Qué significa?**
        - **dN/dt:** Cambio en el alcance con respecto al tiempo
        - **k:** Constante de propagación (velocidad)
        - **(Nmax - N):** Espacio disponible para crecer
        
        **Interpretación:**
        > "La velocidad de crecimiento es proporcional al espacio 
        > disponible que aún no hemos alcanzado"
        """)
    
    st.divider()
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.subheader("3️⃣ Transformada de Laplace")
        st.markdown("""
        #### ¿Por qué la Transformada de Laplace?
        
        La **Transformada de Laplace** es una técnica matemática que:
        
        1. **Convierte** ecuaciones diferenciales en ecuaciones algebraicas
        2. **Simplifica** la resolución de problemas dinámicos
        3. **Facilita** el análisis de sistemas en el dominio de la frecuencia
        
        **En nuestro caso:**
        
        - Tomamos la ecuación diferencial en el **dominio del tiempo**
        - Aplicamos la Transformada de Laplace
        - Resolvemos en el **dominio de la frecuencia** (mucho más fácil)
        - Aplicamos la **Transformada Inversa** para volver al tiempo
        """)
    
    with col2:
        st.subheader("4️⃣ Pasos de Resolución")
        st.markdown("""
        #### Resolución usando Transformada de Laplace
        
        **Paso 1:** Ecuación diferencial original
        
        $$\\frac{dN}{dt} = k(N_{max} - N)$$
        
        **Paso 2:** Aplicar Transformada de Laplace
        
        $$sF(s) - N_0 = k\\left(\\frac{N_{max}}{s} - F(s)\\right)$$
        
        **Paso 3:** Despejar F(s) (mucho más fácil)
        
        $$F(s) = \\frac{N_0}{s + k} + \\frac{kN_{max}}{s(s + k)}$$
        
        **Paso 4:** Descomponer en fracciones parciales y aplicar 
        la Transformada Inversa
        """)
    
    st.divider()
    
    st.subheader("5️⃣ La Solución Final")
    st.markdown("""
    #### Resultado de la Transformada Inversa de Laplace
    
    Después de aplicar la Transformada Inversa, obtenemos la 
    **solución analítica exacta**:
    
    $$N(t) = N_{max} - (N_{max} - N_0)e^{-kt}$$
    
    **Esta es la fórmula que usa nuestro simulador.**
    
    ### Características de la solución:
    
    | Característica | Descripción |
    |---|---|
    | **Cuando t = 0** | N(0) = N₀ (comienza en el alcance inicial) |
    | **Cuando t → ∞** | N(t) → Nmax (asintóticamente se aproxima al máximo) |
    | **Comportamiento** | Crecimiento exponencial amortiguado |
    | **Velocidad inicial** | dN/dt\\|_{t=0} = k(Nmax - N₀) |
    | **Velocidad final** | dN/dt\\|_{t→∞} = 0 (se estabiliza) |
    
    """)
    
    st.divider()
    
    st.subheader("6️⃣ Comparación: Antes vs Después de Laplace")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        **❌ Sin Transformada de Laplace:**
        
        - Ecuación diferencial compleja
        - Requiere técnicas de integración avanzadas
        - Solución no trivial
        - Difícil de interpretar
        - Tiempo de cálculo manual: horas
        """)
    
    with col2:
        st.markdown("""
        **✅ Con Transformada de Laplace:**
        
        - Convierte a ecuación algebraica simple
        - Resolución directa (álgebra básica)
        - Solución clara y elegante
        - Fácil de interpretar y visualizar
        - Tiempo de cálculo: minutos
        """)

# ============================================================================
# TAB 3: ACERCA DE
# ============================================================================
with tab_acerca:
    st.header("ℹ️ Acerca de este Proyecto")
    
    st.markdown("""
    ### 🎓 Proyecto Educativo
    
    Este simulador fue desarrollado como herramienta educativa para 
    una exposición sobre **Transformada de Laplace en Aplicaciones Prácticas**.
    
    ---
    
    ### 🎯 Objetivos
    
    1. **Demostrar** cómo la Transformada de Laplace resuelve problemas reales
    2. **Visualizar** dinámicas de propagación de información
    3. **Facilitar** la comprensión de ecuaciones diferenciales
    4. **Mostrar** aplicaciones prácticas del cálculo avanzado
    5. **Permitir** experimentación interactiva con parámetros
    
    ---
    
    ### 📊 Caso de Uso: Redes Sociales
    
    El modelo utilizado es aplicable a:
    
    - **Virales en redes sociales:** Cómo un video o meme se propaga
    - **Difusión de noticias:** Velocidad de propagación de información
    - **Campañas publicitarias:** Alcance de una campaña publicitaria
    - **Adopción de tecnología:** Cómo nuevas tecnologías se adoptan
    - **Epidemiología:** Propagación de enfermedades (modelo SIS/SIR)
    - **Difusión de innovaciones:** Cómo las innovaciones se distribuyen
    
    ---
    
    ### 💡 ¿Por qué este modelo?
    
    El modelo logístico (ecuación diferencial que usamos) es:
    
    - **Simple:** Fácil de entender y explicar
    - **Realista:** Captura el comportamiento principal de la propagación
    - **Resoluble:** Tiene solución analítica exacta
    - **Versátil:** Aplicable a muchos contextos
    
    ---
    
    ### 🛠️ Tecnología
    
    **Stack tecnológico:**
    - **Python 3.8+:** Lenguaje de programación
    - **Streamlit:** Framework web interactivo
    - **NumPy:** Cálculos numéricos y arrays
    - **Matplotlib:** Visualización de gráficas
    
    **Ventajas de Streamlit:**
    - Sin necesidad de HTML/CSS/JavaScript
    - Desarrollo rápido
    - Interfaz moderna y responsiva
    - Ideal para aplicaciones educativas y científicas
    
    ---
    
    ### 📚 Para Aprender Más
    
    **Conceptos relacionados:**
    - Ecuaciones Diferenciales Ordinarias (EDO)
    - Transformada de Laplace e Inversa
    - Análisis de sistemas dinámicos
    - Modelado matemático
    - Métodos numéricos
    
    **Recursos sugeridos:**
    - Libros de Cálculo Avanzado
    - Cursos de Ecuaciones Diferenciales
    - Documentación de métodos matemáticos aplicados
    
    ---
    
    ### 👨‍🏫 Uso en Clase
    
    **Este simulador puede usarse para:**
    
    1. **Motivación:** Mostrar aplicaciones reales del cálculo
    2. **Explicación:** Visualizar la solución de ecuaciones diferenciales
    3. **Experimentación:** Que los estudiantes cambien parámetros
    4. **Análisis:** Interpretar gráficas y datos
    5. **Evaluación:** Asignar ejercicios de modelado
    
    **Sugerencias pedagógicas:**
    - Comience con el problema real (redes sociales)
    - Muestre la ecuación diferencial
    - Explique la Transformada de Laplace paso a paso
    - Use el simulador para verificar resultados teóricos
    - Pida a los estudiantes que predigan el comportamiento
    
    ---
    
    ### 📝 Versión
    
    **Simulador de Propagación en Redes Sociales**  
    v1.0 - 2026
    
    Desarrollado como proyecto educativo para exposición de Matemáticas Aplicadas
    
    """)
    
    st.divider()
    
    st.info("""
    💡 **Consejo para la presentación:**
    
    1. Inicie con un ejemplo cotidiano (un video viral)
    2. Muestre la ecuación diferencial
    3. Explique por qué usamos Transformada de Laplace
    4. Use el simulador para demostrar casos reales
    5. Permita que la audiencia haga predicciones
    6. Compare predicciones con resultados de la simulación
    """)
