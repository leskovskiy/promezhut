package promezhut;

public class Main {

    public static void main(String[] args) {

        Toys toys1 = new Toys(123,"Mishka",3,300);
        Toys toys2 = new Toys(456,"Cat",1,250);

        AllToys allToys = new AllToys();
        allToys.setToys(toys1);
        allToys.setToys(toys2);

        System.out.println("allToys.findToysByName(\"Mishka\") = " + allToys.findToysByName("Mishka"));


    }
}
