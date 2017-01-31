Anita is the baby sitter of Baron Von Hauser’s kids. Von Hauser is a famous physics professor, so the Von Hauser kids have weird toys, all of which Anita has to master to be able to effectively entertain the kids.
While Anita was cleaning the bathtub she found a new toy, a Squarelotron game. It is extremely weird, and posses a lot of mathematical symmetry. She is determined to understand this new toy, otherwise she won´t be able to play with Von Hauser’s kids. However the complexity of such an extreme toy makes it difficult to play.

A Squarelotron consist basically of a matrix of numbers. This matrix can be decomposed as square rings which can rotate independently in 4 different ways: Upside-Down (↕), Left-Right (↔), reflected through the Inverse Diagonal ( / ), and reflected through the Main Diagonal ( \ ) . As a puzzle, the object of the squarelotron is to take one that is scrambled, and return it to its original state. Here's what the original state looks like:
	
<img src="http://www.cis.upenn.edu/~matuszek/cit590-2016/Images/SquarelotronImages/initial_squarelotron.jpg">

The green line shows the main diagonal.
Flipping the outer ring through the main
diagonal means interchanging 2 and 6,
3 and 11, ..., 20 and 24.

The inverse diagonal would be a line
running through 5, 9, 19, 17, and 21. The squarelotron has two rings and a center piece. The outer ring contains the numbers 1, 2, 3, 4, 5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24, 25, while the inner ring contains 7, 8, 9, 12, 14, 17, 18, 19. The number 13 is by itself in the center.
The following are examples of flips. They are not cumulative; each flip is shown as being from the initial state.

A Upside-Down Flip of the outer ring of the squarelotron yields:

<img src="http://www.cis.upenn.edu/~matuszek/cit590-2016/Images/SquarelotronImages/outer-upside-down.jpg">

A Left-Right Flip of the inner ring of the squarelotron yields:

<img src="http://www.cis.upenn.edu/~matuszek/cit590-2016/Images/SquarelotronImages/left-right-inner.gif">

A Flip through the Main Diagonal of the outer ring of the squarelotron yields:

<img src="http://www.cis.upenn.edu/~matuszek/cit590-2016/Images/SquarelotronImages/p10016e.gif">

An Inverse Diagonal flip of the inner ring yields:

<img src="http://www.cis.upenn.edu/~matuszek/cit590-2016/Images/SquarelotronImages/inner-inverse-diagonal.jpg">

Anita wants you to do a program which performs the following. It will print out the initial squarelotron. Then the program will let you tell it which flips to perform, and it will print out the new squarelotron after each flip. Finally, the program will let you start with a new squarelotron, or quit.
