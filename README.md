# AccuKnozAssignment
### Topic: Django Signals
Q1) By default are django signals executed synchronously or asynchronously?

ANS) By default, Django signals run synchronously. When a signal is emitted, associated handlers (receivers) are run right away in the same process and thread as the caller.
Description of how the code works:
When User.objects.create() is invoked, Django stores the new User object in the database.
Once the save operation has been completed, the post_save signal is emitted. The function my_signal_handler is called because now this function is attached to the post_save signal on the user model.
The handler prints "Signal received.", delays by 5 seconds, and then prints "Signal processing complete.".
Lastly, the print("User is created.") instruction is run.

When you run this code, the output will look like this:
```bash
Signal received.
Signal processing complete.
User created.
```
The signal handler runs synchronously, so the print("User created.") statement waits until the signal processing is complete.

Q2)Do django signals run in the same thread as the caller?

ANS)Yes, Django signals execute in the same thread as the caller by default. Signal handlers are run in the same thread that is sending the signal.
How It Works
The - print(f"Main thread: {threading.current_thread().name}") - line executes in the main thread and prints something like:
```bash
MainThread
Main thread: MainThread
```
When calling User.objects.create(), Django persists the new User object to the database. After saving, the post_save signal is sent.
The my_signal_handler function is called because it is bound to the post_save signal for the User model. The handler prints the name of the thread that it is running in. 
Because Django signals run synchronously by default, this will also be the main thread:
```bash
Signal running in thread: MainThread
```

Q3)By default do django signals run in the same database transaction as the caller?

ANS) By default, Django signals run in the same database transaction as the caller. If the caller is inside a transaction, the signal handlers will also execute within that transaction.
How the code works:
transaction.atomic() guarantees the block within it executes as an atomic transaction. In case something goes wrong, all operations within this block get rolled back.
Django Signals (post_save) sends a signal to the signal recipients after saving an object to the database.
In this case, my_signal_handler receives post_save signals on the User model.
To check if signals run inside transactions , transaction.get_connection().in_atomic_block is used. It indicates whether the immediate code is operating within a transaction.
If True, it ensures that Django signals run under the same database transaction.

Expected Output:
```bash
Inside transaction: True
Signal received inside transaction: True
```
### Topic: Custom Classes in Python

To design a Rectangle class that satisfies the requirements, we must make sure the following is accomplished:<br>
1. The class must be initialized with length and width as int attributes.<br>
2. The class must be iterable, that is, it must be possible to loop over an instance of the class.<br>
3. When iterating over the class, the class must first yield the length in the form {'length': <VALUE_OF_LENGTH>} and afterwards the width in the form {'width': <VALUE_OF_WIDTH>}.
Explanation of code:<br>
Initialization (__init__):<br>
The Rectangle class is constructed with length and width as mandatory.<br>
A private property _iter_index is employed to store the iteration status.<br>

Iteration Protocol (__iter__ and __next__):<br>
The __iter__ function resets the iteration index and returns the instance itself.<br>
The __next__ function yields the length and width in the required format. Once both have been yielded, it raises StopIteration to indicate end of iteration.

Example:<br>
When you iterate over an instance of Rectangle, it yields the length first and then the width in the desired dictionary format.

Output:<br>
For the above example used in code, the output will be:
```bash
{'length': 10}
{'width': 5}
```
