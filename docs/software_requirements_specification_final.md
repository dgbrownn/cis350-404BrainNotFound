# Overview
This Software Requirements Specification (SRS) document defines the functional and non-functional requirements for **Macrocal**, a metabolic rate and nutrition tracking application. It serves as a comprehensive guide for development, testing, and stakeholder alignment. The document is structured into software requirements (functional and non-functional), test specifications, and links to supporting artifacts.  
# Software Requirements 
This document is structured by our project's functional requirements first and then the non-functional requirements. The requirements will be listed, and then the specifications will be underneath them, with a unique ID to separate them.  

### Metabolic Rate Function  
| ID    | Requirement                                                                 |  
|-------|-----------------------------------------------------------------------------|  
| FR-01 | The system shall be able to accurately calculate a user's metabolic rate using a formula. |  
| FR-02 | The application shall be able to take in a user input.                      |  
| FR-03 | The system shall be able to show results clearly.                           |  
| FR-04 | The system shall be able to base the calculations off of being a man or a woman. |  
| FR-05 | The system should also properly be able to change metrics when given different parameters. |  

### User-Profile Management  
| ID    | Requirement                                                                 |  
|-------|-----------------------------------------------------------------------------|  
| FR-06 | The user shall be able to log in using an email and password.               |  
| FR-07 | The system shall allow for a user to be able to change their metrics on the fly. |  
| FR-08 | Users shall be able to properly see the calories, carbs, and protein they are supposed to get on their dashboard. |  
| FR-09 | A user shall be able to delete an account at will.                          |  
| FR-10 | Users will not mess around with the calculation.                            |  

### Dashboard Management  
| ID    | Requirement                                                                 |  
|-------|-----------------------------------------------------------------------------|  
| FR-11 | The dashboard shall display protein, carbs, and calories needed in the day. |  
| FR-12 | The dashboard shall be able to be accessed from any point on the website.   |  
| FR-13 | The system shall change the dashboard when different metrics are put in.   |  
| FR-14 | The dashboard shall be easy to understand.                                  |  
| FR-15 | The dashboard shall be the first thing you see when you log in.            |  

## Non-Functional Requirements  

### Performance  
| ID     | Requirement                                                                 |  
|--------|-----------------------------------------------------------------------------|  
| NFR-01 | The website shall be able to support multiple users.                        |  
| NFR-02 | The website shall be able to load in under 2 seconds.                       |  
| NFR-03 | The website shall be able to support a database for users.                  |  
| NFR-04 | The system will be able to calculate instantly.                             |  
| NFR-05 | The API shall have less than a 500ms response time.                         |  

### Security  
| ID     | Requirement                                                                 |  
|--------|-----------------------------------------------------------------------------|  
| NFR-06 | All sensitive information shall be encrypted.                               |  
| NFR-07 | No user shall be able to see another user's data.                           |  
| NFR-08 | The user shall be under HIPAA.                                              |  
| NFR-09 | No sensitive information shall be sold.                                     |  
| NFR-10 | All user's login information will be encrypted.                             |  

### Usability  
| ID     | Requirement                                                                 |  
|--------|-----------------------------------------------------------------------------|  
| NFR-11 | The system will be easy to understand.                                      |  
| NFR-12 | The User Interface will be simple and sleek.                                |  
| NFR-13 | There shall be fewer than 5 tabs to keep things simple and sleek.           |  
| NFR-14 | The systems tabs shall be easily accessible with one click.                 |  
| NFR-15 | Any user shall be able to understand the website without instructions.      | 

# Test Specification  
This section documents executed test cases for validation, covering unit, integration, and system tests.  

