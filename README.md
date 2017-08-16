# pptx_pdf_script
A python script that will regularly poll for changes, and convert a pptx file to pdf

This was created over a period of ~6 hours; it could be thought of has a hackathon. 

To use, run the script in the bin folder. Let's assume it has been added to the path. It would look like python pptx_export.py [input file path] [output file path]

Right now, it can accept both absolute and relative file paths - though stepping up a directory with ".." is not yet supported. 

# Utility 
Though it is still in planning, I may have the opportunity to give regular talk about software development. As a result, I am going to be interacting a lot with PowerPoint. Having a tool like this to export to PDF every time I save will be nice. Though the impact may not be large, it's good to have one less thing to keep in my mind. 

# What did I learn?
A lot. Though I was familiar with the theory, having this opportunity to practice and learn was great.
* Python OS. I feel a lot more confident with Python's OS module and I have a better understanding of managing files & directories programmatically.
* Python SYS. I had dabbled with argvs before with Python, but this was my first time implementing them in a significant project.

# What’s next?
There are a few major improvements points I want to add in the next version.
* Use PowerShell to kick off the script. Right now, a py file sits in bin, which does not technically make sense. (Stop gap solution). I am still super new to PowerShell, and I hope to learn more from resources like Pluralsight, and by practicing on my own.
* Better unit tests. There is a single unit test, but it is not very significant. I have not done a lot of unit testing before, but I think this project would be a great opportunity to learn & practice.
* Using the OS to watch the directory. Right now, I am using a polling approach, checking the directory every second. It would be more elegant to have the OS notify the script when the file has changed. I attempted to implement this with a few different modules, but I have not yet found success. (I think I just need to go a bit slower and understand the underlying code)

Not only will this make the script better, it will be an opportunity to expand my skillsets and be a better developer. 

# Flow chart:
[![Demo](https://github.com/noah-dev/pptx_pdf_script/blob/master/docs/algorithim.png)]