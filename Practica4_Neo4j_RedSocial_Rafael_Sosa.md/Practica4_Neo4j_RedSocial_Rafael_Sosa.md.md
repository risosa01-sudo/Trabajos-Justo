# Práctica 4 - Neo4j: Red Social  
**Autor:** Rafael Sosa  

---

## Ejercicio 1: Diseño del Modelo de Datos de la Red Social

Diseña un modelo de datos de grafo para representar usuarios y sus interacciones en una red social.  
Considera los siguientes tipos de nodos y relaciones:

### 🔹 Nodos:
- **User:** con propiedades como `username`, `name`, `registration_date`.  
- **Post:** con propiedades como `content`, `timestamp`.

### 🔹 Relaciones:
- **FOLLOWS:** entre `User` y `User`.  
- **POSTED:** entre `User` y `Post`.  
- **LIKES:** entre `User` y `Post`.

---

## Ejercicio 2: Creación de Nodos y Relaciones Iniciales

Utiliza **Cypher** para crear los siguientes nodos y relaciones en tu base de datos.

### Creación de nodos
Crea al menos tres nodos de tipo `User` con las propiedades `username`, `name` y `registration_date`.  
Asegúrate de que los `username` sean únicos.  

![Creación de Nodos](creación%20de%20nodos.png)  
![Crear algunos nodos User](Crear%20algunos%20nodos%20User.png)

---

### Relaciones FOLLOWS
Crea algunas relaciones de tipo `FOLLOWS` entre tus usuarios.  
Por ejemplo: “Alice sigue a Bob”, “Bob sigue a Charlie”.

![Crear relaciones FOLLOWS](Crear%20relaciones%20FOLLOWS.png)  


---

### Creación de Posts y relaciones POSTED
Haz que al menos dos usuarios publiquen un `Post`.  
Cada post debe tener propiedades `content` y `timestamp`.

![Crear algunos Post y relaciones POSTED](Crear%20algunos%20Post%20y%20relaciones%20POSTED.png)  
![Crear algunos Post y relaciones POSTED 2](Crear%20algunos%20Post%20y%20relaciones%20POSTED%202.png)  
![Posted](Posted.png)

---

### Relaciones LIKES
Haz que un usuario dé “Like” a un post de otro usuario.

![Crear relaciones LIKES](Crear%20relaciones%20LIKES.png)  
![Likes](Likes.png)

---

## 🧩 Ejercicio 3: Encontrar Amigos y Seguidores

### Encontrar todos los usuarios que un usuario específico sigue
Escribe una consulta **Cypher** para encontrar todos los usuarios que ‘Alice’ (o cualquier otro) sigue.

![ejer3](ejer3.png)


---

### Encontrar todos los usuarios que siguen a un usuario específico
Escribe una consulta **Cypher** para encontrar todos los usuarios que siguen a ‘Bob’ (o cualquier otro usuario que hayas creado).

![Encontrar todos los usuarios que un usuario específico](Encontrar%20todos%20los%20usuarios%20que%20un%20usuario%20específico.png)

---

## Ejercicio 4: Analizando Posts e Interacciones

### Encontrar todos los posts de un usuario específico
Escribe una consulta **Cypher** para encontrar todos los posts de ‘Alice’ (o cualquier usuario que hayas creado), mostrando el contenido y la fecha/hora.

![ejer4](ejer4.png)

---

### Encontrar los posts que un usuario ha dado “Like”
Escribe una consulta **Cypher** para encontrar los posts a los que ‘Alice’ (o cualquier usuario que hayas creado) ha dado “Like”, mostrando el contenido del post.

![Encontrar los posts que un usuario ha dado Like](Encontrar%20los%20posts%20que%20un%20usuario%20ha%20dado%20Like.png)

---

## Ejercicio 5: Explorando el Grafo Visualmente

Ejecuta algunas de tus consultas anteriores en el **Neo4j Browser** y experimenta con las opciones de visualización:

- Arrastra nodos para reorganizar el grafo.  
  ![Arrastra nodos para reorganizar el grafo](Arrastra%20nodos%20para%20reorganizar%20el%20grafo.png)

- Haz doble clic en un nodo para expandir sus relaciones.  
  ![Haz doble clic en un nodo para expandir sus relaciones](Haz%20doble%20clic%20en%20un%20nodo%20para%20expandir%20sus%20relaciones.png)

- Usa el panel de estilos para cambiar colores y tamaños de nodos o relaciones.  
  ![Usa el panel de estilos para cambiar colores y tamaños](Usa%20el%20panel%20de%20estilos%20para%20cambiar%20colores%20y%20tamaños.png)



