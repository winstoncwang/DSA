package Exercise.Classes;

public class Main {
    public static void main(String[] args) {
        Cookie cOne = new Cookie("green");
        Cookie cTwo = new Cookie("blue");

        cOne.setColor("yellow");

        System.out.println(cOne.getColor());
        System.out.println(cTwo.getColor());
    }
}
