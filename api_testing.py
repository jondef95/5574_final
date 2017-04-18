import unittest, mock, requests
import fact_generator as FG

api_url = ""

class TestInternalMethods(unittest.TestCase):

	def test_get_sentences(self):
		""" Tests that a sentence is split up with proper punctuation.
		"""
		test_sentences = 'This is a test sentence! It should split now. This is the end.'
		print("\nHere are the test sentences: %s" % test_sentences)
		split_sentences = FG.get_sentences(test_sentences)
		self.assertTrue(len(split_sentences) == 3)
		self.assertEqual(split_sentences[0], "This is a test sentence!")
		self.assertEqual(split_sentences[1], "It should split now.")
		self.assertEqual(split_sentences[2], "This is the end.")
		print("\n\n")


	def test_get_fact_subject(self):
		""" Tests that facts can be returned for 'Barack Obama' """
		print("\n\n")
		subject = 'Barack Obama'
		response = FG.get_fact_subject(subject)
		return_subject = response[0]
		facts = response[1]
		self.assertEqual(return_subject, 'Barack Obama')
		self.assertTrue('Obama' in facts)
		print(response)
		print("\n\n")


	def test_get_fact_subject_fail(self):
		""" Tests that an error message is returned when an invalid subject is given"""
		print("\n\n")
		subject = 'ergopoiewgporewom'
		response = FG.get_fact_subject(subject)
		return_subject = response[0]
		facts = response[1]
		self.assertEqual(return_subject, 'error')
		self.assertTrue('ergopoiewgporewom' in facts)
		print(response)
		print("\n\n")


	def test_get_fact_random(self):
		""" Tests that a message is returned with a random subject"""
		print("\n\n")
		response1 = FG.get_fact_random()
		subject1 = response1[0]

		response2 = FG.get_fact_random()
		subject2 = response2[0]

		print(subject1, "  -----  ", subject2)
		self.assertFalse(subject1 == subject2)

		print("\n\n")

class TestExternalMethods(unittest.TestCase):

	@unittest.skipIf(api_url is "", "THIS SHIT AINT HERE")
	def test_get_fact_subject(self):
		payload = {"subject":"Barack Obama"}
		response = requests.get(api_url, params=payload)


if __name__ == '__main__':
	unittest.main()
