# rock_paper_scissors

This repo contains a small python application that represents the "Rock Paper Scissors" game and use it to illustrate some basic test automation techniques.

## Unit Test

In my opinion one of the best way to start with automation testing is from the develop stage, as soon as we can provide feedback about a specific feature it would be more easy to solve issues.

Run the flowing command to run the unit tests.

```bash
$ python setup.py test
```

This project integrates *nose* a very popular unit test framework with setuptools in order to make easy to run the test for the developers.


### nose

To get more information regarding nose please refer to the following link:

http://nose.readthedocs.io/en/latest/usage.html

### Coverage

In addition, when we run the unit test part of this project a coverage report is generated under the coverage folder.


We can define coverage like the number of lines that are cover by the unit test cases and additional information could be found in the next link:

https://coverage.readthedocs.io/en/coverage-4.5.1/

## RestAPI

This application contains an restapi to expose the logic of the game. To run this service the first step need it is to install on our system and we can do that with the following command:

```bash
$ python setup.py develop
```

After run the previous command we can use *rock_paper_scissors_restapi* command to start the service as the following example:

```bash
$ rock_paper_scissors_restapi
```

The service will run on the port 8080 and it will be accessible on the url *http://localhost:8080/match* but a swagger is ready to use on *http://localhost:8080/ui*.


### RestPAI Function test

The function test of this project was written with [lettuce](http://lettuce.it/tutorial/simple.html), to run it, first we need to install lettuce.

```bash
$ pip install lettuce
```

And then to run our function test cases we only need to run the *lettuce* command.
