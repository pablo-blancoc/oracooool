GET_ALL_DRIVERS = "SELECT * FROM drivers"

GET_ALL_TEAMS = "SELECT * FROM teams"

GET_A_TEAM = "SELECT * FROM teams WHERE id = %s"

GET_DRIVERS_OF_TEAM = "SELECT * FROM drivers LEFT JOIN teams ON drivers.team = teams.id WHERE teams.id = %s"

CREATE_AN_ACCOUNT = "INSERT INTO users(name, username, pwd) VALUES (%s, %s, %s) RETURNING *"

GET_USER_BY_USERNAME = "SELECT * FROM users WHERE username = %s"

GET_MY_GROUPS = """
SELECT
    groups.*
FROM
    user_belongs_to_group
LEFT JOIN
    groups
ON
    user_belongs_to_group.group = groups.id
WHERE
    user_belongs_to_group.user = %s
"""

CREATE_A_GROUP = "INSERT INTO groups(name, description, owner) VALUES(%s, %s, %s) RETURNING *"

ADD_USER_TO_GROUP = "INSERT INTO user_belongs_to_group VALUES(%s, %s) RETURNING *"

REMOVE_USER_FROM_GROUP = "DELETE FROM user_belongs_to_group WHERE (user_belongs_to_group.user = %s AND user_belongs_to_group.group = %s)"

GET_ALL_USERS_FROM_GROUP = """
SELECT
    users.*
FROM
    users
LEFT JOIN
    user_belongs_to_group
ON
    user_belongs_to_group.user = users.id
WHERE
    user_belongs_to_group.group = %s
"""

GET_ALL_CIRCUITS = "SELECT * FROM circuits"

PREDICT_CIRCUIT = """
SELECT 
    next_results.*, 
    drivers.id AS did,
    drivers.name AS dname,
    drivers.team AS dteam,
    drivers.nationality AS dnationality,
    drivers.description AS ddescription,
    drivers.image AS dimage,
    drivers.link AS dlink
FROM 
    next_results
LEFT JOIN
    drivers
ON
    next_results.driver = drivers.id
WHERE 
    circuit = %s;
"""

GET_ALL_USERS_ORDERED_BY_POINTS = "SELECT * FROM USERS ORDER BY points"

SAVE_PREDS = "INSERT INTO predictions(userid,circuit,year,results) VALUES(%s, %s, 2023, %s)"

UPDATE_USER_POINTS = "UPDATE users SET points = points + %s WHERE id = %s"

GET_PREDICTION_FROM_USER = "SELECT * FROM predictions WHERE userid = %s AND circuit = %s"
