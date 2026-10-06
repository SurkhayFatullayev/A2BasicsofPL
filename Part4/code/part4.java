import java.io.*;

public class part4 {

    public static void main(String[] args) throws IOException {

        int n = 7;
        int[][] A = new int[n][n];

        // Fill matrix with 1 to 49
        int number = 1;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                A[i][j] = number++;

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

        // A[::-1, ::-1]
        int[][] slice2 = new int[n][n];

        for (int i = 0; i < n; i++) {
            
            for (int j = 0; j < n; j++) {

                // Take elements from the end
                slice2[i][j] = A[n - 1 - i][n - 1 - j];
            }
        
        }

        // Write JSON
        try (PrintWriter file = new PrintWriter("Part4/code/text/java_out.json")) {
            file.print("{");
            writeJsonEntry(file, "original", A, false);
            writeJsonEntry(file, "A[::2, ::2]", slice1, false);
            writeJsonEntry(file, "A[::-1, ::-1]", slice2, true);
            file.println("}");
        }

        System.out.println("Results saved to java_out.json");
    }

    static void writeJsonEntry(
            PrintWriter file,
            String name,
            int[][] matrix,
            boolean last) {
        file.print("\"" + name + "\":[");

        for (int i = 0; i < matrix.length; i++) {
            if (i > 0)
                file.print(",");

            file.print("[");
            for (int j = 0; j < matrix[i].length; j++) {
                if (j > 0)
                    file.print(",");
                file.print(matrix[i][j]);
            }
            file.print("]");
        }

        file.print("]");
        if (!last)
            file.print(",");
    }
}