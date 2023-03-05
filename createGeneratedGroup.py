import mathgenerator as mg
import helper
import os
import File

# CREATES A SOLVER TEST JSON FILE FOR EACH PROBLEM GENERATED BY THE MATHGENERATOR LIBRARY
# AND PUTS THEM ALL INTO THE JSON_MATH_TESTS DIRECTORY

# IDEA: after a question is tested, keep track of if it didn't parse...
#		make a separate file that contains the variations of questions that could be asked
#		then maybe make a script to test those questions at the users discretion

if __name__ == "__main__":
	os.chdir("json_math_tests/generated")								# mathbot_testing/json_math_tests/generated

	testFile = File.TestFile("generated")
	for i in range(len(genList := mg.getGenList())):
		testFile.setSolver(solver_name=genList[i][3])
		numQuestions = 2

		for j in range(numQuestions):
			question, expected = mg.genById(i)
			testFile.addTest(question, expected)

		testFile.writeFile()

	os.chdir("../..") 									# mathbot_testing/