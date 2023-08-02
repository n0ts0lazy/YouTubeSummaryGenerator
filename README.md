# YouTube Summary Generator and Comparision Version 1.0

<h2>This branch has been archived and will not recieve any further update newer codebase is in progress and will be pushed into the new branch</h2>

This project utilizes pipeline from the transformers which is used to create the model used for feature extration from the video transcript. The data from YouTube is extracted using youtube_api (currently deprecated) to generate the video transcript. Which is then used to create a comparative study between actual transcript of the video and the shortened summary generated using this model to see how much of the content is similar.<br>
This project was originally created as a part of University curriculum of my undergradute course in Natural Language Processing prior to existance of Large Language Models used currently for these kind of task which are much faster and efficient<br>

<br>Installation procedure<br>
Non-Windows Platform:
---
You will need at least python 3.7 to execute the program <br>
Recommend creating a virtual environment so that it doesn't install everything into the home directory, create virtual environment using:
>$ python3 -m venv /path/to/new/virtual/environment

Activate the environment by using source command and:
>$ source /yourdirectory/bin/activate

To deactivate the virtual environment use deactivate command:
>$ deactivate

Add the required libraries for the code using the pip command
>$ python3 -m pip install -r requirements.txt -f file:///path/to/archive/

___

<br>Windows Platform:
---
In your choice of IDE add the requirement add the _"requirement.txt"_ as the environment variable during the creation of the project or add it later after creating the project using the import tool for requirement.
<br>

How to use this program
---
On first time execution you will get _"paste our link here.txt"_ where you can enter your link <br>
Also on execution if the export folder is not present it will create that as well<br>
Now enter the video link in _"paste our link here.txt"_ in the same directory and run the program again<br>
Result for the execution will be saved in **_export_** folder<br>
All files will be saved in format <**_file type_ videoID timestamp.txt**>
___
Created by:
n0ts0lazy (aka Arnab)
