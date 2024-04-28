# OIM Final Project
## Mood Tracker Log Web Application

## Project Overview
Mood Tracker is a web application designed to help users log and analyze their daily emotional states through sentiment analysis. By inputting textual descriptions of their day, users can track their mood patterns over time on an interactive calendar.

## Usage Guidelines
- **Logging a Mood**: On the home page, describe your day in the text field and click "Analyze" to log your mood.
- **Viewing Mood Trends**: Moods and sentiment scores are visually represented on the calendar. Click on a specific date to see a detailed view of your mood log with an animation for that day.

## Dependencies
Key libraries and frameworks used in this application include:
- Flask
- Hugging Face's transformers
- SQLite
- FullCalendar

Run `pip install -r requirements.txt` to install all required libraries.

## Deployment
To deploy locally:
- Run `python app.py` in the root directory after installing dependencies.
- Access the web app through `localhost` in your browser.

## Project Structure
The application's structure:
- `/static`: Static files like stylesheets, JavaScript, and images (`favicon.png`).
- `/templates`: HTML templates.
- `/app.py`: Entry point for the Flask application.
- `/db.py`: Database management.
- `/schema.sql`: Database schema.
- `/requirements.txt`: Project dependencies.

## Collaboration Information
Project completed by Steven Huang, handling all planning, development, testing, and documentation.

## Acknowledgments
Thanks to the Flask framework, Hugging Face's transformers for sentiment analysis, and FullCalendar for event visualization.

## Reflection
### Process Reflection
This was a interesting project for me as I incorporated both frontend and backend technologies into making the project work. The development process itself showed me the importance of precise requirements gathering and testing, as I did spend time cotinuously looking for the best dependencies as well as models to make the project work. Early on, integrating the sentiment analysis API posed a challenge, but as I kept trying, I was able to sucessfully integrate machine learning into analyzing journal sentiments. 

### Learning Reflection
This project was an fun and a great learning experience for me, especailly in integrating APIs and visualizing data on the frontend. I was also able to use ChatGPT to help me with research and debugging. Going forward, I will keep building different projects, and these skills and knowledge that I used in this project, and the knowledge I gained form the course will provide me with solid foundation for my future in sde and machine learning..
