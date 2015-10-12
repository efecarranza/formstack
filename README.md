# formstack

This console application interacts with the Formstack API. It is a simulator of an election.

The form to register as a voter/surveyee is located at:
https://efecarranza.formstack.com/forms/product_survey_copy
but forms can be submitted using the console application as well by selecting 'Submit Vote' and following the prompts.

Existing submissions can be edited, but only the views of the surveyee can be updated, the name remains the same.

One can list all submitted forms, as well as run a simulation of an election.
Each voter has an array of values, indicating how likely they are to vote a democrat or a republican given their political views.

Tests for the application can be found under the tests folder.

# Extending the application

A way to extend the application would be to add a database connection, instead of loading all the surveys on memory.
