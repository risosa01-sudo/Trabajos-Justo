# 0. Información del DataFrame
* Vista general de la estructura de los datos.
* Revisión de tipos de datos y valores no nulos.

![Información del DataFrame](1_informacion_df.png)

---
# 1. Eliminación de duplicados
* Se considera un duplicado cuando todos los campos de la fila son idénticos.
* Especial atención a los casos donde el id se repite pero los datos varían (estos no deben borrarse automáticamente).

![Eliminación de duplicados](2_eliminación_duplicados.png)

---
# 2. Normalización de productos
* Eliminar espacios en blanco y convertir a formato CamelCase o Capitalizado.

![Normalización de productos](3_normalización_productos.png)

---
# 3. Tratamiento de precios
* Localizar valores no numéricos (como “ERR”) y tratarlos como nulos.
* Imputar los valores faltantes utilizando la mediana de la columna.

![Tratamiento de precios](4_tratamiento_de_productos.png)

---
# 4. Validación de cantidades
* Detectar y filtrar registros con cantidades negativas (considerarlos errores de entrada).

![Validación de cantidades](5_validacion_cantidades.png)

---
# 5. Estandarización temporal
* Convertir diversos formatos de fecha al estándar ISO.
* Resolver valores relativos como “Ayer” o “Hace 2 dias” calculando la fecha real respecto al día de hoy (usa datetime.now()).

![Estandarización temporal 1](6_estandarizacion_temporal.png)
![Estandarización temporal 2](7_estandarizacion_temporal.png)
![Estandarización temporal 3](8_estandarizacion_temporal.png)