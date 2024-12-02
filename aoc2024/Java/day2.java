import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;

public class Day2 {

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

    public boolean checkValidity(int[] arrayToCheck) {
        // Check for increasing order
        int[] increasingArray = arrayToCheck.clone();
        Arrays.sort(increasingArray);

        // Check for decreasing order
        // but the stupid Array class doesnt have reverse order sort build in so build
        // one yourself
        int[] decreasingArray = arrayToCheck.clone();
        Arrays.sort(decreasingArray);
        // doin it twice as fast, by switching symetrically
        for (int i = 0; i < decreasingArray.length / 2; i++) {
            int temp = decreasingArray[i];
            decreasingArray[i] = decreasingArray[decreasingArray.length - 1 - i];
            decreasingArray[decreasingArray.length - 1 - i] = temp;
        }

        // Check if the sorted arrays match and the difference between the numbers
        if (isValidSequence(increasingArray, arrayToCheck)) {
            return true;
        } else if (isValidSequence(decreasingArray, arrayToCheck)) {
            return true;
        }

        return false;
    }

    // Helper method to check if the sequence is valid (i.e., differences between
    // adjacent elements are within 1 to 3)
    private boolean isValidSequence(int[] sortedArray, int[] originalArray) {
        // Check if the sorted array and the original array are equal
        if (Arrays.equals(sortedArray, originalArray)) {
            // Check the differences between adjacent elements
            for (int i = 0; i < sortedArray.length - 1; i++) {
                int diff = Math.abs(sortedArray[i + 1] - sortedArray[i]);
                if (diff < 1 || diff > 3) {
                    return false; // Return false if any adjacent elements differ by less than 1 or more than 3
                }
            }
            return true; // If all differences are valid, return true
        }
        return false; // If the array is not in sorted order, return false
    }

    // Method to check if removing one level can make the report safe
    public boolean checkValidityWithOneRemoval(int[] arrayToCheck) {
        // If the original report is safe, no need to remove anything
        if (checkValidity(arrayToCheck)) {
            return true;
        }

        // Try removing each element and check if the resulting array is valid
        for (int i = 0; i < arrayToCheck.length; i++) {
            // Create a new array without the i-th element
            int[] newArray = new int[arrayToCheck.length - 1];
            int index = 0;
            for (int j = 0; j < arrayToCheck.length; j++) {
                if (j != i) {
                    newArray[index++] = arrayToCheck[j];
                }
            }

            if (checkValidity(newArray)) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        Day2 day2 = new Day2();
        String fileName = "/Users/Stijn/OneDrive - KU Leuven/PERSONAL/Rommel/AocFiles/aoc2024/java/input.txt";
        ArrayList<int[]> data = readFileToArray(fileName);
        int count = 0;

        for (int[] arr : data) {
            if (day2.checkValidityWithOneRemoval(arr)) {
                count++;
            }
        }

        System.out.println(count);
    }

}
