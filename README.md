## Flash Card Project
__If your goal is to learn a foreign language while taking it easy, this app is for you.__  

As the name suggests, we have a card represented by a 
canvas object, on one side with a word in the language to be learned (and its name - Spanish, in this case), and on 
the other side the translation of the word in the known language.   
 
There are also two buttons to press, one if the word that appears is already memorized and will be removed from the list of words 
to learn, and the other if the word needs to appear a few more times to be assimilated.
Other details:
* The Graphical User Interface was created with __tkinter__ package.
* The list of words and their translation is read from a csv file, using __pandas__ library, and are displayed randomly on the card. 
* The waiting time until the card is flipped is 3 seconds.
  * Timer is disabled if the next card is called before the time runs out