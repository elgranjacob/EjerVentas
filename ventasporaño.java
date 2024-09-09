import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ventasporaño {
    // Atributos para almacenar los departamentos, ventas y meses
    private List<String> departamentos;
    private List<List<Integer>> ventas;
    private List<String> meses;

    // Constructor para inicializar los datos
    public ventasporaño() {
        this.departamentos = Arrays.asList("Ropa", "Deportes", "Juguetes");
        this.ventas = new ArrayList<>();
        for (int i = 0; i < departamentos.size(); i++) {
            ventas.add(new ArrayList<>());
        }
        this.meses = Arrays.asList("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre");
    }

    // Método para insertar las ventas en un departamento
    public void insertarVentas(String departamento, List<Integer> ventasMensuales) {
        if (departamentos.contains(departamento)) {
            int indice = departamentos.indexOf(departamento);
            if (ventasMensuales.size() == 12) {
                ventas.set(indice, ventasMensuales);
                System.out.println("Ventas para " + departamento + " han sido actualizadas.");
            } else {
                System.out.println("Debe proporcionar ventas para los 12 meses.");
            }
        } else {
            System.out.println("Departamento no encontrado.");
        }
    }

    // Método para buscar ventas de un mes en particular para todos los departamentos
    public void buscarVentasPorMes(String mes) {
        if (meses.contains(mes)) {
            int indiceMes = meses.indexOf(mes);
            System.out.println("Ventas en " + mes + ":");
            for (int i = 0; i < departamentos.size(); i++) {
                System.out.println(departamentos.get(i) + ": " + ventas.get(i).get(indiceMes));
            }
        } else {
            System.out.println("Mes no encontrado.");
        }
    }

    // Método para eliminar los datos de un departamento en particular
    public void eliminarVentasDepartamento(String departamento) {
        if (departamentos.contains(departamento)) {
            int indice = departamentos.indexOf(departamento);
            ventas.set(indice, new ArrayList<>());
            System.out.println("Datos de ventas para " + departamento + " han sido eliminados.");
        } else {
            System.out.println("Departamento no encontrado.");
        }
    }

    // Método para mostrar todas las ventas de todos los departamentos
    public void mostrarVentas() {
        System.out.printf("%-12s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s %-8s%n",
                "Departamento", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Sept", "Oct", "Nov", "Dic");
        for (int i = 0; i < departamentos.size(); i++) {
            if (!ventas.get(i).isEmpty()) {
                System.out.printf("%-12s ", departamentos.get(i));
                for (int j = 0; j < 12; j++) {
                    System.out.printf("%-8d ", ventas.get(i).get(j));
                }
                System.out.println();
            } else {
                System.out.printf("%-12s %-8s%n", departamentos.get(i), "Sin datos");
            }
        }
    }

    public static void main(String[] args) {
        // Crear una instancia de la clase
        ventasporaño ventas = new ventasporaño();

        // Insertar ventas por departamento
        ventas.insertarVentas("Ropa", Arrays.asList(500, 600, 550, 700, 750, 800, 900, 850, 1000, 1100, 950, 1200));
        ventas.insertarVentas("Deportes", Arrays.asList(300, 400, 350, 500, 550, 600, 700, 750, 800, 850, 900, 950));
        ventas.insertarVentas("Juguetes", Arrays.asList(200, 300, 250, 400, 450, 500, 600, 650, 700, 750, 800, 850));

        // Mostrar ventas
        ventas.mostrarVentas();

        // Buscar ventas para un mes en particular
        ventas.buscarVentasPorMes("Marzo");

        // Eliminar las ventas de un departamento
        ventas.eliminarVentasDepartamento("Juguetes");

        // Mostrar ventas nuevamente para ver los cambios
        ventas.mostrarVentas();
    }
}

