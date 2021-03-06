/**
 * This class represents a doubly linked node, where every node has two pointers, meant to be used in
 * the Stack class.
 * @class @public 
 */
class StackNode{
    constructor(val) {
        this.val = val;
        this.prev = null;
        this.next = null; 
    }
}

/**
 * This class represents the data structure known as a Stack, implemented using doubly linked list
 * nodes. 
 */
class Stack {
    constructor() {
        this.tail = null; 
    }

    push(val) {
        let node = new StackNode(val);
        if (this.tail) {
            this.tail.next = node;
            node.prev = this.tail;
            this.tail = node; 
        }
        else {
            this.tail = node; 
        }
    }

    pop() {
        if (this.tail) {
            let oldTailVal = this.tail.val;
            if (this.tail.prev) {
                let newTail = this.tail.prev; 
                newTail.next = null;
                this.tail = newTail;
            }
            else {
                this.tail = null;
            }
            return oldTailVal; 
        }
        else {
            throw Error("pop from empty stack");
        }
    }

    top() {
        if (this.tail) {
            return this.tail.val;
        }
        else {
            throw Error("empty stack")
        }
    }

    length() {
        let size = 0;
        let node = this.tail; 
        while (node) {
            size++;
            node = node.prev;
        }
        return size; 
    }

}

export {Stack}; 