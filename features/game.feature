Feature: As an stakeholder I want a game to increase the knowlage
    about BDD.

    Scenario: Verify that the parameter "player" can't be sent as empty.
        When I send "" as player to the "/match" service
        Then I see a response with title "Bad Request" and status "400"

    Scenario: Verify that the parameter "player" is mandatory.
        When I don't send player as match service's parameter
        Then I see a response with title "Bad Request" and status "400"
