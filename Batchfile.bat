behave -f allure_behave.formatter:AllureFormatter -o Report\allure_result ./features
allure generate Report\allure_result -o Report\allure-results --clean