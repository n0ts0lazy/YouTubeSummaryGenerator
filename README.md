# YouTube Summary Generator Version 2.0

## Welcome to the new and improved version of your favorite video transcription tool for YouTube™️ by yours truely n0ts0lazy which can also shrink your hour long lectures into short summaries so that you don't need to watch the video at 2x speed (😏 I know how many of you do this) or read the whole transcrption of the video

---

Installation instructions for the code base
>`$ python3 venv <your local packages name>`

Now switch to this as your packages directory by
> `$ source <your local package name>\bin\activate`<br>
> `pip install -r requirements.txt`
 
Verify it once by using
>`diff <(pip freeze | sort) <(sort requirements.txt)`
<br>*You should get output similar to this in case there is a package discrepency else it should be blank*
>>`< missing-package-1==1.0.0`
<br>`< missing-package-2==2.0.0`
<br>`> extra-package-1==1.0.0`
<br>`> extra-package-2==2.0.0`

<br>In this example:

Lines prefixed with `<` indicate packages that are in requirements.txt but not installed.
Lines prefixed with `>` indicate packages that are installed but not listed in *`requirements.txt`*.
The version numbers shown after the package names `(==1.0.0, ==2.0.0)` may vary depending on your actual packages and their versions.

<br> To turn it off just type `deactivate` in the console to come out for this package directory and use your global packages again

---

Currently working on re-writing the new codebase which is utilizing LLM models for creating the transcript and summary

---
Future plans include a toggleable GUI interface and end user executable for both console version and GUI version
