import datetime

def calcular_diferencia_fechas(fecha1_str, fecha2_str):
    # Convertir las cadenas de texto a objetos de fecha
    formato_fecha = "%d/%m/%Y"  # Formato de fecha: día/mes/año
    fecha1 = datetime.datetime.strptime(fecha1_str, formato_fecha)
    fecha2 = datetime.datetime.strptime(fecha2_str, formato_fecha)
    
    # Calcular la diferencia entre las dos fechas
    diferencia = fecha2 - fecha1
    
    # Retornar la diferencia en días
    return diferencia.days

# Ejemplo de uso
fecha1 = "20/05/2023"
fecha2 = "29/08/2024"

dias_diferencia = calcular_diferencia_fechas(fecha1, fecha2)
print(f"La diferencia entre {fecha1} y {fecha2} es de {dias_diferencia} días.")
