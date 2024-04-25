<html lang="en">
  <head>
    <title>Клиенты</title>
    <link rel="stylesheet" href="style.css" type="text/css" />
  </head>
  <body>
    <h1>Clients</h1>
    <table>
      <tr>
        <th>ID</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Email</th>
        <th>Phone Number</th>
        <th>Preferred Contact</th>
      </tr>
      <?php
				$mysqli = new mysqli("db", "user", "password", "appDB");
				$result = $mysqli->query("SELECT * FROM Customers"); foreach ($result as $row) {
      echo "
      <tr>
        <td>{$row['Id']}</td>
        <td>{$row['FName']}</td>
        <td>{$row['LName']}</td>
        <td>{$row['Email']}</td>
        <td>{$row['PhoneNumber']}</td>
        <td>{$row['PreferredContact']}</td>
      </tr>
      "; } ?>
    </table>
    <?php
			phpinfo();
		?>
  </body>
</html>

