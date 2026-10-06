public class part3test {

    public static void main(String[] args) {
        testSmallMatrix();
        testIdentityMatrix();
        testZeroMatrix();
        testRectangularMatrices();
        testInvalidDimensions();
        System.out.println("All matrix multiplication tests passed.");
    }

    private static void testSmallMatrix() {

        double[][] A = {
                {1, 2},
                {3, 4}
        };

        double[][] B = {
                {5, 6},
                {7, 8}
        };

        double[][] expected = {
                {19, 22},
                {43, 50}
        };

        double[][] result = part3.multiply(A, B);

        assertMatrixEquals(expected, result);
    }


    private static void testIdentityMatrix() {

        double[][] A = {
                {1, 2},
                {3, 4}
        };

        double[][] identity = {
                {1, 0},
                {0, 1}
        };

        double[][] result =
                    part3.multiply(A, identity);

        assertMatrixEquals(A, result);
    }


    private static void testZeroMatrix() {

        double[][] A = {
                {1, 2},
                {3, 4}
        };

        double[][] zero = {
                {0, 0},
                {0, 0}
        };

        double[][] expected = {
                {0, 0},
                {0, 0}
        };

        double[][] result =
                part3.multiply(A, zero);

        assertMatrixEquals(expected, result);
    }


    private static void testRectangularMatrices() {

        double[][] A = {
                {1, 2, 3},
                {4, 5, 6}
        };

        double[][] B = {
                {7, 8},
                {9, 10},
                {11, 12}
        };

        double[][] expected = {
                {58, 64},
                {139, 154}
        };

        double[][] result =
                part3.multiply(A, B);

        assertMatrixEquals(expected, result);
    }


    private static void testInvalidDimensions() {

        double[][] A = {
                {1, 2},
                {3, 4}
        };

        double[][] B = {
                {1, 2, 3}
        };

        try {
            part3.multiply(A, B);
            throw new AssertionError("Expected an IllegalArgumentException");
        } catch (IllegalArgumentException expected) {
            // Invalid dimensions were rejected as expected.
        }
    }


    private static void assertMatrixEquals(
            double[][] expected,
            double[][] actual) {

        if (expected.length != actual.length) {
            throw new AssertionError("Matrix row counts do not match");
        }

        for (int i = 0; i < expected.length; i++) {
            if (expected[i].length != actual[i].length) {
                throw new AssertionError("Matrix column counts do not match");
            }

            for (int j = 0; j < expected[i].length; j++) {
                if (Math.abs(expected[i][j] - actual[i][j]) > 0.000001) {
                    throw new AssertionError("Matrix values do not match");
                }
            }
        }
    }
}