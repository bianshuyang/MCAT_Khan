# Re-available Khan Courses
# MCAT
As described by Khan Academy, MCAT Materials will be expired in September 30, 2021. This project aims at downloading all MCAT stuff(including excerises, reading material, discussion page and videos) to your desktop computer. Currently, this is a project coded in python. 
Detailed information about the removal of MCAT stuff please refer to this link provided by Khan Academy:
https://khanacademy.zendesk.com/hc/en-us/articles/360043801271#h_3892d747-c83f-490f-9ded-e080b04f9a4d
# NCLEX-RN
As described by Khan Academy, NCLEX-RN Materials will be expired in July 15, 2020. This project also aims at downloading all NCLEX-RN stuff to your desktop computer. Currently, this is a project coded in python. 
Detailed information about the removal of MCAT stuff please refer to this link provided by Khan Academy:
https://khanacademy.zendesk.com/hc/en-us/articles/360043801271
# Main Goal
This project aims at downloading Khan Academy material to a desktop computer to help students who don't have stable connection to internet. 
Note: This project could also be used to download other K-12 material and test-prep material provided by Khan-academy.
# How to Use
0. Place all .py files in one same directory.
0. Find a folder where you will save all of your videos and documents. It might took several gigabytes.
0. Python should be installed and added to Environmental Path, urllib package should be installed.
1. Run main.py. Input the type of test you want. For instance, MCAT, nclex-rn, etc.
2. After running the main.py, a bat file get_folder.bat will be found on this folder. Run this .bat file.
3. Run submain.py, this will add a get_videos.py into each folder and create a get_video.bat.
4. Run this get_video.bat file. It will download all videos from Khan.
5. Run thirdmain.py. It could be run simultaneously with submain.py. And that their bat files could also be run simultaneously. Generally, get_article.bat would take far less time to complete since it only downloads webpages into docx. While for get_videos.bat, it may take several full days to complete the downloading process. To save energy, it might be best to shut down other download tools and close the screen (but not let the computer sleep) whenever possible.
# Other features are still under construction.
I am a novice at programming, if there are issues and errors please don't hesitate to contact me. Thanks.
