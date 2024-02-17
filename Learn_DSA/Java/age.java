package Java;

import java.util.Scanner;

public class age {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Please enter your age :\n");
        int age = sc.nextInt();

        if (age > 2 || age <= 15) {
            if (age >= 1 && age < 5) {
                System.out.println("You are a toddler");
            } else if (age > 5 && age <= 10) {
                System.out.println("You are in School Age");
            } else {
                System.out.println("You are not a child");
            }
        } else if (age > 15 && age <= 18) {
            System.out.println("You are in teenage");
        } else {
            System.out.println("You are an adult");
        }
        sc.close();
    }
}
