# ================================================================
# SISTEMA EXPERTO: Diagnóstico de PC
# Implementación con motor de inferencia hacia adelante
# ================================================================

# ──────────────────────────────────────────────────────────────
# COMPONENTE 1: BASE DE CONOCIMIENTO
# Aquí vive el conocimiento del experto técnico.
# Cada regla tiene: id, condiciones (lista de síntomas requeridos),
# conclusión y un factor de confianza de 0 a 1.
# ──────────────────────────────────────────────────────────────

base_de_conocimiento = [
    {
        "id": "R01",
        "descripcion": "Fuente de poder dañada",
        "condiciones": ["no_enciende", "sin_luces", "sin_sonido"],
        "conclusion": "Revisar o reemplazar la fuente de poder",
        "confianza": 0.92
    },
    {
        "id": "R02",
        "descripcion": "Falla de RAM",
        "condiciones": ["enciende", "pitidos_arranque", "sin_video"],
        "conclusion": "Probar con módulos de RAM de a uno",
        "confianza": 0.88
    },
    {
        "id": "R03",
        "descripcion": "Falla de tarjeta de video",
        "condiciones": ["enciende", "pantalla_negra", "sin_pitidos"],
        "conclusion": "Revisar tarjeta de video y conexiones del monitor",
        "confianza": 0.80
    },
    {
        "id": "R04",
        "descripcion": "Problemas de almacenamiento",
        "condiciones": ["enciende", "inicia_lento", "disco_al_100"],
        "conclusion": "Verificar salud del disco duro con herramienta SMART",
        "confianza": 0.85
    },
    {
        "id": "R05",
        "descripcion": "Infección por malware",
        "condiciones": ["enciende", "inicia_lento", "ventilador_siempre_activo"],
        "conclusion": "Escanear con antivirus y revisar procesos en segundo plano",
        "confianza": 0.72
    },
    {
        "id": "R06",
        "descripcion": "Driver o RAM dañada",
        "condiciones": ["enciende", "pantalla_azul_frecuente"],
        "conclusion": "Actualizar drivers y testear memoria RAM con MemTest86",
        "confianza": 0.87
    },
    {
        "id": "R07",
        "descripcion": "Sobrecalentamiento",
        "condiciones": ["enciende", "se_apaga_solo", "calor_excesivo"],
        "conclusion": "Limpiar ventiladores y reaplicar pasta térmica",
        "confianza": 0.90
    },
    {
        "id": "R08",
        "descripcion": "Pila de la BIOS agotada",
        "condiciones": ["enciende", "hora_desconfigurada", "error_cmos"],
        "conclusion": "Reemplazar la pila CR2032 de la placa madre",
        "confianza": 0.95
    },
    {
        "id": "R09",
        "descripcion": "Problema de conectividad Wi-Fi o Red",
        "condiciones": ["enciende", "sin_internet", "icono_red_alerta"],
        "conclusion": "Reiniciar el router, reinstalar controladores de red o revisar tarjeta Wi-Fi",
        "confianza": 0.82
    },
    {
        "id": "R10",
        "descripcion": "Batería de laptop degradada o dañada",
        "condiciones": ["enciende", "solo_funciona_enchufado", "descarga_rapida"],
        "conclusion": "Calibrar la batería mediante el sistema o solicitar un reemplazo físico",
        "confianza": 0.89
    }
]

# ──────────────────────────────────────────────────────────────
# COMPONENTE 2: BASE DE HECHOS (Working Memory)
# Estado actual del caso. Usamos un set de Python para
# representar los síntomas presentes (eficiente para búsqueda).
# ──────────────────────────────────────────────────────────────

base_de_hechos = set()  # vacía al inicio, se llena con los síntomas

# ──────────────────────────────────────────────────────────────
# COMPONENTE 3: MOTOR DE INFERENCIA
# Funciones de equiparación y resolución de conflictos
# ──────────────────────────────────────────────────────────────

def equiparar(base_conocimiento, hechos):
    """
    Proceso de equiparación (pattern matching).
    Retorna todas las reglas cuyas condiciones están satisfechas
    por los hechos actuales. Esto es el 'conflict set'.
    """
    conflict_set = []
    for regla in base_conocimiento:
        # Verificar si TODOS los síntomas de la regla están en los hechos
        # set.issubset() es O(len(condiciones)), más eficiente que un bucle
        if set(regla['condiciones']).issubset(hechos):
            conflict_set.append(regla)
    return conflict_set


def resolver_conflictos(conflict_set):
    """
    Estrategia de resolución de conflictos: mayor confianza.
    Si hay empate, preferir la regla con más condiciones (más específica).
    """
    return sorted(
        conflict_set, 
        key=lambda r: (r['confianza'], len(r['condiciones'])), 
        reverse=True
    )


