import java.io.*;

public class part4 {

    public static void main(String[] args) throws IOException {

        // Create a 7x7 matrix
        int n = 7;
        int[][] A = new int[n][n];

        // Fill the matrix with numbers 1 to 49
        int number = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                A[i][j] = number;
                number++;
            }
        }

        // Print original matrix
        System.out.println("# original");
        printMatrix(A);

        // A[::2, ::2]

        int size = (n + 1) / 2;
        int[][] slice1 = new int[size][size];

        int row = 0;

        for (int i = 0; i < n; i += 2) {

            int col = 0;

            for (int j = 0; j < n; j += 2) {
                slice1[row][col] = A[i][j];
                col++;
            }

            row++;
        }

        System.out.println("# A[::2, ::2]:");
        printMatrix(slice1);

        // A[::-1, ::-1]

        int[][] slice2 = new int[n][n];

        for (int i = 0; i < n; i++) {

            for (int j = 0; j < n; j++) {

                // Take elements from the end
                slice2[i][j] = A[n - 1 - i][n - 1 - j];
            }
        }

        System.out.println("# A[::-1, ::-1]:");
        printMatrix(slice2);


        // Save results to a file
        try (PrintWriter file = new PrintWriter("Part4/code/text/java_out.txt")) {

            file.println("Original matrix:");
            writeMatrix(file, A);

            file.println("#A[::2, ::2]:");
            writeMatrix(file, slice1);

            file.println("#A[::-1, ::-1]:");
            writeMatrix(file, slice2);
        }

        System.out.println("\nResults saved to text/java_out.txt");
    }


    // Function to print a matrix
    static void printMatrix(int[][] matrix) {

        for (int i = 0; i < matrix.length; i++) {

            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + "\t");
            }

            System.out.println();
        }
    }


    // Function to write a matrix to a file
    static void writeMatrix(PrintWriter file, int[][] matrix) {

        for (int i = 0; i < matrix.length; i++) {

            for (int j = 0; j < matrix[i].length; j++) {

                if (j > 0) {
                    file.print(",");
                }

                file.print(matrix[i][j]);
            }

            file.println();
        }
    }
}
