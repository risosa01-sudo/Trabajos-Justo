import boto3

# 1. Crear un recurso de servicio de DynamoDB
# Reemplaza 'us-east-1' con la región que estés utilizando
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# 2. Seleccionar la tabla 'Orders'
table = dynamodb.Table('Orders')

# 3. Imprimir un mensaje de confirmación
print(f"Conectado a la tabla '{table.name}' en la región '{dynamodb.meta.client.meta.region_name}'.")




# 1 Llamada

def create_order(order_id, customer_name, product, quantity, status):
    """Crea un nuevo ítem en la tabla Orders."""
    try:
        response = table.put_item(
           Item={
                'order_id': order_id,
                'customer_name': customer_name,
                'product': product,
                'quantity': quantity,
                'status': status,
                'order_date': '2025-11-10' # Puedes usar una fecha actual
            }
        )
        print(f"Pedido {order_id} creado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al crear el pedido: {e}")




# 2 Busqueda

def get_order(order_id):
    """Obtiene un ítem de la tabla Orders por su ID."""
    try:
        response = table.get_item(Key={'order_id': order_id})
        item = response.get('Item')
        if item:
            print(f"Datos del pedido {order_id}: {item}")
            return item
        else:
            print(f"No se encontró el pedido con ID {order_id}.")
            return None
    except Exception as e:
        print(f"Error al obtener el pedido: {e}")




# 3. Modificar los datos

def update_order_status(order_id, new_status):
    """Actualiza el atributo 'status' de un pedido."""
    try:
        response = table.update_item(
            Key={'order_id': order_id},
            UpdateExpression="set #st = :s",
            ExpressionAttributeNames={'#st': 'status'},
            ExpressionAttributeValues={':s': new_status},
            ReturnValues="UPDATED_NEW"
        )
        print(f"Estado del pedido {order_id} actualizado a '{new_status}'.")
        return response
    except Exception as e:
        print(f"Error al actualizar el pedido: {e}")



# 5. Eliminar datos

def delete_order(order_id):
    """Elimina un item de la tabla Orders."""
    try:
        response = table.delete_item(Key={'order_id': order_id})
        print(f"Pedido {order_id} eliminado exitosamente.")
        return response
    except Exception as e:
        print(f"Error al eliminar el pedido: {e}")



# 6. Busqueda de clientes
from boto3.dynamodb.conditions import Attr

def get_orders_by_customer(customer_name, table):
    """Devuelve todos los pedidos realizados por un cliente concreto."""
    try:
        response = table.scan(
            FilterExpression=Attr('customer_name').eq(customer_name)
        )

        orders = response.get('Items', [])

        if orders:
            print(f"Pedidos encontrados para el cliente '{customer_name}':")
            for order in orders:
                print(f"- ID: {order['order_id']}, Producto: {order['product']}, "
                      f"Cantidad: {order['quantity']}, Estado: {order['status']}")
        else:
            print(f"No se encontraron pedidos para el cliente '{customer_name}'.")

        return orders

    except Exception as e:
        print(f"Error al obtener pedidos: {e}")
        return []





if __name__ == "__main__":
    print("--- Demostración de operaciones con DynamoDB ---")

    # 1 Llamada de ejemplo
    create_order(order_id="10", customer_name="Rafa", product="C3", quantity=30, status="Sin pagar")

    # 2 Busqueda de ejemplo
    get_order("12")

    # 3. Modificar los datos
    update_order_status("12", "Pagado")

    # 4. # Busqueda de clientes
    get_orders_by_customer("Rafa", table)

    # 5. Eliminar datos
    delete_order("12")

    print("\n--- Demostración finalizada ---")