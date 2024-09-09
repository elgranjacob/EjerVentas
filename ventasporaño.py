# Datos de ventas por mes para cada departamento
ventas = [
    [500, 600, 550, 700, 750, 800, 900, 850, 1000, 1100, 950, 1200],  # Ventas de ropa por mes
    [300, 400, 350, 500, 550, 600, 700, 750, 800, 850, 900, 950],     # Ventas de deportes por mes
    [200, 300, 250, 400, 450, 500, 600, 650, 700, 750, 800, 850]      # Ventas de juguetes por mes
]

# Nombres de los departamentos y meses
departamentos = ['Ropa', 'Deportes', 'Juguetes']
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

# Imprimir la tabla de ventas por departamento y mes
print(f"{'Departamento':<12} {'Enero':<8} {'Febrero':<8} {'Marzo':<8} {'Abril':<8} {'Mayo':<8} {'Junio':<8} {'Julio':<8} {'Agosto':<8} {'Sept':<8} {'Oct':<8} {'Nov':<8} {'Dic':<8}")

# Iterar sobre los departamentos y mostrar sus ventas por mes
for i in range(len(departamentos)):
    print(f"{departamentos[i]:<12} ", end="")
    for j in range(12):
        print(f"{ventas[i][j]:<8} ", end="")
    print()  # Nueva línea al finalizar cada departamento

class VentasDepartamentos:
    def __init__(self):
        # Inicializar ventas vacías para ropa, deportes y juguetes
        self.departamentos = ['Ropa', 'Deportes', 'Juguetes']
        self.ventas = [
            [],  # Ventas de ropa
            [],  # Ventas de deportes
            [],  # Ventas de juguetes
        ]
        self.meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    # Método para insertar las ventas en un departamento
    def insertar_ventas(self, departamento, ventas_mensuales):
        if departamento in self.departamentos:
            indice = self.departamentos.index(departamento)
            if len(ventas_mensuales) == 12:
                self.ventas[indice] = ventas_mensuales
                print(f"Ventas para {departamento} han sido actualizadas.")
            else:
                print("Debe proporcionar ventas para los 12 meses.")
        else:
            print("Departamento no encontrado.")
    
    # Método para buscar ventas de un mes en particular para todos los departamentos
    def buscar_ventas_por_mes(self, mes):
        if mes in self.meses:
            indice_mes = self.meses.index(mes)
            print(f"Ventas en {mes}:")
            for i, departamento in enumerate(self.departamentos):
                print(f"{departamento}: {self.ventas[i][indice_mes]}")
        else:
            print("Mes no encontrado.")

    # Método para eliminar los datos de un departamento en particular
    def eliminar_ventas_departamento(self, departamento):
        if departamento in self.departamentos:
            indice = self.departamentos.index(departamento)
            self.ventas[indice] = []
            print(f"Datos de ventas para {departamento} han sido eliminados.")
        else:
            print("Departamento no encontrado.")
    
    # Método para mostrar todas las ventas de todos los departamentos
    def mostrar_ventas(self):
        print(f"{'Departamento':<12} {'Enero':<8} {'Febrero':<8} {'Marzo':<8} {'Abril':<8} {'Mayo':<8} {'Junio':<8} {'Julio':<8} {'Agosto':<8} {'Sept':<8} {'Oct':<8} {'Nov':<8} {'Dic':<8}")
        for i, departamento in enumerate(self.departamentos):
            if self.ventas[i]:
                print(f"{departamento:<12} ", end="")
                for j in range(12):
                    print(f"{self.ventas[i][j]:<8} ", end="")
                print()  # Nueva línea al finalizar cada departamento
            else:
                print(f"{departamento:<12} {'Sin datos':<8}")

# Crear una instancia de la clase
ventas = VentasDepartamentos()

# Insertar ventas por departamento
ventas.insertar_ventas('Ropa', [500, 600, 550, 700, 750, 800, 900, 850, 1000, 1100, 950, 1200])
ventas.insertar_ventas('Deportes', [300, 400, 350, 500, 550, 600, 700, 750, 800, 850, 900, 950])
ventas.insertar_ventas('Juguetes', [200, 300, 250, 400, 450, 500, 600, 650, 700, 750, 800, 850])

# Mostrar ventas
ventas.mostrar_ventas()

# Buscar ventas para un mes en particular
ventas.buscar_ventas_por_mes('Marzo')

# Eliminar las ventas de un departamento
ventas.eliminar_ventas_departamento('Juguetes')

# Mostrar ventas nuevamente para ver los cambios
ventas.mostrar_ventas()


    

