examples = [
	{
		"input": "How many passengers survived and how many did not?",
		"query": "SELECT survived, COUNT(*) AS count FROM titanic GROUP BY survived;"
    },
	{
		"input": "How many female passengers survived?",
		"query": "SELECT COUNT(*) AS count FROM titanic WHERE survived=1 and sex='female';"
    },
	{
		"input": "How many passengers travelling in the first class did not survive?",
		"query": "SELECT COUNT(*) AS count FROM titanic WHERE survived=0 and pclass=1;"
    },
    {
        "input": "What is the average age of passengers who survived versus those who did not?",
        "query": "SELECT survived, AVG(age) AS average_age FROM  titanic GROUP  BY survived;"
    },
    {
        "input": "How many passengers were in each class (pclass)?",
        "query": "SELECT pclass, COUNT(*) AS count FROM  titanic GROUP  BY pclass;"
    },
    {
        "input": "What is the survival rate for each passenger class (pclass)?",
        "query": "SELECT pclass, AVG(survived) AS survival_rate FROM  titanic GROUP  BY pclass;"
    },
    {
        "input": "Did women have a higher survival rate than men?",
        "query": "SELECT sex, AVG(survived) AS survival_rate FROM  titanic GROUP  BY sex;"
    },
    {
        "input": "What is the average fare paid by passengers in each class?",
        "query": "SELECT pclass, AVG(fare) AS average_fare FROM  titanic GROUP  BY pclass;"
    },
    {
        "input": "How many passengers were traveling with siblings/spouses aboard?",
        "query": "SELECT \"siblings/spouses aboard\", COUNT(*) AS count FROM  titanic GROUP  BY \"siblings/spouses aboard\";"
    },
    {
        "input": "What is the survival rate for passengers with different numbers of parents/children aboard?",
        "query": "SELECT \"parents/children aboard\", AVG(survived) AS survival_rate FROM  titanic GROUP  BY \"parents/children aboard\";"
    },
    {
        "input": "What is the distribution of ages among passengers?",
        "query": "SELECT age, COUNT(*) AS count FROM  titanic GROUP  BY age ORDER BY age;" 
	},
    {
        "input": "What is the distribution of ages among survivors?",
        "query": "SELECT age, COUNT(*) AS count FROM  titanic WHERE survived=1 GROUP  BY age ORDER BY age;" 
	},
    {
        "input": "List the names of all the people who did not survive.",
        "query": "SELECT name FROM  titanic WHERE survived=0;" 
	},
    {
        "input": "List the names of all survivors.",
        "query": "SELECT name FROM  titanic WHERE survived=1;" 
	},
	{     
		"input": "Which passengers paid the highest fares?",     
		"query": "SELECT name, fare FROM titanic ORDER BY fare DESC LIMIT 10;"
	}
]