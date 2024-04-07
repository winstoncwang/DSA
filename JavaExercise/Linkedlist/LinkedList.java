package Exercise.Linkedlist;

public class LinkedList {
    private Node head;
    private Node tail;
    private int length;

    class Node {
        int value;
        Node next;
        public Node (int value) {
            this.value = value;
        }
    }

    public LinkedList (int value) {
        Node newNode = new Node(value);
        head = newNode;
        tail = newNode;
        length = 1;
    }

    public void printList() {
        Node tmp = head;
        while (tmp != null) {
            System.out.println(tmp.value);
            tmp = tmp.next;
        }
    }

    public void getHead() {
        System.out.println("HEAD: " + head.value);
    }

    public void getTail() {
        System.out.println("TAIL: " + tail.value);
    }

    public void getLength() {
        System.out.println("Length: " + length);
    }

    public void append (int value) {
        Node newNode = new Node(value);
        // consider when LL is empty
        if (length == 0) {
            head = newNode;
        } else {
            tail.next = newNode;
        }
        tail = newNode;
        length ++;
    }

    public Node removeLast () {
        Node tmp = head;
        Node pre = head;
        if (length == 0) return null;
        while(tmp.next != null) {
            pre = tmp;
            tmp = tmp.next;
        }
        tail = pre;
        tail.next = null;
        length --;
        // check length again, if 0 assign to null for the length == 1 edge case
        if (length == 0) {
            head = null;
            tail = null;
        }
        return tmp;
    }

    public void prepend (int value) {
        Node newNode = new Node (value);
        if (length == 0) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
        length++;
    }
}
