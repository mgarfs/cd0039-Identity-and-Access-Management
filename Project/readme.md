# Coffee Shop (Full Stack)

This readme is used as a ongoing TODO and Checklist used while working with this Project!

_After Forking and Cloning GitHub repo_

## TODO List

1: [X] Read `03_coffee_shop_full_stack/starter_code/README.md`

2: [X] Check `TODO.lst`

   Working Directory: `03_coffee_shop_full_stack/starter_code`

3: (1:->) [X] Read `./backend/README.md`

 &nbsp;&nbsp;&nbsp;  (3:->)

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 1: Python - _already installed (using Python 3.8.10)_

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 2: Virtual Environment - _not using virtual environment_

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 3: PIP Dependencies - _install when as/when needed (ref: `pip install -r requirements.txt`)_

 &nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;  Ran into this issue before executing `pip install -r requirements.txt`:

 &nbsp;&nbsp;&nbsp;  &nbsp;&nbsp;&nbsp;  https://stackoverflow.com/questions/66647787/attributeerror-cant-set-attribute-when-connecting-to-sqlite-database-with-flas

    ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    launchpadlib 1.10.13 requires testresources, which is not installed.
    Successfully installed Click-7.0 Flask-1.0.2 Flask-Cors-3.0.8 Flask-SQLAlchemy-2.5.0 Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.6 astroid-2.2.5 ecdsa-0.13.2 future-0.17.1 isort-4.3.18 itsdangerous-1.1.0 lazy-object-proxy-1.4.0 mccabe-0.6.1 pylint-2.3.1 six-1.12.0 typed-ast-1.4.2 wrapt-1.11.1

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 4: Key Dependencies (Flask, SQLAlchemy, Flask-SQLAlchemy, jose) - _already installed_

 &nbsp;&nbsp;&nbsp;  [X] Check `./backend/src/database/models.py` - _during development of backend_

 &nbsp;&nbsp;&nbsp;  [X] Run the server - ref: `./backend/src/run_the_server.sh`

 &nbsp;&nbsp;&nbsp;  [X] Setup Auth0 (as described in `./backend/README.md`)

 &nbsp;&nbsp;&nbsp;  [ &nbsp;] Implement the server - ref: 5 and 6 below

4: (1:->) [X] Read `./frontend/README.md`

 &nbsp;&nbsp;&nbsp;  (4:->)

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 1: Node and NPM - _already installed (node v10.19.0 and npm 6.14.4)

 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; `sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash`

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 2: Ionic Cli (ref: <strike>`sudo npm install -g @ionic/cli --no-audit --prefer-offline`</strike>)

 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; `sudo npm install -g yarn --no-audit --prefer-offline`

 &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; `sudo yarn global add  @ionic/cli`

 &nbsp;&nbsp;&nbsp;  [X] Install dependencies 3: Project dependencies (ref: `npm install`)

 &nbsp;&nbsp;&nbsp;  [X] Configure Environment Variables - ref: 8 below

 &nbsp;&nbsp;&nbsp;  [X] Run the Frontend (ref: `ionic serve`)

 &nbsp;&nbsp;&nbsp;  OPTIONAL: [ &nbsp;] Check _Key Software Design Relevant to Our Coursework_ (as described in `./frontend/README.md`)

5: (2,3:->) [ &nbsp;] Perform changes in `./backend/src/auth/auth.py`

6: (2,3:->) [ &nbsp;] Perform changes in `./backend/src/api.py`

7: (2:->) OPTIONAL: [ &nbsp;] Add more tests in `./frontend/src/app/app.component.spec.ts`

8: (2,4:->) [X] Replace variables in `./frontend/src/environments/environment.ts`




