# Web Scraping with Python
This is the repository for the LinkedIn Learning course Web Scraping with Python. The full course is available from [LinkedIn Learning][lil-course-url].

![Web Scraping with Python][lil-thumbnail-url] 
Instructor Ryan Mitchell teaches the practice of web scraping using the Python programming language. Ryan helps you understand how a human browsing the web is different from a web scraper. She introduces the Chrome developer tools and how to use them to examine network calls. Ryan shows you how to install Scrapy with pip and how to write some "Hello, World" code to scrape a simple web page. She covers how to use the Scrapy LinkExtractor to find internal links on a web page, then demonstrates how to configure Scrapy and the ItemPipeline to write data to various file formats. Ryan walks you through best practices for organizing your projects, writing reusable parsers, and future-proofing your spiders. She explains how APIs work and how they can be used to retrieve data directly. Ryan explores headers and cookies, then goes into browser automation and how to integrate Selenium with Scrapy. In conclusion, she offers ideas to continue your studies in computer science and think creatively about automation.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
All files for the course are available in the Main branch. Additionally, files are available in branches, which are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get this message:

   	error:  Your local changes to the following files would be overwritten by checkout:        [files]
    	Please commit your changes or stash them before you switch branches.
    	Aborting

To resolve this issue:
	
   	Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


## Installing
1. Clone this repository into your local machine using the terminal (Mac), CMD (Windows), or a GUI tool like SourceTree.


### Instructor

**Ryan Mitchell Specht**

_Senior Software Engineer at GLG_

Check out my instructor page on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/ryan-mitchell-specht?u=104).

[lil-course-url]: https://www.linkedin.com/learning/web-scraping-with-python
[lil-thumbnail-url]: https://cdn.lynda.com/course/2848331/2848331-1607698087639-16x9.jpg
