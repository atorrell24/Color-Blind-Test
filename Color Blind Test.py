import tkinter
from tkinter import *
Redgreen = ['Deuteranomaly', 'Protanomaly', 'Protanopia', 'Deuteranopia']

print('This is a colorblind test, please answer all questions to the best of your ability. Once a number pops up and you have looked at it, please exit to proceed.');

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 489)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara1.PNG')#add the file location to where it says file location
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()

while True:
    try:
        tally = 0;
        firstquestion = int(input('What is the number that you see?'));
        if firstquestion == 8:
            print('Goodjob! You got it correct. PLease move on to the next question');
            tally += 1;
            break
        elif firstquestion != 8:
            print('You entered the wrong number, please move on to the next question.')
            break

    except ValueError:
        print('Invalid input, please enter a valid number');
   

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara2.PNG')#add the file location to where it says file location
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()

while True:
    try:
        secondquestion = int(input('What number do you see?'));
        if secondquestion == 6:
            print('Congrats! Please move on to the next question');
            tally += 1;
            break
        elif secondquestion !=6:
            print('You entered the wrong number, please go to the next question');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=512, height = 489)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara3.PNG')
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()
while True:
    try:
        thirdquestion = int(input('What number does this image read?'));
        if thirdquestion == 29:
            print('Correct!');
            tally += 1;
            break
        elif thirdquestion != 29:
            print('Unfortunately, the answer you have provided was incorrect. ');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')


window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 537)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara4.PNG')
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()

while True:
        try:
            fourthquestion = int(input('What number does this image read?'));
            if fourthquestion == 57:
                print('Correct!');
                tally += 1;
                break
            elif fourthquestion !=57:
                print('Unfortunately, the answer you have provided was incorrect. ');
                break
        except ValueError:
            print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara5.PNG')
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()
while True:
    try:
        fifthquestion = int(input('What number does this image read?'));
        if fifthquestion == 5:
            print('Correct!');
            tally += 1;
            break
        elif fifthquestion!= 5:
            print('Sorry, the answer you have provided was incorrect. ');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara6.PNG')
window. create_image(0,0, anchor = NW, image = image)

window.mainloop()
while True:
    try:
        sixthquestion = int(input('What number does this image read?'));
        if sixthquestion == 3:
            print('Correct!');
            tally += 1;
            break
        elif sixthquestion != 3:
            print('Sorry, the answer you have provided was incorrect. ');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara7.PNG')
window. create_image(0,0, anchor = NW, image = image)

while True:
    try:
        seventhquestion = int(input('What number does this image read?'));
        if seventhquestion == 15:
            print('Correct!');
            tally += 1;
            break
        elif seventhquestion !=15:
            print('Sorry, the answer you have provided was incorrect. ');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara8.PNG')
window. create_image(0,0, anchor = NW, image = image)

while True:
    try:
        eighthquestion = int(input('What number does this image read?'));
        if eighthquestion == 74:
            print('Correct!');
            tally += 1;
            break
        elif eighthquestion !=74:
            print('Sorry, the asnwer you have provided was incorrect. ');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

print('You have made it to the last two questions, for these questions please attempt to answer correctly. If you see nothing in the images, please enter "nothing".');

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 487)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara9.PNG')
window. create_image(0,0, anchor = NW, image = image)

while True:
    try:
        ninthquestion = input('What number do you see presented in this image?');
        if ninthquestion == '2':
            print('Correct');
            tally += 1;
            break
        elif ninthquestion == 'nothing' or ninthquestion == 'Nothing':
            print('Now moving on to the next question');
        else:
            print('Wrong answer, please move onto the next question');
            break
    except ValueError:
        print('Invalid input, please enter a valid number')

window = Tk()
window.title('Add Image')
window = Canvas(window,width=500, height = 500)
window.pack()
image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara10.PNG')
window. create_image(0,0, anchor = NW, image = image)

tenthquestion = input('What number do you see presented in this image?');
if tenthquestion == '6':
    print('Correct');
    tally += 1;
elif tenthquestion == 'nothing' or tenthquestion == 'Nothing':
    print('Now moving on to the next question');
else:
    print('Wrong answer, please move onto the next question');

