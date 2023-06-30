import module_to_test
import unittest

class TestModule(unittest.TestCase):
    def test_function(self):
        # Отримайте результат виклику функції, яку ви тестуєте
        result = module_to_test.function_to_test()
        
        # Перевірте, чи є результат правильним, використовуючи методи assert
        self.assertEqual(result, expected_result)

# Запустіть ваші тести, використовуючи nose2
if __name__ == '__main__':
    nose2.main()
