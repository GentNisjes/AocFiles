import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class day2 {

    public static ArrayList<int[]> readFileToArray(String fileName) {
        ArrayList<int[]> data = new ArrayList<>();

        try (Scanner sc = new Scanner(new File(fileName))) {
            while (sc.hasNextLine()) {
                String line = sc.nextLine();
                // Split the line into strings by spaces
                String[] tokens = line.split("\\s+");

                // Convert the strings to integers and store them in a subarray
                int[] subArray = new int[tokens.length];
                for (int i = 0; i < tokens.length; i++) {
                    subArray[i] = Integer.parseInt(tokens[i]);
                }

                // Add the subarray to the main array
                data.add(subArray);
            }
        } catch (FileNotFoundException fnfe) {
            System.out.println("File not found: " + fileName);
            return null;
        } catch (NumberFormatException nfe) {
            System.out.println("Invalid number format in the file.");
            return null;
        }

        return data;
    }

    public static void main(String[] args) {
        String fileName = "input.txt"; // Specify the file name
        ArrayList<int[]> data = readFileToArray(fileName);

        // Print the content of the main array
        if (data != null) {
            for (int[] subArray : data) {
                for (int num : subArray) {
                    System.out.print(num + " ");
                }
                System.out.println();
            }
        }
    }

}
