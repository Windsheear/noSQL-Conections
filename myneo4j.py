from neo4j import GraphDatabase

uri = "neo4j+s://4d6d8fe6.databases.neo4j.io"  # Ajusta esto a la URI de tu instancia de Neo4j
username = "neo4j"  # El usuario por defecto suele ser 'neo4j'
password = "rd_sXN_3_A6zbt4ijberAXVqSjzSNOu469N492EE-18"  # Reemplaza esto con tu contraseña real

# Crear una instancia del driver de Neo4j
driver = GraphDatabase.driver(uri, auth=(username, password))
driver.verify_connectivity()

def create_node_with_role(tx, name, role):
    # Crear un nodo en Neo4j con un rol
    tx.run("CREATE (:Person {name: $name, role: $role})", name=name, role=role)

def get_nodes(tx):
    # Obtener todos los nodos de tipo 'Person'
    result = tx.run("MATCH (n:Person) RETURN n.name AS name")
    return [record["name"] for record in result]

def create_director_relationship(tx, director_name, employee_name):
    # Crear una relación donde una persona es el director de otra
    tx.run("""
    MATCH (director:Person {name: $director_name}), (employee:Person {name: $employee_name})
    CREATE (director)-[:DIRECTS]->(employee)
    """, director_name=director_name, employee_name=employee_name)

def delete_node(tx, name):
    # Eliminar un nodo en Neo4j
    tx.run("MATCH (n:Person {name: $name}) DETACH DELETE n", name=name)

def update_node_info(tx, name, new_role):
    # Actualizar la información de un nodo en Neo4j
    tx.run("MATCH (n:Person {name: $name}) SET n.role = $new_role", name=name, new_role=new_role)



# Usar el driver para ejecutar funciones
with driver.session() as session:
    
    session.execute_write(update_node_info, "Alice", "Manager")
    nodes = session.execute_read(get_nodes)
    print(nodes)

# Cerrar el driver
session.close()
driver.close()