## Unit Tests  
| ID  | Description                     | Steps                                                                 | Input Values                   | Expected Output               | Actual Output | Pass/Fail | Requirement Link |  
|-----|---------------------------------|-----------------------------------------------------------------------|--------------------------------|-------------------------------|---------------|-----------|------------------|  
| TC1 | BMR Calculation                 | 1. Enter valid height/weight/age.<br>2. Execute calculation.          | Height: 70", Weight: 160lbs, Age: 25 | BMR: ~1667 kcal           | 1667 kcal     | Pass      | FR-01, FR-04     |  
| TC2 | Maintenance Calorie Calculation | 1. Calculate BMR first.<br>2. Apply activity multiplier.              | Activity: "moderate"          | Maintenance: ~2500 kcal    | 2500 kcal     | Pass      | FR-05            |  
| TC3 | Macro Calculation               | 1. Enter calorie intake.<br>2. Execute macro split.                   | Calories: 2000, Protein: 30%  | Protein: 150g              | 150g          | Pass      | FR-11            |  
| TC4 | Gender Validation               | 1. Input gender.<br>2. Validate against allowed values.               | Gender: "female"              | "female"                   | "female"      | Pass      | FR-04            |  

## Integration Tests  
| ID  | Description                     | Steps                                                                 | Input Values                   | Expected Output               | Actual Output | Pass/Fail | Requirement Link |  
|-----|---------------------------------|-----------------------------------------------------------------------|--------------------------------|-------------------------------|---------------|-----------|------------------|  
| TC5 | User Profile + Dashboard Sync   | 1. Update profile metrics.<br>2. Verify dashboard reflects changes.   | Weight: 170lbs → 165lbs       | Dashboard updates calories   | Updated       | Pass      | FR-07, FR-13     |  
| TC6 | Login + Data Encryption         | 1. Log in with credentials.<br>2. Check data encryption in transit.   | Email: "test@test.com"         | Encrypted session            | Encrypted     | Pass      | NFR-06, NFR-10   |  
| TC7 | Activity Level → Calorie Calc   | 1. Set activity level.<br>2. Verify maintenance calories update.      | Activity: "sedentary" → "active" | Calories increase by ~20%   | +20%          | Pass      | FR-05, FR-13     |  

## System Tests  
| ID  | Description                     | Steps                                                                 | Input Values                   | Expected Output               | Actual Output | Pass/Fail | Requirement Link |  
|-----|---------------------------------|-----------------------------------------------------------------------|--------------------------------|-------------------------------|---------------|-----------|------------------|  
| TC8 | End-to-End User Flow            | 1. Register → Login → Enter metrics → View dashboard.                 | Full user journey             | Correct macros/calories      | Correct       | Pass      | FR-06, FR-15     |  
| TC9 | Stress Test (Multiple Users)    | 1. Simulate 50 concurrent users.                                      | 50 login requests             | All requests processed in <2s | <2s           | Pass      | NFR-01, NFR-02   |  
| TC10| Data Privacy Check              | 1. Attempt to access another user’s dashboard via URL manipulation.   | Malicious user ID input       | Access denied                | Denied        | Pass      | NFR-07           |  

# Software Artifacts  
This section provides links to design and planning artifacts created during the project's development. These links will send you to a google doc folder, which will hold 

### **Diagrams**  
- **Use Case Diagram**: Illustrates user interactions with the system.  
  [View Use Case Diagram](https://docs.google.com/document/d/1PD-ulUSecM9u9wfln4B8XIfrYQI5E7XXNzgdV7z4Jmg/edit?tab=t.0)  
- **UML Class Diagram (Python Code)**: Shows the structure of the Python implementation.  
  [View Python UML Diagram](https://docs.google.com/document/d/11GkJoLwkPLsMyYJjFq2Im8ZB6uxH9JJJJRaiHgkcfZM/edit?tab=t.0)  
- **UML Diagram (Full Project)**: High-level architecture of the entire system.  
  [View Full Project UML](https://docs.google.com/document/d/12Sfur0Pr24MSAavq5sjwCDOVCPrzywjilEoeVlDrzRU/edit?tab=t.0)  

### **Project Planning**  
- **Gantt Chart**: Tracks project timelines and milestones.  
  [View Gantt Chart](https://docs.google.com/spreadsheets/d/1P-es0IwoiZeVfSLGGtsHRr5ka2ETJJqb1tXknbzdbIs/edit?gid=0#gid=0)
- **Jira Board**: Agile task management and sprint tracking.  
  [View Jira Board](https://macrocals.atlassian.net/jira/software/projects/UR404/boards/3) 

