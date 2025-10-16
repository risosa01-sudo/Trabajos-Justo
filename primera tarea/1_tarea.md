#  Práctica MongoDB – Consultas con find()

##  Ejercicio 1: Encontrar portátiles de una marca con más de 8GB de RAM

**Objetivo:**  
Obtener todos los productos cuya categoría sea **"Portátiles"**, que pertenezcan a la marca **TecnoÁgora Devices** y cuya memoria RAM sea superior a **8GB**.

---

### Datos de ejemplo

```js
db.productos.insertMany([
  {
    _id: "SKU-001",
    nombre: "TecnoBook Pro 14",
    categoria: "Portátiles",
    marca: "TecnoÁgora Devices",
    especificaciones: {
      procesador: "Intel i7",
      ram: 16,
      almacenamiento: "512GB SSD"
    },
    precio: 1200,
    stock: 8,
    tags: ["nuevo", "oferta", "gama-alta"],
    reviews: [
      { usuario: "Laura", puntuacion: 5, comentario: "Excelente rendimiento y diseño." },
      { usuario: "Carlos", puntuacion: 4, comentario: "Muy rápido, pero algo caro." }
    ]
  },
  {
    _id: "SKU-002",
    nombre: "Portátil Pro-Book X1",
    categoria: "Portátiles",
    marca: "TecnoÁgora Devices",
    especificaciones: {
      procesador: "Intel i5",
      ram: 8,
      almacenamiento: "256GB SSD"
    },
    precio: 900,
    stock: 3,
    tags: ["oferta", "ligero"],
    reviews: [
      { usuario: "Ana", puntuacion: 3, comentario: "Cumple, pero se calienta un poco." },
      { usuario: "Mario", puntuacion: 4, comentario: "Buen portátil para trabajar." }
    ]
  },
  {
    _id: "SKU-003",
    nombre: "GigaNote X15",
    categoria: "Portátiles",
    marca: "GigaTech",
    especificaciones: {
      procesador: "AMD Ryzen 7",
      ram: 16,
      almacenamiento: "1TB SSD"
    },
    precio: 1100,
    stock: 10,
    tags: ["profesional", "rendimiento"],
    reviews: [
      { usuario: "Luis", puntuacion: 5, comentario: "Excelente calidad-precio." }
    ]
  },
  {
    _id: "SKU-004",
    nombre: "TecnoPad 11",
    categoria: "Tablets",
    marca: "TecnoÁgora Devices",
    especificaciones: {
      procesador: "ARM A12",
      ram: 6,
      almacenamiento: "128GB"
    },
    precio: 400,
    stock: 15,
    tags: ["portátil", "ligero"],
    reviews: [
      { usuario: "Sofía", puntuacion: 4, comentario: "Ideal para estudiar." }
    ]
  },
  {
    _id: "SKU-005",
    nombre: "SmartVision TV 50",
    categoria: "Televisores",
    marca: "VisuTech",
    especificaciones: {
      resolucion: "4K",
      ram: 4,
      almacenamiento: "16GB"
    },
    precio: 750,
    stock: 2,
    tags: ["oferta", "smart-tv"],
    reviews: [
      { usuario: "Héctor", puntuacion: 2, comentario: "Buena imagen, pero lento." }
    ]
  },
  {
    _id: "SKU-006",
    nombre: "TecnoBook Max 15",
    categoria: "Portátiles",
    marca: "TecnoÁgora Devices",
    especificaciones: {
      procesador: "Intel i9",
      ram: 32,
      almacenamiento: "1TB SSD"
    },
    precio: 1800,
    stock: 6,
    tags: ["premium", "nuevo"],
    reviews: [
      { usuario: "Daniela", puntuacion: 5, comentario: "Una bestia en potencia." },
      { usuario: "Ernesto", puntuacion: 5, comentario: "Perfecto para diseño y edición." }
    ]
  }
]);


## Imagen de búsqueda de RAM

A continuación se muestra una imagen ilustrativa de la consulta para encontrar portátiles con más de 8GB de RAM:

![Búsqueda de RAM](img_busqueda_ram.png)




##  Ejercicio 2: Buscar productos con la etiqueta “oferta”




##  Ejercicio 3: Incrementar el stock de un producto en 10 unidades



##  Ejercicio 4: Añadir una nueva reseña (review) a un producto


## Parte 4: Ejercicios adicionales (opcional)


