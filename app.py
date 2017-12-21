from flask import Flask, render_template
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'paw'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234qwer'
app.config['MYSQL_DATABASE_DB'] = 'pra'
app.config['MYSQL_DATABASE_HOST'] = '77.55.217.112'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")

DELIMITER $$
CREATE
DEFINER = `paw` @ ` % ` PROCEDURE `
createUser
`(
     IN p_name VARCHAR(45),
 IN
p_usernameVARCHAR(45),
IN
p_password
VARCHAR(45)
)
BEGIN
if (select exists (select 1 from users where username = p_username) ) THEN
select
'Username Exists !!';

ELSE

insert
into
users
(
    name,
    username,
    password
)
values
(
    p_name,
    p_username,
    p_password
);

END
IF;
END$$
DELIMITER;