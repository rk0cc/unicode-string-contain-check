import unittest

import unicode_string_contain_check as uin


class TestContain(unittest.TestCase):
    def test_iscontaintc(self):
        '''
        To identify words on Trad. Chinese
        :return: Should be true
        '''
        test_target_word = "測試"
        test_phrase = "執行蟒蛇測試程式"
        self.assertTrue(uin.utf_contain(test_phrase, test_target_word))

    def test_iscontainsc(self):
        '''
        To identify words on Simp. Chinese
        :return: Should be true
        '''
        test_target_word = "语言"
        test_phrase = "同一语言有不同文字表达"
        self.assertTrue(uin.utf_contain(test_phrase, test_target_word))

    def test_iscontainjp(self):
        '''
        To identify words on Japanese
        :return: Should be true
        '''
        test_target_word = "べません"  # I just pick randomly which may not a valid word
        test_phrase = "生鮭は食べません"
        self.assertTrue(uin.utf_contain(test_phrase, test_target_word))

    def test_iscontainkr(self):
        '''
        To identify words on Korean
        :return: Should be true
        '''
        test_target_word = "피클"
        test_phrase = "김치는 피클에서 나온 부분이에요"
        self.assertTrue(uin.utf_contain(test_phrase, test_target_word))

    def test_isnotcontain(self):
        '''
        To identify words which does not contains
        :return: Should be false since `Test Mic` is not contain in the phrase
        '''
        test_target_word = "試咪"
        test_phrase = "執行蟒蛇測試程式"
        self.assertFalse(uin.utf_contain(test_phrase, test_target_word))

    def test_nonsensecompare(self):
        '''
        To check any non-sense compare blocked successfully
        :return: Catching IndexError
        '''
        with self.assertRaises(IndexError) as nonsense_test:
            test_target_word = "閔民旻閔民旻閔民旻閔民旻閔民旻閔民旻閔民旻閔民旻閔民旻閔民旻"  # Seem ridiculous but truly invalid
            test_phrase = "閔議員"
            never_reach = uin.utf_contain(test_phrase, test_target_word)  # Possibly is None object

        self.assertTrue("Target word's length should be smaller than the input" in str(nonsense_test.exception))


if __name__ == "__main__":
    unittest.main()
