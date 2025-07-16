# Códigos de Aprendizaje por Refuerzo

Este repositorio contiene implementaciones y ejemplos de algoritmos de aprendizaje por refuerzo (Reinforcement Learning) desarrollados con fines educativos y de investigación.

## 📋 Contenido del Repositorio

### 1. FrozenLake Q-Learning (`FrozenLake5.py`)
Implementación del algoritmo Q-Learning aplicado al ambiente FrozenLake de OpenAI Gym.

**Características:**
- Algoritmo Q-Learning con exploración ε-greedy decreciente
- Ambiente FrozenLake-v1 con penalizaciones personalizadas
- Visualización de la política aprendida
- Configuración de hiperparámetros: learning rate = 0.1, γ = 0.95

**Funcionalidades principales:**
- Entrenamiento del agente durante 500 episodios
- Penalizaciones adicionales en estados específicos (5, 7, 11, 12)
- Función de visualización para observar la política aprendida

### 2. Q-Iteration para Robot Limpiador (`Q_iteration_Robot_clening.ipynb`)
Implementación del algoritmo Q-Iteration (Value Iteration) para un problema de robot limpiador en un ambiente determinístico.

**Características del ambiente:**
- 6 estados discretos
- 2 acciones posibles: [-1, 1] (moverse izquierda/derecha)
- Estados terminales con recompensas específicas
- Ambiente completamente determinístico

**Componentes principales:**
- Clase `enviroment()`: Define las dinámicas del ambiente del robot
- Clase `Qiteration()`: Implementa el algoritmo de iteración Q
- Función de recompensa personalizada
- Visualización de la convergencia de la función Q

### 3. FrozenLake Colaborativo (`FrozenLake2024.ipynb`)
Implementación colaborativa del ambiente FrozenLake con extensiones adicionales.

## 🚀 Instalación y Uso

### Requisitos
```bash
pip install numpy
pip install gym
pip install matplotlib
```

### Ejecución

**Para FrozenLake Q-Learning:**
```bash
python FrozenLake5.py
```

**Para Q-Iteration Robot:**
```bash
jupyter notebook Q_iteration_Robot_clening.ipynb
```

## 📊 Algoritmos Implementados

### Q-Learning
- **Tipo:** Model-free, off-policy
- **Aplicación:** Ambiente estocástico (FrozenLake)
- **Exploración:** ε-greedy decreciente

### Q-Iteration (Value Iteration)
- **Tipo:** Model-based, planning
- **Aplicación:** Ambiente determinístico (Robot limpiador)
- **Convergencia:** Garantizada para ambientes determinísticos

## 🎯 Objetivos de Aprendizaje

Este repositorio está diseñado para:
- Comprender las diferencias entre algoritmos model-free y model-based
- Implementar algoritmos de aprendizaje por refuerzo desde cero
- Comparar el comportamiento en ambientes determinísticos vs estocásticos
- Visualizar el proceso de aprendizaje y convergencia

## 📈 Resultados

Los algoritmos implementados demuestran:
- Convergencia exitosa hacia políticas óptimas
- Manejo efectivo de la exploración vs explotación
- Adaptación a diferentes tipos de ambientes

## 🔧 Personalización

Los códigos incluyen parámetros configurables:
- **Learning rate:** Controla la velocidad de aprendizaje
- **Discount factor (γ):** Importancia de recompensas futuras
- **Número de episodios:** Duración del entrenamiento
- **Funciones de recompensa:** Modificables según el problema

## 📚 Referencias

- Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction.
- OpenAI Gym: https://gym.openai.com/
- Documentación de NumPy y Matplotlib

## 🤝 Contribuciones

Este repositorio está abierto a contribuciones para:
- Nuevos algoritmos de RL
- Mejoras en la documentación
- Optimizaciones de código
- Nuevos ambientes de prueba

---

**Nota:** Este repositorio tiene fines educativos y de investigación en el área de aprendizaje por refuerzo.
