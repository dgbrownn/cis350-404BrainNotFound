![image](https://github.com/user-attachments/assets/1df5bdf9-3ed7-4ef8-9f91-960917da843d)

# Team Members and Roles

* Dylan Brown (Python Backend Logic, Logic Unit Testing)
* Michael Frankowski (Web Application Designer)
* Eli Assaf (Debugger, Frontend Logic)
* Nick Fultz (Front End Developer)

# Abstract

Maintaining a healthy diet requires consistent effort, and one of the biggest challenges people face is accurately tracking their daily calorie intake. Staying on top of nutritional goals can be overwhelming with busy schedules, varied food choices, and hidden calories in many foods. Our Calorie Tracker simplifies this process by providing an intuitive, user-friendly platform that helps individuals monitor their food consumption, set personalized goals, and make informed dietary decisions. By offering a comprehensive database of foods, easy logging features, and insightful analytics, our tool empowers users to take control of their nutrition without the hassle of manual calculations. Whether for weight loss, muscle gain, or general wellness, Calorie Tracker makes calorie tracking effortless and effective.

# Our Project

Our project is a macronutrient (fats, protein, carbohydrates) and calorie calculator. The logic is written in Python, while user interface design is done in HTML and connected using the FLASK microweb framework. The calorie calculator portion of our project first calculates a user's basal metabolic rate (the amount of calories needed for the body to function while stagnant) and calculates maintenance calories using that BMR. Next, the application uses a user's maintenance calories to calculate calorie deficits (weight loss) or surplus amounts (weight/muscle gain). This is shown in a sleek very easy-to-understand way using HTML and CSS scripts. It allows you to only focus on the calories, protein, and other nutrients you might need in the day. This allows you to only focus on your goals, and nothing else!

# Tasks and Ticket System (Jira)

In order to keep track of features, designs, and the actual web app, we used the project management application Jira. This kept us on track for the various different features functions and designs that we had to do. It allowed us to focus on what needed to get done while keeping it simple. Overall, this helped streamline our workflow. 
![image](https://github.com/user-attachments/assets/7f7bfa4d-89ea-48b7-acca-29a17d07fb5a)

# Run Instructions

Running the application is quite a simple process due to using flask! All you need to do in order to run the website is save the folder in this repo "macro_cal_FLASK". This will download the code for the python, HTML, and CSS. When downloaded, make sure to run the file in a virtual environment (For example if you are using a Linux system, make sure you run python3 -m venv, usr/bin/activate, and then flask run! This is used to cache all the times someone accessed the website). Doing this will run the website on your device, using the loopback address 127.0.0.1. When you input that into your browser, it will show the login page. Here there will be a button that says admin login. You can find the admin information in the source code. When inputting the admin information, you will be greeted by the metrics page, and once submitted, you will be directed to the homepage, to see your needed calories, protein, and other notable nutrients!

## Login page
![image](https://github.com/user-attachments/assets/4fad2b45-b5ca-49bb-b90c-a445f4d996f5)
Once you run the server in the terminal, go to any browser you prefer (Firefox, Google Chrome, Microsoft Edge, etc.), and type in the address it gives you (it should be http://127.0.0.1:5000). This will bring you to the homepage! You can then login using the admin credentials (this is hardcoded into the app.py file!). 

## Calculation page
![image](https://github.com/user-attachments/assets/4100c6ec-d102-4079-bcb5-012d896abb7a)

Once you login, you will be prompted with the above. This is the interface to do the calorie calculation! Put in your metrics, and hit the complete button. This will then bring you to the dashboard with the calories, protein, carbohydrates, and fats. 

## Dashboard
![image](https://github.com/user-attachments/assets/5665fa9e-38c2-4c17-858e-3bc86dacc7ab)
This is an example of what the dashboard would look like! Now, of course this will change depending on the metrics you put into the calculation page of course. 

# Conclusion
Overall, this web app is definitly a fun little project that you can run anywhere you would like! It's a neat little web application that does serve a very good purpose of calculation calories. It is still bare bones, however that just means that there is a lot of implementation that can be done with it! We truly believe that this can be a useful tool for anyone willing to get into shape.




