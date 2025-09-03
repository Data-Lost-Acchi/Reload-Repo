class Pet {
    String name;

    Pet(String name) {
        this.name = name;
    }

    void introduce() {
        System.out.println("This Pet's name is " + this.name);
    }
}

// Created Pet Class, U can now create objects of the pet class
// for example -> Pet John = new Pet("John"); now there is an object called John of the pet class, the pet's name that we set is John

// Now we will try inheritance
class Dog extends Pet {
    Dog(String name) {
        super(name);
    }

    void bark() {
        System.out.println("bark");
    }
}

// Now we can create Dogs
// The dogs have inherited the functions and variables from pet class
// like you have to name the object of dogs as well
// we will now try to create a Dog

public class Main {
    public static void main(String[] args) {
        Dog Johnny = new Dog("Johnny");
        Johnny.bark();
        Johnny.introduce();

        // Lets create Cats as well
        class Cat extends Pet {
            Cat(String name) {
                super(name);
            }

            @Override
            void introduce() {
                System.out.println("This is a cat, its name is " + this.name);
            }

            void meow() {
                System.out.println("Meow");
            }
        }

        // We have now created cats
        // note however as you see that the introduce function already exists in pet class
        // so if we want to change the introduce function only for cats
        // we can set another introduce function
        // so now for every cat, if we introduce it, the standard pet introduce function has been overwritten by our new function
        // it will follow our function
        // lets create a cat

        Cat Meowsy = new Cat("Meowsy");
        Meowsy.introduce();
        Meowsy.meow();
    }
}
// you have learnt the basics of OOP in java , however you still have more to learn
