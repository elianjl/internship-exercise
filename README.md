# Exercise for an intership

## 1. Exercise ❔

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below:

_Example 1:_

INPUT
- RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
- ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
- ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
- ASTRID-RENE: 2
- ASTRID-ANDRES: 3
- RENE-ANDRES: 2

_Example 2:_

INPUT:
- RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00
- ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:
- RENE-ASTRID: 3

## 2. Solution 🧠

The input has a specific format, so it can be separated the data in a class like object-oriented paradigm and then process that to find the solution.

The solution consists of comparing each employee with the rest of their teammates without repetitions, compare their schedule starting with the day and consequently, iterating and comparing their schedules to find a coincide at work on the same day. Finally, show on the screen the number of times that each employee has coincided at work with their teammates.

## 3. Architecture 🏗
The architecture of the solution is based on the MVC (Model-View-Controller)
<div align="center"> 
<img width="600" height="600" alt="MVC Diagram" src="https://github.com/elianjl/internship-exercise/blob/main/architecture/MVC_ACME.png">
</div>

## 4. Aproach 🛠
The approach that I found for the solution was look for the input data, after that convert the data into an object for easy handling. The object contains 2 attributes employee and a schedule, the schedule is a list that contains the days and hours. After obtaining the objects compare each employee with the rest to know the number of coincidences at the office.

## 5. Instructions to run the project 📝
### 5.1. In any IDE that allows running python code:
- Download the repository.
- Open the extracted repository folder from the IDE of your choice.
- Enter to the project folder.
- Run the _app.py_ file.

To run the unit tests:
- Enter to the project folder.
- Open a new terminal.
- Install pytest `pip install -U pytest`
- Write `pytest`

### 5.2. In CMD or PowerShell:
- Download the repository.
- Open the extracted repository folder in a CMD or PowerShell.
- Write `cd project` & Enter.
- Write `python app.py` & Enter.

## 6. Developed with ✏
- Visual Studio Code - IDE used
- Python 3.10.5 - Language used
- pytest - Unit testing framework used

##
Developed by Elian 🎧
