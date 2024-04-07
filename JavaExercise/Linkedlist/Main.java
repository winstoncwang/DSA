package Exercise.Linkedlist;

public class Main {
    public static void main(String[] args) {
        LinkedList newLinkedList = new LinkedList(4);
        newLinkedList.append(7);
        newLinkedList.append(9);
        newLinkedList.append(11);
        newLinkedList.prepend(2);

        newLinkedList.printList();
        newLinkedList.getHead();
        newLinkedList.getTail();
        newLinkedList.getLength();
        System.out.println("-------------");


    }
}