def inferir(base_conocimiento, hechos):
    print()
    print('━' * 55)
    print('  MOTOR DE INFERENCIA INICIADO')
    print('━' * 55)
    print(f'  Hechos ingresados: {hechos}')
    print()

    conflict_set = equiparar(base_conocimiento, hechos)

    if not conflict_set:
        print('  ⚠ No se encontraron reglas aplicables.')
        return

    reglas_ordenadas = resolver_conflictos(conflict_set)
    mejor_regla = reglas_ordenadas[0]

    print('  DIAGNÓSTICO PRINCIPAL')
    print('  ───────────────────────────────────────────────────')
    print(f'  Regla aplicada: {mejor_regla["id"]} — {mejor_regla["descripcion"]}')
    print(f'  Recomendación:  {mejor_regla["conclusion"]}')
    print(f'  Confianza:      {mejor_regla["confianza"] * 100:.0f}%')
    print()

    if len(reglas_ordenadas) > 1:
        print('  RANKING DE OTRAS POSIBILIDADES:')
        for r in reglas_ordenadas[1:]:
            print(f'  - {r["id"]}: {r["descripcion"]} ({r["confianza"]*100:.0f}% confianza)')

    # COMPONENTE 4: INTERFAZ DE EXPLICACIÓN
    print()
    print('  TRAZABILIDAD DEL RAZONAMIENTO')
    print('  ───────────────────────────────────────────────────')
    print(f'  Síntomas que activaron la regla principal: {mejor_regla["condiciones"]}')
    print('━' * 55)



# ──────────────────────────────────────────────────────────────
# COMPONENTE 5: INTERFAZ DE USUARIO
# ──────────────────────────────────────────────────────────────

PREGUNTAS = {
    "no_enciende":              "¿El equipo NO enciende (sin luces, sin sonido)?",
    "sin_luces":                "¿No hay ninguna luz LED encendida?",
    "sin_sonido":               "¿No se escucha ningún sonido al encender?",
    "pitidos_arranque":         "¿Se escuchan pitidos (beeps) al encender?",
    "sin_video":                "¿La pantalla no muestra absolutamente nada?",
    "pantalla_negra":           "¿La pantalla queda en negro (sin pitidos)?",
    "sin_pitidos":              "¿No se escuchan pitidos?",
    "inicia_lento":             "¿El equipo tarda más de 3 minutos en iniciar?",
    "disco_al_100":             "¿El administrador de tareas muestra disco al 100%?",
    "ventilador_siempre_activo":"¿El ventilador está siempre a máxima velocidad?",
    "pantalla_azul_frecuente":  "¿Aparece pantalla azul (BSOD) con frecuencia?",
    "se_apaga_solo":            "¿El equipo se apaga solo sin advertencia?",
    "calor_excesivo":           "¿El chasis está muy caliente al tacto?",
    # Nuevas preguntas (Nivel 1)
    "hora_desconfigurada":      "¿La hora del reloj de Windows/Linux se desconfigura al apagar la PC?",
    "error_cmos":               "¿Aparece un mensaje de 'CMOS Checksum Error' al encender la máquina?",
    "sin_internet":             "¿El equipo se encuentra completamente sin acceso a internet?",
    "icono_red_alerta":         "¿El ícono de red muestra un triángulo amarillo o advertencia?",
    "solo_funciona_enchufado":  "¿La computadora portátil se apaga de inmediato al desconectar el cargador?",
    "descarga_rapida":          "¿La batería pasa de estar cargada a 0% en pocos minutos?"
}

def consultar():
    base_de_hechos.clear() 
    print()
    print('=' * 55)
    print('   SISTEMA EXPERTO: Diagnóstico de Computador')
    print('   Responde s (sí) o n (no) a cada pregunta')
    print('=' * 55)
    print()

    resp_encendido = input("  ¿El equipo enciende (hay luces o sonido)? [s/n]: ").strip().lower()
    if resp_encendido == 's':
        base_de_hechos.add('enciende')
    else:
        base_de_hechos.add('no_enciende')

    for sintoma, pregunta in PREGUNTAS.items():

        if 'no_enciende' in base_de_hechos and sintoma not in ["sin_luces", "sin_sonido"]:
            continue
            
        if 'enciende' in base_de_hechos and sintoma in ["sin_luces", "sin_sonido"]:
            continue

        resp = input(f'   {pregunta} [s/n]: ').strip().lower()
        if resp == 's':
            base_de_hechos.add(sintoma)

    inferir(base_de_conocimiento, base_de_hechos)


# Ejecutar
consultar()