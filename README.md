# CS-374FinalProject
WORKER WATCHER
By: Michael Connors, Evan Tilton, and Owen Fazzini

This program is be able to parse and execute commands based on a database of information from Google Forms responses.

Google Form to fill out: https://docs.google.com/forms/d/e/1FAIpQLSczvHolDctkvJLxm-PfOcCE4VcJFqqBH994Auo-6Q1thZ3Ncw/viewform

The Google Form has Regular Expressions built in to help narrow down possible user input. The "Worker Name:" field does not allow any commas, and the "Break Duration:" response has to fit in the criteria of this regular expression: \d+ [a-z]+( [a-z]* ?\d+ [a-z]+)?

Google Sheets that stores all responses: https://docs.google.com/spreadsheets/d/1l20PqkNbb3_HmhJprtnLzuWiBWeYkbv6t5RQKZKMtGU/edit?usp=sharing

Google Sheet for output: https://docs.google.com/spreadsheets/d/19_a76VLiyTyHuXwHH4-beAQuUvxEowTaJiBVJSRRlPI/edit?gid=0#gid=0

File paths will have to be updated based on local file location.

Google Slideshow Presentation: https://docs.google.com/presentation/d/1BeNvWNpisUvEChD9Oqh7D5cPazunxVhT_rEBqfafLgw/edit?usp=sharing

Evan's Digital Presentation: https://youtu.be/gQ8b7aSxRLY

---------------------[ Submission Writeup]---------------------------
Our program idea was to parse inputs based on reponses to a Google Form. We did so by putting every response into a Google Sheet, downloading it as a csv, and then performing calculations specified through user input based on the values stored. Finally, the user has a choice to upload their calculations into a separate Google Sheet that makes the information a lot easier to process for those who are not as technilogically inclined. We had some complications with the unit tests though. The unittest import used to test our functions caused some issues. However, our functions are equipped to handle any edge case from the user input, and the google forms can only accept certainly formatted responses so the database can not be sabotaged. It took us two days to complete our project before the deadline. It was very enjoyable to watch as our concept flourished into a fully fledged program. Therefore, we believe that we deserve an A on our outstanding project.
