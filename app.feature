Feature: TheMovie
  Scenario: Launch App
    Given Launch TheMovie - Application
    Then Verify the application logo.
    Then Get text of select tv label & Verify Screen Title.
    Then Tap on the selected movie.
    Then Verify Expected tv name is Correct or Incorrect.
    Then Go back to previous screen.
    Then Filter Movie by their year.
    Then Verify user filtered movie year.
    Then Filter movie by their popularity.
    Then Verify user filtered movie popularity.


