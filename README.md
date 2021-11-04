# Practica_6
## Student
- Juslan Vargas

## 1. Describing the Problem

Our job consists of organizing the schedules of the speakers who will come to give talks to the Catholic university on 3 different areas, there are various restrictions that must be met such as that a speaker should not give two consecutive talks from the same area and others more. With all these restrictions and the speakers that will be presented, we must see if a schedule that accommodates all restrictions without exception is applicable or not.

## 2. Describing the Solution

In this case, the knowledge of PSSR will be applied, starting with the challenge of modeling the problem as if it were a PSSR. Later we will apply the algorithms seen in class that solve the problem using, such as the Backtrack algorithm and the heuristics that are seen in classes such as the "most constrained value", the "least constrained value" and "forward checking".

To apply PSSR, Variables, domains and assignments are required.
- In our case, the variables will be our available hours such as 9:00, 10:00. It is worth mentioning that each talk has a duration of 1 hour. As there are three areas which can be given talks, there will be 3 variables of the 9:00 type so, for example, to be able to assign a schedule of 9:00 to three same areas since it is completely possible.
- Moving on to the domains, in this case all the speakers will give the talks in order to assign them to a respective schedule.
- The assignments were placed while the algorithm is running, we just have to place one speaker in the start of the algorithm to continue with the others

It was convenient to apply PSSR in this way since the schedules have their neighbors defined, as an example we can see the neighbors of a schedule at the file "Vecinos de un horario de arriba" that is inside the images folder for any hour of (9:00 or 17:00)


Here (at the file "Horarios de un dia.png" that is inside the images folder) we can see the neighbors of a schedule that is between 10:00 until 16:00

All the variables are 90, here we can see the complet variables.
(at the file "Horarios de toda la semana.png" that is inside the images folder)


## 3. Experiments & Results

I could not run the algorithms togheter to solve the problem, but the algorithms and logic of the problem are in the Backtrack.py file

