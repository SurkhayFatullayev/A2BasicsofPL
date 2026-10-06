public class part3 {

    public static void main(String[] args) {
        int[] matrixSizes = {100, 200, 500};

        for (int size : matrixSizes) {
            System.out.println("---------------------------------------------------");
            System.out.println("Testing matrix with size: " + size );

            double[][] A = createMatrix(size);
            double[][] B = createMatrix(size);

            long start = System.nanoTime();
            multiply(A, B);
            long end = System.nanoTime();

            System.out.println(
                    size + "x" + size + " matrix execution time: "
                            + (end - start) / 1000000.0 + " ms"
            );
        }
    }

    private static double[][] createMatrix(int size) {
        double[][] matrix = new double[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                matrix[i][j] = i + j;
            }
        }

        return matrix;
    }

    public static double[][] multiply(double[][] A, double[][] B) {

        int rowsA = A.length;
        int colsA = A[0].length;

        int rowsB = B.length;
        int colsB = B[0].length;

        if (colsA != rowsB) {
            throw new IllegalArgumentException(
                    "Wrong dimensions"
            );
        }

        double[][] C = new double[rowsA][colsB];

        for (int i = 0; i < rowsA; i++) {
            for (int j = 0; j < colsB; j++) {
                for (int k = 0; k < colsA; k++) {
                    C[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return C;
    }
}
