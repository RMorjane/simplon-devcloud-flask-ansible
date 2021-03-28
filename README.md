# Flask Application

This is a Flask Application deployed with Ansible in Azure Virtual Machine using Postgresql database.

Accessing to the home page : 

![image](https://user-images.githubusercontent.com/71873995/112757576-9c293e80-8fea-11eb-9a40-2d8d40e6cb0a.png)

Accessing to the incrementing id page : 

![image](https://user-images.githubusercontent.com/71873995/112757615-c7ac2900-8fea-11eb-91e0-6141da15b94b.png)

Accessing to the display id page : 

![image](https://user-images.githubusercontent.com/71873995/112757643-edd1c900-8fea-11eb-8d5b-e30fbad6afbb.png)


## Installation

playbook.yml :
```
- name: Install flask app with postgres database
  hosts: morjane-vm
  become: yes
  become_method: sudo
  gather_facts: yes
  remote_user: morjane

  tasks:

    - name: Install flask ripository
      shell: rm -Rf flask_app
      shell: chdir=/home/morjane/ git clone https://github.com/RMorjane/simplon-devcloud-flask-ansible.git flask_app

    - name: Go to the folder and execute docker-compose
      shell: chdir=/home/morjane/flask_app/ docker-compose up --build
```

docker-compose file : 
```
version: "3.2"

services:
  db:
    container_name: local_postgres
    image: postgres
    env_file: .env
    networks:
      - dbnet

  flask_app:
    container_name: flask
    build: ./app
    depends_on:
      - db
    ports:
      - 4000:4000
    volumes:
      - .:/app
    networks:
      - dbnet
    command: sh -c "python /app/main.py"

networks:
  dbnet: {}
```

Use the following command line :

```bash
ansible-playbook -i hosts playbook.yml --key-file rmorjane_key.pem
```

## Technologies

#### Back-End :
``
Python : language for loading web application,
Flask : creating recipe web application,
render_template : rendering the web page,
Postgresql database.
``
#### Front-End :
``
HTML5,
CSS3,
Javascript
``


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