def Scorecount():
    if tally >= 8:
        print(f'Congrats! You had a score of {tally}. You are not colorblind.');
    elif tally < 8:
        print(f'You had a total score of {tally}. This indicates that you may have a color deficiency, please proceed to the next couple of questions to determine which category you may fall under. ');
        

Scorecount()
Protandeficiency = 0;
Protanomoly = 0;
Deuteranopia = 0;
Deuteranomaly = 0;
if tally < 8:
    window = Tk()
    window.title('Add Image')
    window = Canvas(window,width=500, height = 500)
    window.pack()
    image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara11.PNG')
    window. create_image(0,0, anchor = NW, image = image)

    eleventhquestion = input('Please enter the number that you see clearer. For example if the left number is more clear than the right, enter that value. Ex. if you see 36 however the 3 is slightly less visable, enter (3)6. Or if you see 6 less visable enter 3(6), what number do you see? ');
    if eleventhquestion == '6':
        Protandeficiency += 1;
    elif eleventhquestion == "(2)" + "6":
        Protanomoly +=1;
    elif eleventhquestion == '2':
        Deuteranopia += 1;
    elif eleventhquestion == '2' + '(6)':
        Deuteranomaly += 1;
    else:
        print('Please move on to the next question');
    
    window = Tk()
    window.title('Add Image')
    window = Canvas(window,width=500, height = 423)
    window.pack()
    image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara12.PNG')
    window. create_image(0,0, anchor = NW, image = image)

    twelfthquestion = input(' Please enter the value that you see. Make sure to enter properly. ');
    if twelfthquestion == '2':
        Protandeficiency += 1;
    elif twelfthquestion == '(4)' + '2':
        Protanomoly +=1;
    elif twelfthquestion == '4':
        Deuteranopia += 1;
    elif twelfthquestion == '4' + '(2)':
        Deuteranomaly += 1;
    else:
        print('Please move on to the next question');

    window = Tk()
    window.title('Add Image')
    window = Canvas(window,width=500, height = 500)
    window.pack()
    image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara13.PNG')
    window. create_image(0,0, anchor = NW, image = image)

    thirteenthquestion = input(' Please enter the value that you see. Make sure to enter properly. ');
    if thirteenthquestion == '5':
        Protandeficiency += 1;
    elif  thirteenthquestion== '(3)' + '5':
        Protanomoly +=1;
    elif thirteenthquestion == '3':
        Deuteranopia += 1;
    elif thirteenthquestion == '3' + '(5)':
        Deuteranomaly += 1;
    else:
        print('Please move on to the next question');

    window = Tk()
    window.title('Add Image')
    window = Canvas(window,width=500, height = 500)
    window.pack()
    image =PhotoImage(file = 'C:\\Users\\antor\\OneDrive\\Desktop\\Ishihara14.PNG')
    window. create_image(0,0, anchor = NW, image = image)

    fourteenthquestion = input(' Please enter the value that you see. Make sure to enter properly. ');
    if fourteenthquestion == '6':
        Protandeficiency += 1;
    elif  fourteenthquestion == '(9)' + '6':
        Protanomoly +=1;
    elif fourteenthquestion == '9':
        Deuteranopia += 1;
    elif fourteenthquestion== '9' + '(6)':
        Deuteranomaly += 1;
    else:
        print('Please move on to the next question');
    
if Protandeficiency == 4:
    print(f'You had a score of {Protandeficiency}. This indicates that you may have a' , Redgreen[2] , 'color deficiency. Please see a specialist to get further help.');
elif Protanomoly == 4:
    print(f'You had a score of {Protanomoly}. This indicates that you may have a' , Redgreen[1] , 'color deficiency. Please see a specialist to get further help.');
elif Deuteranopia == 4:
    print(f'You had a score of {Deuteranopia}. This indicates that you may have a' , Redgreen[4] , 'color deficiency. Please see a specialist to get further help.');
elif Deuteranomaly == 4:
    print(f'You had a score of {Deuteranomaly}. This indicates that you may have a' , Redgreen[0] , 'color deficiency. Please see a specialist to get further help.');

print('This concludes the colorblind test, thank you for using it!');

