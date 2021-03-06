# Write a SQL query for a report that provides the following information for each person in the Person table, 
# regardless if there is an address for each of those people:

# FirstName, LastName, City, State

select FirstName, LastName, City, State
from Person as p
left join Address as a
on p.PersonId = a.PersonId

