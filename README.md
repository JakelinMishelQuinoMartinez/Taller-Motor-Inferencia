# Taller: Diagnóstico de PC con Inteligencia Artificial

Este proyecto es un **Sistema Experto** creado en Python para detectar fallas en computadoras.

---

## 1. ¿Cómo funciona el sistema?

El programa se divide en 5 partes sencillas:
1. **Base de Conocimiento:** Es el "manual técnico" donde están guardadas todas las reglas y fallas conocidas con su nivel de confianza.
2. **Base de Hechos:** Es la memoria temporal que guarda los síntomas que el usuario va respondiendo en el momento.
3. **Motor de Inferencia:** Es el "cerebro" del programa. Compara los síntomas del usuario con el manual de fallas para encontrar coincidencias.
4. **Interfaz de Explicación:** Le muestra al usuario qué síntomas exactos activaron el diagnóstico.
5. **Interfaz de Usuario:** El cuestionario interactivo en la pantalla.

---

## 2. Mejoras y Desafíos Implementados

* **Preguntas Inteligentes:** Si el usuario dice que la PC *no enciende*, el sistema es lo suficientemente inteligente como para no hacer preguntas absurdas (como si tiene pantalla azul o virus).
* **Nivel 1 (Más Fallas):** Agregué 3 reglas nuevas para detectar problemas de batería en laptops, fallas de Wi-Fi y la pila de la BIOS descargada.
* **Nivel 2 (Ranking de Soluciones):** En lugar de dar una sola respuesta, el motor ahora muestra **todas las fallas posibles ordenadas de mayor a menor probabilidad**, según su porcentaje de confianza.

---

## 3. Preguntas y Respuestas

### 1. ¿Cuál es la diferencia principal entre un sistema experto y un programa tradicional?
Un programa tradicional sigue instrucciones fijas y obligatorias en el código (si pasa X, haz Y). Un sistema experto separa las reglas del problema del motor que las analiza, permitiendo que el sistema "piense" y tome caminos diferentes según las respuestas.

### 2. ¿Por qué el conocimiento está separado del motor de razonamiento? ¿Cuál es la ventaja?
Porque las reglas (el conocimiento) se guardan en una lista aparte de las funciones que las procesan (el motor). La ventaja es que puedes agregar, quitar o cambiar reglas de fallas de PC muy fácil sin tener que modificar todo el código del programa.

### 3. ¿Qué es la base de hechos y en qué se diferencia de la base de conocimiento?
**Base de Hechos:** Son los datos temporales del caso actual (los síntomas que el usuario marca con "sí" en la encuesta de hoy).
**Base de Conocimiento:** Es el manual permanente (la lista fija de todas las reglas y diagnósticos que el programa ya se sabe).

### 4. ¿Qué significa que pueda "explicar su razonamiento"? ¿Por qué importa en medicina o derecho?
Significa que el programa te dice exactamente qué síntomas (hechos) activaron esa respuesta. Es vital en medicina o derecho porque un doctor o un juez no pueden tomar decisiones graves basados en una caja negra; necesitan ver la lógica detrás para estar seguros.

### 5. ¿Por qué fracasaron comercialmente en los años 90? (3 razones)
- Escribir miles de reglas a mano hablando con expertos humanos era lentísimo y costaba mucho dinero.
- No aprendían solos de la experiencia, se quedaban estancados si algo cambiaba.
- Mantenerlos actualizados al ritmo que avanzaba la tecnología era casi imposible.

## 6. Con los hechos {fiebre=True, tos=False, perdida_olfato=True}, ¿se activa la regla: SI (fiebre AND tos) OR perdida_olfato ENTONCES sospecha_covid?
Sí se activa. La primera parte (fiebre AND tos) da falso porque falta la tos, pero como la regla usa un OR (O), basta con que perdida_olfato sea verdadero para que toda la regla se cumpla.

### 7. Tabla de verdad para: (A AND NOT B) OR (NOT A AND B)
| A | B | NOT A | NOT B | A AND NOT B | NOT A AND B | Resultado Final |
|---|---|---|---|---|---|---|
| V | V | F | F | F | F | **F** |
| V | F | F | V | V | F | **V** |
| F | V | V | F | F | V | **V** |
| F | F | V | V | F | F | **F** |

### 8. ¿Diferencia entre encadenamiento hacia adelante y hacia atrás?
- **Hacia adelante (De los síntomas a la solución):** Empezar con los datos y buscar qué diagnóstico se cumple. Ejemplo: Ver que la PC no da video, pita y se deduce que es la RAM.
- **Hacia atrás (De la sospecha a los síntomas):** Empezar con una hipótesis y buscar pruebas para ver si es verdad. Ejemplo: Sospechas de que la PC tiene virus y se va a revisar específicamente si el administrador de tareas muestra el disco al 100%.

### 9. 3 Reglas IF-THEN para recomendar un lenguaje:
- **Regla 1:** SI el objetivo es desarrollo_web ENTONCES aprender JavaScript.
- **Regla 2:** SI el objetivo es analisis_datos ENTONCES aprender Python.
- **Regla 3:** SI el objetivo es desarrollo_videojuegos ENTONCES aprender C#.

### 10. Red de inferencia de las 3 reglas:
```text
[objetivo: desarrollo_web] ---> ( Regla 1 ) ---> [aprender: JavaScript]
[objetivo: analisis_datos] ---> ( Regla 2 ) ---> [aprender: Python]
[objetivo: des_videojuegos] ---> ( Regla 3 ) ---> [aprender: C#]
```

### 11. ¿Qué problema surge si dos reglas piden lo mismo pero dan conclusiones diferentes? ¿Cómo se resuelve?
Se genera una contradicción (el motor no sabrá cuál elegir porque ambas empatan perfectamente).
**Solución:** Se resuelve agregando una condición más a una de las reglas para desempatar (hacerla más específica), o usando el nivel de confianza para que el motor elija la que más veces ocurre en la vida real.