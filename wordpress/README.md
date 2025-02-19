# Auto docker setup for Wordpress

By running `docker compose up -d` you will create 3 containers:
- `wordpress-web`: Creates a wordpress instance that autoconnects to the MariaDB database that is also created in the docker-compose file.
- `mariadb`: The database in which wordpress saves all web-related data to.
- `nginx-revese-proxy`: Handels the traffic to the wordpress website.

If you want you can change the values in the `env` folder but remember that the `MYSQL_` and `WORDPRESS_DB_` needs to have the same values in order to connect with each other.

When you've set everything up you can access the website with [localhost](http://localhost:80) and set up your wordpress website.

**OBS: WHEN YOU SET THE USERNAME AND PASSWORD YOU NEED TO REMEMBER IT IN ORDER TO LOG IN FOR THE FIRST TIME!**
