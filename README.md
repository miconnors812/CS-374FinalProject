# CS-374FinalProject
This program will be able to parse and execute commands based on a database of information from Google Forms responses.

Google Form to fill out: https://docs.google.com/forms/d/e/1FAIpQLSczvHolDctkvJLxm-PfOcCE4VcJFqqBH994Auo-6Q1thZ3Ncw/viewform

Google Sheets that stores all responses: https://docs.google.com/spreadsheets/d/1l20PqkNbb3_HmhJprtnLzuWiBWeYkbv6t5RQKZKMtGU/edit?usp=sharing

Google Sheet for output: https://docs.google.com/spreadsheets/d/19_a76VLiyTyHuXwHH4-beAQuUvxEowTaJiBVJSRRlPI/edit?gid=0#gid=0

The Google Form has Regular Expressions built in to help narrow down possible user input. The "Worker Name:" field does not allow any commas, and the "Break Duration:" response has to fit in the criteria of this regular expression: \d+ [a-z]+( [a-z]* ?\d+ [a-z]+)?
