import {Heap} from "../../data structures/Heap.js";


test('test minheap', () => {
    let obj1 = new Heap();
    let array = [9,3,1,2,5,7];
    obj1.heapify(array);
    console.log(array);
    expect(array).toStrictEqual([1,2,7,3,5,9]);

    obj1.remove(array);
    expect(obj1.peek(array)).toStrictEqual(2);

    obj1.insert(array, -10);
    expect(obj1.peek(array)).toStrictEqual(-10);
});


test('test 2', () => {
    let obj1 = new Heap(null, 1);
    let array = [9,3,1,2,5,7];
    obj1.heapify(array);

    console.log(array);

    expect(array).toStrictEqual([9,5,7,2,3,1]);

    obj1.remove(array);
    expect(obj1.peek(array)).toStrictEqual(7);

    obj1.insert(array, 100);
    expect(obj1.peek(array)).toStrictEqual(100);
});
