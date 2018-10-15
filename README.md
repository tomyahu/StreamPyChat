# StreamPyChat

This is the program that I use to display the chat of my streams over at Picarto.tv in real time.

The program itself just reads form a textfile and displays it as a chat in a very tall window. The text file is formated like this:

```
[hour] Source User, Message
[23:56:39] Picarto.tv TomyAtemo, TomyAtemo: hola :O
[0:12:30] Picarto.tv TomyAtemo, Derianart: hola c:
```

And the program displays the message of each line in a box.

##Dependencies

StreamPyChat has the following dependencies (tested in python 3.6)

- pygame

##How do I use it in my streams?

Well first you need [Restream](https://restream.io), it is a program that gets the chat of your streams and can pass it to a text file (with the same format seen before). Set it so that the file RestramChat.txt is in the same directory as main.py, then run main.py.

After that you can capture the screen of the chat with [OBS](https://obsproject.com/) and adjust it as you like. Pro tip: you can use the chroma key filters in obs to make black (#000000) invisible. 

##Customization

My idea when I made this program was "wow, it would be really cool if I could display my chat in my streams with a custom skin" so I've been working on that. Currently it can support diferent fonts and different boxes for items:

###Creating Frames

####Add a Font

To create custom Frames (the boxes I talked about earlier) first add your own font in the font directory view/fonts (suppose it is named "myFont.tff"). Then go to fontBank.py and add the following line:

```myFont = loadFont('myFont.tff', 20)```

The '20' there is just the size of the font, the value 20 is recommended but you can change that number if it is not the size you like.

####Make the box

Then for the box itself you need to create a new folder in view/images (suppose we named it "myFrame"), inside you have to put 4 images in order for the program to create your frame:

- an image named top.png (the top border of your frame)
- an image named bottom.png (the bottom border of your frame)
- an image named border.png (the left and right borders)
- an image named background.png (the background)

After you've done that, then go to textureBank and add the line:

```myTex = create_splitted_texture('myFrame')```

####Finally...

Go to main.py and go to line 24 where it should say ```factory = FrameFactory()```. After that line add the following two lines:

```
factory.set_texture(myTex)
factory.set_font(myFont)
``` 

And you are done :D

##Future Plans

- Create an interface with TKinter
- Fix bug that makes a super big box when there is a super big word like an url.